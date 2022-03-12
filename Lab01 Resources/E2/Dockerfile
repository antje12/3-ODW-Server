# A Dockerfile often begins with the FROM instruction, telling the Docker engine which image this image is built from.
# In this case ubuntu is used as the argument.
FROM ubuntu

# The RUN instruction is an instruction that takes a BASH command as argument. In this way simple functionality is included in the Dockerfile.
# In this case, the text “Hello, World!” is inserted into a txt-file called ‘helloWorld’.
RUN echo “Hello, World! 42.” > helloWorld.txt

# The CMD instruction is the instruction that determines the container's lifetime. This instruction is not runned when building the image. When a container is spinned up from an image, the following command is runned as the executing command. When the command finishes its execution, the container will shut down.
# In this case, the text inside the ‘helloWorld.txt’-file is printed to the screen.
CMD cat helloWorld.txt

