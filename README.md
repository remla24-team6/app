# Description
This is the app that the user would interact with. Part of the overarching project for the CS4295 Release Engineering for Machine Learning Applications course at TU Delft.

# Use Case
![Use Case](/phishing_detection/static/use_case.png)
We provide a simple use case in our application. On receiving the result from the model, the user will be asked whether the model is correct or not. Based on this feedback, we can monitor the model's performance and we can also create more training data that is verified by the user. We will build upon this use case through this course. 

# Review information
In `phishing_detection/views.py` the three endpoints of the server are defined. The `index` method returns `index.html` along with the current version of the `lib-version` library. This version should be shown in the title of the page.

The `check` method, takes the user input, forwards it to the model_service (URL defined as env variable), and then returns this to the frontend.

The `feedback` method takes feedback from the user about whether the model is correct or not. This is used to monitor the model's performance and also create more training data from the user's feedback. The data is stored in the model service.

# Instructions

## Running without container
Instructions for running the non-containerized app are listed below. However, it is recommended to run the application using docker-compose. More instructions are present in the operations repository.

1. Run the model service locally and export the `MODEL_SERVICE_URL` environment variable to point to the model service.
2. Export both `SAVE_TRAINING_DATA_FOLDER` and `SAVE_TRAINING_DATA_FILENAME` so the app can store feedback and training data.
3. Create a virtual environment by running `virtualenv env`
4. Install the requirements using `pip install -r requirements.txt`
5. To run the app, run `python manage.py runserver`

## Metrics
We use the `django-prometheus` to support Prometheus metrics in our django app. We track the following metrics in our app -
1. feedback_received (Counter): The total amount of feedback received from users. We track this metric for both versions of our app in our experiment and use it to determine the effect of the UI on the user's interaction with the app.
2. model_performance (Gauge): The accuracy of the model determined from the feedback.
3. url_length (Histogram): The length of the URL that is checked for phishing. This can be used to detect a distribution shift in the data.
4. prediction_time (Summary): The time taken by the model to run inference for a URL.

# Release
On every push with a release tag, this repo should automatically be packaged and released.
