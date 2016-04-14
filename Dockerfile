FROM ubuntu:trusty

MAINTAINER Joel James <joel.james1985@gmail.com>

## Install Build Tools
RUN apt-get update && \
    apt-get install -y build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


## Add User
RUN useradd -ms /bin/bash app
RUN adduser app sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chmod 4755 /usr/bin/sudo
ENV HOME /home/app


## Install Python3 Tools and Postgres Tools
RUN apt-get update && \
    apt-get install -y wget python3-pip python3-dev python3-software-properties && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8000

# Don't run application as root
USER app

# Install Python dependencies
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN sudo pip3 install -r requirements.txt

ADD . /usr/src/app
RUN sudo chown -R app /usr/src/app
