What is container orchestration?

Suppose you have developed a wonderful application which will be used by millions of users. 
How will it be deployed efficiently without having a single point failure to handle a large number of requests?

Managing systems at large scale very difficult. Millions of containers run on different machines.
How will you track which container has stopped or which service is no longer running?

Managing this cluster of containers effectively is called container orchestration. 
At present, there are three major tools available that help in container orchestration namely, Docker swarm, Kubernetes, and Apache Mesos.

What is Docker swarm?
Docker swarm is a container orchestration tool that allows a user to manage multiple containers deployed across multiple host machines. 
Docker swarm has different components which helps it to manage the swarm effectively. Let’s have a look at the architecture to understand how it works.

Docker swarm architecture

A worker node is something on which tasks are created by the manager. 
It will have services running on it to maintain the state defined in the YAML file.

In this architecture, there is only one YAML file. That’s the power of the YAML file. 
A stack of services is created and deployed on each worker node using the YAML file.

A node is a machine. It can act as a manager, worker, or both. 
We can also have multiple manager nodes but there will always be a primary node to manage the swarm cluster.

Characteristics of the manager node include:

1) It always knows the exact state of the cluster

2) It is responsible for maintaining the state of the cluster described in the YAML file

3) It creates the different tasks on worker nodes to maintain the desired service state.

4) It keeps backups in case if a node fails and, starts new containers from backups on available nodes to maintain the count of containers

Let’s understand each component of the architecture.

Building blocks of Docker swarm 

A swarm cluster can have the following components:

Node: The node is the host machine. A machine can act as a worker, manager, or both. 
We can have a swarm with one node as well. In that case, the respective machine acts as both a worker and manager nodes.
For example, In a cluster of 5 computers, each computer will be a node. And there will be a master computer which is responsible for 
the communication of the Cluster.

Stack: A set of services combined is called a stack. Stack and Compose work somewhat similarly, except, there are some commands which 
will be ignored by docker-compose in a non-swarm mode such as deploy.
For example, when we want to deploy our whole project which is a collection of services (like web server, database and maybe a task queue) in a single command; 
we declare all the services in a YAML file and that YAML file is now a stack of services for the swarm manager. Swarm manager will deploy the stack and maintain
the desired states of services defined in the YAML file.

Service: A service is the definition of the tasks to execute on the manager or worker nodes. It is the central structure of the swarm system and the primary 
root of user interaction with the swarm. When you create a service, you specify which container image to use and which commands to execute inside running 
containers.
For example, The flask app we created earlier is a service. Why? Because we are using flask_app:2.0 docker image which will be running in a container 
with the command to run the WSGI server.

Task: Task is responsible for maintaining the desired replica set of the service. To deploy a service on a worker node, swarm manager creates a task and starts 
a container in it.
For instance, you define a service that instructs the swarm manager to keep three instances of an HTTP listener running at all times. The orchestrator 
responds by creating three tasks. Each task is a slot that the scheduler fills by spawning a container. The container is the instantiation of the task. If an 
HTTP listener task subsequently fails its health check or crashes, the orchestrator creates a new replica task that spawns a new container.

A task is a one-directional mechanism. It progresses monotonically through a series of states: assigned, prepared, running, etc.
If the task fails the orchestrator removes the task and its container and then creates a new task to replace it according to the desired state 
specified by the service.


Initializing the swarm node

If you are using the Docker Desktop for Windows or for Mac, Docker swarm comes prebuilt. You can check that using docker swarm -v. To initialize the swarm mode, 
type `docker swarm init`.

The node you started will be a manager node. We can add other machines or hosts to this swarm network using the command above with the provided token. But for now, we will see all the operations on a single worker-manager node only.

Creating services #
Like we have created containers using docker run command, a service does the same thing for a swarm cluster.

docker service create <service name> allows us to create a service on swarm with a defined number of containers in it.

Our aim is to create a load-balanced Flask app service and attach a database to it.
Swarm cluster only works with prebuilt images. This means we cannot build an image using a Dockerfile while creating a container. 
So, we have to build the image of our app first and then  create a service from it.

Process
Type docker service create -p 5000:5000 flask_app:3.0. This will create a service with one container in it, which is also called a task.
If the image is not pulled from the Docker Hub, it will warn us saying other swarm nodes may not have the same image, which is fine for now.

At this point, if you open localhost:5000 to see the app, you will get MySQLdb._exceptions.OperationalError MySQLdb._exceptions.OperationalError: 
(2005, "Unknown MySQL server host 'database' (-2)") error because we don’t have a database running yet.

So, the next task is to create a database service.

Database services

We already have a mysql-server image locally so, let’s create a service by using it. 
Type docker service create --name database --env-file <.env file location> --mount type=bind,src=<location of init.sql>,
dst=/docker-entrypoint-initdb.d/init.sql mysql/mysql-server:5.7

The command is a little bit longer. Let’s understand each argument of the command.

--name: name of the service through which it can be reachable

--mount: bind local file system to the container file system

--env_file: to provide environment variables using the file

Type docker service ls to list all the services available on the swarm node

Networking #
Both services are running now, but, you will get the same error as they are not connected. 
If you remember, we used the link argument to connect the database container. 
In swarm mode, the link option is not supported and we have to connect services using a network.

Services connected to the same network can talk to each other. So, to connect our database service to app service, 
we will create an “overlay network”. In swarm mode, we deal with distributed systems, hence, we use an overlay network to establish communication 
between services.

To create an overlay network, type docker network create --driver=overlay app. This will create a new network named ‘app’ on Docker host.

Updating services

Now, we have our overlay network. Let’s attach it to both the services and let’s see if it solves the problem or not.

To update a service, type docker service update --network-add <network name> <service name/ID>.
As soon as the network is updated, you will see that your app start working normally.

We have deployed our app using services on the swarm node. Check out all the containers using docker ps. 
Docker service offers a few more commands to help you work with services. You can explore using docker service --help and docker service <COMMAND> --help.

Scaling app containers
You can deploy multiple containers on a different node. If there are multiple nodes in the cluster, the swarm manager will create container copy on every 
other node until it covers all the nodes or the defined number of containers are created.

And if there is only a single node in the cluster, all the containers are created in only that node.

We will scale our app to have three app containers and two database containers.

Let’s see this in action. If you haven’t stopped the services, then type docker service scale <service ID/Name>=Replicas_number.

Services can be scaled up and down using the same command. If you just provide the number of replicas, the swarm manager will create or stop the 
containers based on the number provided.

As every container handles the different requests, it might happen that a certain request can make a container exit the execution. 
If there are multiple hosts machines, how will you know which machine has stopped working and where the remaining containers created by the Swarm manager are?

For this, Docker has a GUI service that monitor’s all the running containers and nodes in a swarm cluster.


Monitoring Clusters Using a Visualizer

 The image we are going to use for our cluster visualization is dockersamples/docker-swarm-visualizer.

Running on Linux
We can deploy this image as an independent container or as a swarm service. To run as a container, follow the steps below.

Running as a container
Type $ docker run -it -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock dockersamples/visualizer

This will run the container with host port 8080 mapped to the container port 8080.

Running as a service #
To run a visualizer as a service on swarm node, type, 
docker service create --name=viz --publish=8080:8080/tcp --constraint=node.role==manager 
--mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock dockersamples/visualizer

Parameters:

--publish: mapping of host and container ports

--constraint: location or name of the node on which the service will be created

--mount: bind Docker socket to container socket to receive all the events from Docker host

This will create the service on the swarm manager node as mentioned in the constraint parameter.

Docker stack

Docker stack is a bundle of services. When you want to deploy a set of services to a machine, instead of creating each service separately,
Docker stack allows users to deploy the full-stack of the services at once.

`docker stack --help`

