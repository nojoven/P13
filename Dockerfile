#FROM python:3.9-bullseye
FROM python:3.9-alpine

RUN apk update && apk add make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
RUN apk add jpeg-dev

LABEL OPCStudent: Cedric_Joseph

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev postgresql-dev

RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /weatwork
WORKDIR /weatwork
COPY ./weatwork /weatwork

RUN adduser -D maintainer
USER maintainer
