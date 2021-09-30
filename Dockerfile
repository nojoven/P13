#FROM python:3.9-bullseye
FROM python:3.9-alpine

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

LABEL OPCStudent: Cedric_Joseph

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt


RUN mkdir /weatwork
WORKDIR /weatwork
COPY ./weatwork /weatwork

RUN adduser -D maintainer
USER maintainer
