FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip bash openssl ca-certificates  \
    && pip3 install --upgrade pip \
    && pip3 install ipython

RUN mkdir -p /igp

COPY . /igp

WORKDIR /igp

RUN pip3 install -r requirements.txt