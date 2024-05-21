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

## Running Locally
1. Run the model service locally and export the `MODEL_SERVICE_URL` environment variable to point to the model service.
2. Create a virtual environment by running `virtualenv env`
3. Install the requirements using `pip install -r requirements.txt`
4. To run the app, run `python manage.py runserver`

## Running using Docker
1. Pull the latest image using `docker pull ghcr.io/remla24-team6/app:latest`
2. Run the image `docker run -t -i --network host -p 8000:8000 app`


# Release
On every push with a release tag, this repo should automatically be packaged and released.
