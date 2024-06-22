from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from versioning_remla.versioning import VersionUtil
import requests
import os
import json
from .metrics import predict_requests, num_correct

def index(request):
    return render(request, 'index.html', {'version': VersionUtil().get_version()})

def check(request):
    test_url = json.loads(request.body.decode('utf-8')).get('test_url')
    MODEL_SERVICE_URL = os.getenv('MODEL_SERVICE_URL', 'http://no-url-add-env')
    # response = requests.post(settings.MODEL_SERVICE_URL + "/predict", json={'data': [test_url]})
    response = requests.post(MODEL_SERVICE_URL + "/predict", json={'data': [test_url]})
    prediction = response.json().get('prediction')
    print(prediction)
    is_phishing = prediction[0] == 1
    predict_requests.inc()
    return JsonResponse({'is_phishing': is_phishing})

def feedback(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        url = data.get('url')
        is_phishing = data.get('label')
        feedback_result = data.get('feedback')
        
        print(f'url {url} with label { is_phishing} has feedback {feedback_result}')
        
        if url is None or is_phishing is None or feedback_result is None:
            return HttpResponseBadRequest("URL, is_phishing, and feedback_result are required.")
        
        if int(feedback_result) == 1:
            num_correct.inc()
            
        json_msg = {
            'url': url,
            'label': int(is_phishing),
            'feedback': feedback_result
        }
        
        response = requests.post(settings.MODEL_SERVICE_URL + "/add", json=json_msg)
        result = response.json().get('msg')
    
        # Here you can add logic to handle the feedback, e.g., logging it or updating your model
        # For now, we'll just return a success message
        return JsonResponse({'message': 'Feedback received successfully', 'feedback_result': feedback_result})
    except (json.JSONDecodeError, KeyError):
        return HttpResponseBadRequest("Invalid JSON data.")
    except requests.RequestException as e:
        return HttpResponseBadRequest(f"Error processing feedback: {e}")
    