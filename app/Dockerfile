FROM python:3.11-slim

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE "config.settings"

COPY requirements.txt requirements.txt

RUN mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
