from prometheus_client import Counter

predict_requests = Counter('num_predict_requests', 'Number of requests receieved by the model')
num_correct = Counter('num_feedback_correct', 'Number of times the feedback is correct by the user.')