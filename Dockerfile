#FROM python:3.9-bullseye
FROM python:3.9-alpine
LABEL OPCStudent: Cedric_Joseph

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    pip install --no-cache-dir cryptography==2.1.4 && \
    apk del \
        libressl-dev \
        musl-dev \
        libffi-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt


RUN mkdir /weatwork
WORKDIR /weatwork
COPY ./weatwork /weatwork

RUN adduser -D maintainer
USER maintainer
