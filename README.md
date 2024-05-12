# Description
This is the app that the user would interact with. Part of the overarching project for the CS4295 Release Engineering for Machine Learning Applications course at TU Delft.

# Review information
In `phishing_detection/views.py` the two endpoints of the server are defined. The `index` method returns `index.html` along with the current version of the library. This version should be shown in the title of the page.

The `check` method, takes the user input, forwards it to the model_service (URL defined as env variable), and then returns this to the frontend.

# Instructions
Note: These are only instructions for building and running this container. Instructions for running the entire system are in the operations repo.

to build:
```
docker build -t app .
```

to run:
```
docker run -t -i --network host -p 8000:8000 app
```


# Release

On every push with a release tag, this repo should automatically be packaged and released.
