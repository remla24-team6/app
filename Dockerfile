FROM python:3.12

RUN python3 -m venv /opt/venv

RUN . /opt/venv/bin/activate && pip install django numpy

COPY . .

# Without this line, django doesnt work. idk
ENV PYTHONUNBUFFERED=1

CMD . /opt/venv/bin/activate && python manage.py runserver