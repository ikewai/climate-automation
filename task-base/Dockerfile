FROM ubuntu:20.04

RUN apt update

RUN apt install -y python3 python3-pip
RUN apt install -y wget

RUN python3 -m pip install tapipy agavepy

COPY ./actor/ actor/
COPY ./docker-build/ docker-build/.