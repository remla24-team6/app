from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from versioning_remla.versioning import VersionUtil
import requests
import json
from time import time
from .metrics import feedback_received, model_performance, url_length, model_time_taken
from .utils import add_feedback_and_get_new_accuracy
import os


def index(request):
    return render(request, "index.html", {"version": VersionUtil().get_version()})


def check(request):
    test_url = json.loads(request.body.decode("utf-8")).get("test_url")

    MODEL_SERVICE_URL = os.getenv("MODEL_SERVICE_URL", "http://no-url-add-env")
    start_time = time()
    response = requests.post(MODEL_SERVICE_URL + "/predict", json={"data": [test_url]})
    time_taken = time() - start_time

    # Observe the length in the histogram
    url_length.observe(len(test_url))
    
    # Observe the time taken in the summary
    model_time_taken.observe(time_taken)

    prediction = response.json().get("prediction")
    print(prediction)
    is_phishing = prediction[0] == 1

    return JsonResponse({"is_phishing": is_phishing})


def feedback(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        url = data.get("url")
        is_phishing = data.get("label")
        feedback_result = data.get("feedback")

        print(f"url {url} with label { is_phishing} has feedback {feedback_result}")
        

        if url is None or is_phishing is None or feedback_result is None:
            return HttpResponseBadRequest(
                "URL, is_phishing, and feedback_result are required."
            )

        json_msg = {"url": url, "label": int(is_phishing), "feedback": feedback_result}

        # Update feedback in the training data and get the new accuracy
        new_accuracy = add_feedback_and_get_new_accuracy(
            url, int(is_phishing), feedback_result
        )
        
        # Increment the total feedback received.
        feedback_received.inc()
        model_performance.set(new_accuracy)
        
        # Here you can add logic to handle the feedback, e.g., logging it or updating your model
        # For now, we'll just return a success message
        return JsonResponse(
            {
                "message": "Feedback received successfully",
                "feedback_result": feedback_result,
            }
        )
    except (json.JSONDecodeError, KeyError):
        return HttpResponseBadRequest("Invalid JSON data.")
    except requests.RequestException as e:
        return HttpResponseBadRequest(f"Error processing feedback: {e}")
