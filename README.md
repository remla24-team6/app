# Description
This is the frontend server that the user would interact with. Part of the overarching project for the CS4295 Release Engineering for Machine Learning Applications course at TU Delft.

# Instructions

to build:
```
docker build -t app .
```

to run:
```
docker run -t -i --network host -p 8000:8000 app
```

# Release

On every push, this repo should automatically be packaged and released to `ghcr.io`