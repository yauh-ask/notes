Docker file explanation

The Compose file is in YAML format. It’s a very simple language. You can validate your YAML file using any of the online validator tools.
[YAML Checker](https://yamlchecker.com/) Sup, YAML of Docker-compose:

- version ‘3’: Like other software, docker-compose also started with a version 1.0. Compose versions are backwards compatible, 
hence I suggest you use the latest version.

- services: The services section defines all the different containers to be created; e.g. web and database.

- web: This is the name of our Flask app service. It can be anything. Docker Compose will create containers with this name.

- build: This clause specifies the Dockerfile location. ‘.’ represents the current directory where the docker-compose.yml file is located 
and Dockerfile is used to build an image and run the container from it. We can also enter a path to Dockerfile there.

- ports: The ports clause is used to map or expose the container ports to the host machine. 
If you remember, we used -p 5000:5000 while running the container using Docker. This will do the same work for us.

- volumes: This is the same as the -v option used to mount disks in Docker. Here, we are attaching our code files directory to the containers,
./code directory so that we don’t have to rebuild the images for every change in the files.

This will also help in auto-reloading the server when running in debug mode.

- links: Links literally links one service to another. In the bridge network, we have to specify which container should be accessible to which container using
a link to respective containers,eg linking the database container to the web container, so that our web container can reach the database in the bridge network.

- image: If we don’t have a Dockerfile and want to run a service directly using an already built image, we can specify the image location using the ‘image’
clause. Compose will pull the image and fork a container from it.

- environment: Any environment variable that needs to be set up in the container can be created using the ‘environment’ clause.
This does the same work as the -e argument in Docker while running a container.

All the clauses or keywords above are commonly used keywords, which are enough to start a development workflow. 

`docker-compose build`
This command builds images of the mentioned services in the docker-compose.yml file for which a Dockerfile is provided.
The job of the ‘build’ command is to get the images ready to create containers. If a service is using the prebuilt image, it will skip that service.

`docker-compose images`
This command lists images built using the current docker-compose file.

`docker-compose run`
Similar to docker run command, this one creates containers from images built for the services mentioned in the compose file.
It runs a specific service provided as an argument to the command.

`docker-compose up`
This does the job of the docker-compose build and docker-compose run commands. It initially builds the images if they are not located locally and then starts the containers.If images are already built, it will fork the container directly. We can force it to rebuild the image by adding a --build argument.



Priority of .env variables
There are multiple ways we can use the environment variables in Docker, which includes,

ENV in Dockerfile
environment keyword in docker-compsoe.yml file
-e option from the command line

So, docker-compose has precedence levels to overcome the clash of variables. Let’s see those.

When you set the same environment variable in multiple files, here’s the priority used by Compose to choose which value to use:

Compose file
Shell environment variables
Environment file
Dockerfile
Variable is not defined

So, if we define a variable in the Compose file in the - environment section and also in a .env file, Compose will consider the variable declared in the Compose file from -environment section.
