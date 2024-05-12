from django.shortcuts import render
from django.http import JsonResponse
from versioning_remla.versioning import VersionUtil
import requests
import os
import json


def index(request):
    return render(request, 'index.html', {'version': VersionUtil().get_version()})

def check(request):
    test_url = json.loads(request.body)['test_url']
    print(test_url)
    response = requests.post(os.environ['MODEL_SERVICE_URL'] + "/predict", json={'data': [test_url]})
    prediction = response.json().get('prediction')
    print(prediction)
    is_phishing = prediction[0] == 1
    return JsonResponse({'is_phishing': is_phishing})


