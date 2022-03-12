#!/bin/bash 

# Write a function task_100ms that prints 
# “task 100ms running” every time it is called 
# from the while loop
function task_100ms()
{
    echo "task 100ms running"
}

# call task_1s when 10x task_100ms has run
function task_1s()
{
    echo "task 1s running"
}

# Do the same for task_5s every 50 times
function task_5s()
{
    echo "task 5s running"
}

# Add a counter that counts up every time the while loop runs
let counter=0

# Make a while loop 
while [ : ]
do
    # that sleeps every 0.1 seconds
    sleep 0.1
    let counter++;

    if [ $(( counter % 50 )) -eq 0 ] 
    then
        task_5s
    elif [ $(( counter % 10 )) -eq 0 ] 
    then
        task_1s
    else
        task_100ms
    fi
done

# Edit the rights to the file to make the file executable
# chmod +x scheduler.sh

# run file
# ./scheduler.sh
