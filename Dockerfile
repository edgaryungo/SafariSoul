FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY app/ /app

WORKDIR /app

RUN adduser --disabled-password --gecos "" --no-create-home django_user

USER django_user

# CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "app.wsgi"]