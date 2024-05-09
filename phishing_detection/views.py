from django.shortcuts import render
from django.http import JsonResponse
import numpy as np


def index(request):
    return render(request, 'index.html')

def check(request):
    result = np.random.randint(1, 100) > 50
    return JsonResponse({'is_phishing': result})


