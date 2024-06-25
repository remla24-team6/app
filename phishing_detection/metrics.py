from prometheus_client import Counter, Histogram, Gauge, Summary

feedback_received = Counter("feedback_received", "The total amount of feedback received from users.")
model_performance = Gauge(
    "model_performance", "The accuracy of the model detemined from the feedback."
)
url_length = Histogram(
    "url_length",
    "The length of the URL that is checked for phishing. This can be used to detect a distribution shift in the data.",
)
model_time_taken = Summary(
    "prediction_time",
    "The time taken by the model to run inference for a URL.",
)

