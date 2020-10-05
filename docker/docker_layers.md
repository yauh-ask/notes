As every image is built on top of Linux kernel, it has some common dependencies that can be reused by other images. 
Docker bundles these dependencies in one stack and these stacks are called layers.

> Only the instructions RUN, COPY, and ADD create layers. Other instructions create temporary intermediate images and do not increase the size of the build.

Docker caches these intermediate layers to speed up the image building process. 

Commands:

docker pull \<images-name>:\<version> : pulls image from Docker registry
docker run \<images-name>:\<version> : runs container from mentioned image
docker ps : shows all running containers
docker ps -a: shows all available containers
docker exec: executes a command in a running container

`docker run -it <container name> <command to execute>` : to get the shell, we will execute bash as a command. 
The options i & t are used to provide an interactive mode and a pseudo tty terminal.

> Make sure you work with the same container every time. If the container is stopped start it using the `docker start <container_id/name>` command and work in it using `docker exec -it <container_id/name> bash` command.

### Commiting Images

What is the use of commit? Sharing code with someone else with a different environment can lead to bugs.

When you commit the container, a new image is created and you can push that image to the registry. 
Anybody can fetch the image and will have the same code with a consistent environment. This also helps in deployment as well.
To commit the container by `$docker commit -m "<commit message>" <container_id/name> <new_image_name>:<version>`.

Push your image to your Docker Hub account so that anybody can access it. Steps to push:

1. Docker login

2. Docker tag <image_name> <your_docker_hub_username>/<image>:<version>

3. Docker push <your_docker_hub_username>/<image>:<version>

