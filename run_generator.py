FROM ubuntu:20.04 as npm_build

## Install docker
RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y apt-transport-https ca-certificates curl software-properties-common build-essential && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" && \
    apt-get update && \
    apt-get install -y docker-ce
