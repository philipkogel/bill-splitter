FROM python:3.10-alpine
LABEL maintainer="philipkogel"

COPY ./requirements.txt /app/requirements.txt
COPY ./app /app

WORKDIR /app

RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r requirements.txt