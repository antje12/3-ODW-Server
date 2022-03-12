#!/bin/bash 

# create a new network
docker network create my-net

# Write a bash script that starts 10 containers. 
# Using a for loop is advisable.
for i in {1..10}
do
    # The names of the 10 containers should be 
    # bash_container_1, bash_container_2 and so on.
    name="bash_container_$i"
    
    # -d=true => start as detached / run in background
    # --network my-net => connect it to my-net 
        # using default "bridge" connection type
    # .it => interactive (to keep it running)
    docker run --name $name -d=true --network my-net -it ubuntu
done

# Edit the rights to the file to make the file executable
# chmod +x scheduler.sh

# run file
# ./container-starter.sh

# docker ps
# docker network inspect my-net
