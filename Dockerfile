FROM python:rc-buster

RUN apt-get update
RUN apt-get install -y python3 python3-pip wget golang git

RUN pip3 install flask flask_cors

WORKDIR /script
RUN wget https://raw.githubusercontent.com/fumiyas/home-commands/master/echo-sd
RUN chmod +x echo-sd

RUN go get -u github.com/greymd/ojichat

