#Dockerfile for server1.py
FROM python:3.7.1

LABEL Author="Tochukwu Nwoko"
LABEL E-mail="nwokotochukwu@gmail.com"
LABEL version="0.0.1b"

RUN mkdir /app
WORKDIR /app

COPY  . /app


RUN   pip install -U Flask


ADD . /app

EXPOSE 8000

CMD py server1.py
