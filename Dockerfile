#FROM python:3.9-bullseye
FROM python:3.9-alpine

RUN apk update && apk add make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
RUN apk add jpeg-dev

LABEL OPCStudent: Cedric_Joseph


ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install wheel
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-libs postgresql-dev musl-dev zlib zlib-dev
RUN pip3 uninstall psycopg2
RUN pip3 list --outdated
RUN pip3 install --upgrade wheel
RUN pip3 install --upgrade setuptools
#RUN pip3 install psycopg2==2.9.1

RUN pip3 install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /weatwork
WORKDIR /weatwork
COPY ./weatwork /weatwork

RUN adduser -D maintainer
USER maintainer
