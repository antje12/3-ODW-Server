FROM ubuntu

COPY L6E1/ /home/

RUN apt-get update
RUN apt-get -y install python3
RUN python3 /home/fibonacci.py

CMD python3 /home/fibonacci.py

# docker build -t fib .
# docker run fib
# docker run --cpus=0.4 fib
# docker run --cpus=8 fib
