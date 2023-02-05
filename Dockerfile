FROM python:3.10-alpine
LABEL maintainer="philipkogel"

COPY ./requirements.txt /app/requirements.txt
COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt