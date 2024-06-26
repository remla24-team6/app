# Description
This is the app that the user would interact with. Part of the overarching project for the CS4295 Release Engineering for Machine Learning Applications course at TU Delft.

# Use Case
![Use Case](/phishing_detection/static/use_case.png)
We provide a simple use case in our application. On receiving the result from the model, the user will be asked whether the model is correct or not. Based on this feedback, we can monitor the model's performance and we can also create more training data that is verified by the user. We will build upon this use case through this course. 

# Review information
In `phishing_detection/views.py` the three endpoints of the server are defined. The `index` method returns `index.html` along with the current version of the library. This version should be shown in the title of the page.

The `check` method, takes the user input, forwards it to the model_service (URL defined as env variable), and then returns this to the frontend.

The `feedback` method takes feedback from the user about whether the model is correct or not. This is used to monitor the model's performance and also create more training data from the user's feedback. The data is stored in the model service.

# Instructions
Note: These are only instructions for building and running this repository locally. Instructions for running the entire system are in the operations repo.

## Running without container
Instructions for running the non-containerized app are listed below. However, it is recommended to run the application using docker-compose. More instructions are present in the operations repository.

1. Run the model service locally and export the `MODEL_SERVICE_URL` environment variable to point to the model service.
2. Export both `SAVE_TRAINING_DATA_FOLDER` and `SAVE_TRAINING_DATA_FILENAME` so the app can store feedback and training data.
3. Create a virtual environment by running `virtualenv env`
4. Install the requirements using `pip install -r requirements.txt`
5. To run the app, run `python manage.py runserver`

## Prometheus Metrics
1. num_feedback_correct (Counter): This metric counts the number of correct model outputs based on user feedback.
2. predict_requests (Counter): This metric counts the total number of requests received by the /predict endpoint.

# Release
On every push with a release tag, this repo should automatically be packaged and released.
