#FROM python:3.9-bullseye
FROM python:3.9-alpine
LABEL OPCStudent: Cedric_Joseph

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv


RUN mkdir /weatwork
WORKDIR /weatwork
COPY ./weatwork /weatwork

RUN adduser -D maintainer
USER maintainer
