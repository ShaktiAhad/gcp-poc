FROM jenkin-with-python3-pip3-n-gcp-cli:latest
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y 
# RUN apt-get install python3-pip -y
RUN curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-387.0.0-linux-x86_64.tar.gz
RUN tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/
RUN sh /tmp/google-cloud-sdk/install.sh -q
ENV PATH="/tmp/google-cloud-sdk/bin:${PATH}"

# docker run --name jenkin -v /Users/ahadnoor.shakti/jenkin_home:/var/jenkins_home -p $(ipconfig getifaddr en0):8080:8080
# docker build --no-cache -t gcp .
# ipconfig getifaddr en0
# echo $PATH