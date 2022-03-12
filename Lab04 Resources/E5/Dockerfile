FROM python:3

RUN apt-get update
#RUN apt-get -y install python3
RUN pip3 install Flask
RUN pip3 install requests

COPY Python/ /home/
CMD python3 /home/E5.py

# $ docker build -t pytest .
# $ docker run -p 7000:5000 pytest
