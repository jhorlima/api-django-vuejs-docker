FROM python:3
#FROM python:3-alpine

MAINTAINER Jhordan Lima "jhordan.lima@niduu.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/