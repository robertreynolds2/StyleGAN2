FROM ubuntu:20.04

RUN apt-get update
RUN free -h
RUN lscpu
RUN echo $(egrep '^flags.*(vmx|svm)' /proc/cpuinfo | wc -l)
