#!/bin/bash 

# Write a bash script that stops 10 containers. 
# Using a for loop is advisable.
for i in {1..10}
do
    # The names of the 10 containers should be 
    # bash_container_1, bash_container_2 and so on.
    name="bash_container_$i"

    docker rm $name -f
done

# stop the new network
docker network rm my-net

# Edit the rights to the file to make the file executable
# chmod +x scheduler.sh

# run file
# ./container-stopper.sh

# docker ps
# docker network inspect my-net
