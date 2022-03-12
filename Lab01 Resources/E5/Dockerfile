FROM ubuntu

COPY L1E5/ /home/

RUN apt-get update
RUN apt-get -y install python3
RUN python3 -u /home/count.py

CMD bash

