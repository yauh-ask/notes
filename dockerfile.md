The Docker engine executes all commands on your behalf, but we need to tell Docker what commands we want to execute. 
So, Docker has something called a Dockerfile. All the steps mentioned in the Dockerfile are executed step by step.

Docker isolates the code environment from the host machine using containers and containers are the instances of the image.
In a programming language, this Dockerfile will provide us with a blueprint also called an image, from which we can run our app in a container.



Example:

FROM python:3.9-rc-buster

Setting up Docker environment:  WORKDIR /code

Export env variables:

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

Copy requirements file from current directory to file in containers code directory we have just created:

COPY requirements.txt requirements.txt

Run and install all required modules in container:

RUN pip3 install -r requirements.txt

Copy current directory files to containers code directory:
COPY . .

RUN app.
CMD ["flask", "run"]

#### To recap

FROM #
The FROM keyword tells Docker which base image to use or what should be the main platform for this image.

The Python:3.9-rc-buster image is a Linux-based image which has Python installed and no other additional programs or software.

WORKDIR #
The WORKDIR instruction sets a working directory for other Docker instructions such as RUN and CMD.

If we do not specify a working directory, we have to provide a full path for running our app.py file while using the RUN instruction.

ENV #
The ENV instruction sets an environment variable required for the flask app. We can skip these ENV steps, but you have to provide those variables using .flaskenv file.

Here, we are setting host to 0.0.0.0 which means we can access the app using any IP within the container.

Setting up a host to 0.0.0.0 is required if you are running the app inside the container and want to access it outside. If you change it to anything else, you won’t be able to access the app from the host machine.

COPY #
The COPY instruction literally copies the file from one location to another. COPY SOURCE DESTINATION is the syntax of the command.

Here, we are copying the requirements.txt file first so that we will have all the libraries installed before copying all the files.

RUN #
The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.

In the previous section, we learnt about layers. The RUN instruction creates a new layer here. It runs the commands provided as an argument in that layer.

One benefit of running requirements before copying all the files is whenever a change occurs in project files, we don’t have to build requirements again and Docker will use a cached layer for requirements.

CMD #
CMD runs the command inside the container once a container is forked or created from an image. You can only have one CMD instruction in a Dockerfile. If multiple CMD instructions are used, the last one will be executed.

Here, once the container is created, the CMD command will run our project.

We have one more frequently-used instruction.

ENTRYPOINT #
The ENTRYPOINT instruction can be used if you want to configure your container as an executable. If you want to override CMD while running a container, use ENTRYPOINT,

for example, ENTRYPOINT [“flask”, “run”]


Now: cd into the directory where the Dockerfile is located. Type `docker build -t flask_app:1.0 .`

> The last ‘.’ in the command is very important. It denotes the current directory or location of the Dockerfile to use for building the image.


#### port mapping

to run the container `docker run flask_app:1.0`
with the option `docker run -p 5000:5000 flask_app:1.0`

Before adding this option, the app was running in the container on the container’s 5000 port. 
There is no way the host machine will reach into the container. 
However, the -p 5000:5000 option will create a pipe/tunnel on the host machine’s 5000 port to the container’s 5000 port. 
This is called port mapping. You can create interfaces to establish communication between host and container.

#### managing data
Mounting a filesystem onto the container.Type pwd to get the absolute path to ‘Docker’ directory. Next, add one more option to the docker run command,

`docker run -it -v <host_absolute_path>:<folder path in container> -p 5000:5000 flask_app:1.0`

For example, `docker run -it -v /Users/venkateshachintalwar/Documents/Online_Projects/Docker:/code -p 5000:5000 flask_app:1.0`

### Daemon mode
Instead of running a container in interactive shell mode (-it option stands for -i - Interactive, -t TTY terminal) of the container, it can be run as a background process. Means, docker container will run in the background completely detached from the shell of the host machine.

This way, the shell or the terminal will not be locked and other commands can be executed on the same shell. To run the container in daemon mode, use -d option while running or creating the container from the image.

Example: docker run -d -v <path_to_code_directory>:/code -p 5000:5000 flask_app:1.0

This will print the container id something like this: 9ffc383cf193af15ff4daa744db5a58f1cdc85b9b51d09f096aa4c591dc24d6b

To get back into the container, Type `docker exec -it <container id> bash`. 
This will attach the shell of the container to the host terminal. docker exec is used to execute commands from the running container.

You can also directly attach the container running in detached mode to the shell using `docker attach <container id>`. 
But you will not see any output as no process in the container is printing to stdout of the container.
And the container will continue running in the background. The id is a full SHA256 digest of the container.


#### container logs
`docker logs <CONTAINER ID>`

real-time: `docker logs -f <CONTAINER ID>`
