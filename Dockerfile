FROM python:3.12

RUN pip install django numpy versioning-remla

COPY . .

# Without this line, django doesnt work. idk
ENV PYTHONUNBUFFERED=1