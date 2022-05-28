FROM jenkins/jenkins:latest
USER root
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
# docker build --no-cache -t jenkin .
# cf199abc1e8643a398a8ec6b6bb2e42a
# 192.168.0.169:8080