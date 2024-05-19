from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from versioning_remla.versioning import VersionUtil
import requests
import os
import json

def index(request):
    return render(request, 'index.html', {'version': VersionUtil().get_version()})

def check(request):
    test_url = json.loads(request.body.decode('utf-8')).get('test_url')

    response = requests.post(settings.MODEL_SERVICE_URL + "/predict", json={'data': [test_url]})
    prediction = response.json().get('prediction')
    print(prediction)
    is_phishing = prediction[0] == 1
    return JsonResponse({'is_phishing': is_phishing})


def add_training(request):
    data = json.loads(request.body.decode('utf-8'))
    new_url = data.get('url')
    label = data.get('label')
    response = requests.post(settings.MODEL_SERVICE_URL + "/add", json={'url': new_url,
                                                                'label': label})
    result = response.json().get('msg')
    # Add logic to save the new URL and label to your training data
    return JsonResponse({'message': result})