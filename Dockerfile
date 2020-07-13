FROM ubuntu:20.04
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN apt-get update \
    && apt-get install -y libssl-dev libpq-dev \
    && apt-get install -y default-libmysqlclient-dev python3-pip
RUN pip3 install -r requirements.txt