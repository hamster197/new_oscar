FROM python:3.6

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt