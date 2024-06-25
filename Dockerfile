FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Without this line, django doesnt work. idk
ENV PYTHONUNBUFFERED=1
