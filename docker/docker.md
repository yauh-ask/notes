# What is Docker?
- Docker is an engine that allows you to run containers. Containers have many advantages, including:

    - Code and dependancies are packaged together, so software runs more reliably in different environments
    - Containers are a standard unit of software
    - As standalone executable packages, containers include everything needed to run the application
    - Containers are lightweight in comparison to virtual machines
    
 
## Dockerfile
- Text document that contains all the commands and instructions necessary to build a Docker Image. See [here](https://docs.docker.com/engine/reference/builder/) a Dockerfile Reference

## Docker Image
- Executable packages comprised of code, dependancies, libraries, a runtime, environment variables, and configuration files. 
Very similar to a virtual machine snapshot. Basically, the app is packaged with libraries and binaries required by it. But how does Docker achieve this packaging?

Docker provides the facility to create a custom image on top of the Linux kernel with your app and its libraries. The image is a blueprint of the container and the container is created from it.

For simplicity, if you take this from an object-oriented programming point of view, an image is a class, where all the requirements are defined and declared. A container is an instance of the image. These images are stored somewhere in the cloud and pulled as needed.

## Docker Container
- A runtime instance of a Docker Image. This is what the image becomes when executed in memory.

A container is an instance of an image, which simulates the required environment with the use of the Linux kernel packaged in it. In the diagram, you can see app B is enclosed in one container. Similarly, you can enclose the other two apps as well.

You might ask, how a container provides the required environment with isolation if it shares the OS kernel. Well, that is done with the help of images.

Let’s take an example here. If your app only needs Python 3.5 from the system, you will only need that in your production environment as a dependency. Everything else will be an extra overhead. So, Docker provides the template built on the Linux kernel with the needed dependencies only and nothing is installed in that template. That template is called an image.

So, if you fetch a Python 3.5 image from Docker and run an instance of it, you can do whatever you were able to do in the host machine using a command line interface. If you make any mistake with that instance, you can delete the container and create a new one from the existing image. This way, your main environment remains intact in the form of an image and you can play around with the dependencies packaged in the image using containers.

[Resources](https://docs.docker.com/get-started/)


### Docker ecosystem
- Docker Registry: Docker maintains all the images in the registry and they can be pulled from the registry too

- Docker Hub: This is the repository for all your custom-built images. Images can be pushed and accessed from the Hub

- Docker Client: The CLI tool used to interact with the Docker server

- Docker Daemon: The Docker server process responsible for pulling, pushing, and building the images. It is also used for running the container

### `docker run hello-world`

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

