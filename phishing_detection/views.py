from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from versioning_remla.versioning import VersionUtil


def index(request):
    return render(request, 'index.html', {'version': VersionUtil().get_version()})

def check(request):
    result = np.random.randint(1, 100) > 50
    return JsonResponse({'is_phishing': result})


