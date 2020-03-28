#!IMAGE mobi/patient-hospital-optimization

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    libaio-dev \
    nginx \
    sudo # to ease debugging

RUN apt-get update && apt-get install -y \
    curl \
    python3.5 \
    python3-pip \
    wget

RUN pip3 install \
    flask==0.10.1 \
    eventlet==0.21.0 \
    gunicorn==19.6.0 \
    psycopg2==2.6.1 \
    requests==2.8.1 \
    pandas==0.23.0 \
    boto3==1.9.39 \
    flask_cors==3.0.7 \
    python-jose==3.0.1 \
    auth0-python==3.6.1 \
    iso8601==0.1.12


# Create user "mobi"
RUN adduser --disabled-password --gecos '' mobi \
    && adduser mobi sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
# Switch user at the end so files created in previous steps belong to root


RUN mkdir /mobi
WORKDIR /mobi

COPY . /mobi/src

USER mobi

# Change the owner so all scripts can be run as user "mobi"
RUN sudo chown -R mobi:mobi /mobi

RUN touch /mobi/__init__.py

WORKDIR /mobi

ENV PYTHONPATH /

EXPOSE 8080