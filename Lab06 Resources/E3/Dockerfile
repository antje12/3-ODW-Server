FROM ubuntu

COPY L6E3/ /home/

RUN apt-get update
RUN apt-get -y install python3
RUN python3 /home/mem-user.py

CMD python3 /home/mem-user.py

# docker build -t mem .
# docker run mem
# docker run --memory=200m mem
# docker run --memory-swap=1g -m=200m
