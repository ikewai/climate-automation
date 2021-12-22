FROM ubuntu:20.04

RUN apt update

RUN apt install -y python3 python3-pip
RUN apt install wget

RUN python3 -m pip install tapipy

COPY ./actor/ actor/