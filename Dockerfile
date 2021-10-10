FROM ubuntu:20.04

FROM tensorflow/tensorflow:1.14.0-gpu-py3

RUN apt-get update
RUN free -h
RUN lscpu
RUN echo $(egrep '^flags.*(vmx|svm)' /proc/cpuinfo | wc -l)
