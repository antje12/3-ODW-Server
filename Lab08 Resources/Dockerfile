FROM ubuntu

# copy the files
COPY Resources/ /home/

RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install htop

# change folder
WORKDIR "/home"

# compile the c files using make 
# and gcc (GNU C compiler).
RUN make -f makefile

# docker build -t compiler .
# docker run -it compiler /bin/bash

# ./code1
# ./code2
# ./code3
# ./code4
# run code 5 in background and watch the cpu usage
# ./code5 &
# htop
