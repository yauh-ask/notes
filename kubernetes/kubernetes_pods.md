> A Pod is a way to represent a running process in a cluster.
> If you have used Docker or Docker Swarm, you’re probably used to thinking that a container is the smallest unit and that more complex patterns are built on top of it. 
With Kubernetes, the smallest unit is a Pod.

Even though a Pod can contain any number of containers, the most common use case is to use the single-container-in-a-Pod model. 
In such a case, a Pod is a wrapper around one container. From Kubernetes’ perspective, a Pod is the smallest unit.

We cannot tell Kubernetes to run a container. Instead, we ask it to create a Pod that wraps around a container.

Arguments for writing .yml file for pod are [here](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#pod-v1-core).

[Commands](https://gist.github.com/vfarcic/d860631d0dd3158c32740e9260c7add0) to play with pod.





### Components Involved in a Pod’s Scheduling #

1. API Server #
The API server is the central component of a Kubernetes cluster and it runs on the master node. Since we are using Minikube, both master and worker nodes are baked into the same virtual machine. However, a more serious Kubernetes cluster should have the two separated on different hosts.

All other components interact with API server and keep watch for changes. Most of the coordination in Kubernetes consists of a component writing to the API Server resource that another component is watching. The second component will then react to changes almost immediately.

2. Scheduler #
The scheduler is also running on the master node. Its job is to watch for unassigned pods and assign them to a node which has available resources (CPU and memory) matching Pod requirements. Since we are running a single-node cluster, specifying resources would not provide much insight into their usage so we’ll leave them for later.

3. Kubelet #
Kubelet runs on each node. Its primary function is to make sure that assigned pods are running on the node. It watches for any new Pod assignments for the node. If a Pod is assigned to the node Kubelet is running on, it will pull the Pod definition and use it to create containers through Docker or any other supported container engine.

#### Sequential Breakdown of Events #
The sequence of events that transpired with the kubectl create -f pod/db.yml command is as follows:

Kubernetes client (kubectl) sent a request to the API server requesting creation of a Pod defined in the pod/db.yml file.

Since the scheduler is watching the API server for new events, it detected that there is an unassigned Pod.

The scheduler decided which node to assign the Pod to and sent that information to the API server.

Kubelet is also watching the API server. It detected that the Pod was assigned to the node it is running on.

Kubelet sent a request to Docker requesting the creation of the containers that form the Pod. In our case, the Pod defines a single container based on the mongo image.

Finally, Kubelet sent a request to the API server notifying it that the Pod was created successfully.

The process might not make much sense right now since we are running a single-node cluster. If we had more VMs, scheduling might have happened somewhere else, and the complexity of the process would be easier to grasp. We’ll get there in due time.


### Anatomy of a Pod

Pods are designed to run multiple cooperative processes that should act as a cohesive unit. Those processes are wrapped in containers.

All the containers that form a Pod are running on the same machine. A Pod cannot be split across multiple nodes.

All the processes (containers) inside a Pod share the same set of resources, and they can communicate with each other through localhost. One of those shared resources is storage.

A volume (think of it as a directory with shareable data) defined in a Pod can be accessed by all the containers thus allowing them all to share the same data.


>> A Pod is a collection of containers. However, that does not mean that multi-container Pods are common. They are rare. Most Pods you’ll create will be single container units.

Monitoring health is possible via __liveness and readiness probes__.

#### Pods Are (Almost) Useless (By Themselves)
Pods are fundamental building blocks in Kubernetes. In most cases, you will not create Pods directly. Instead, you’ll use higher level constructs like Controllers.

Pods are disposable. They are not long lasting services. Even though Kubernetes is doing its best to ensure that the containers in a Pod are (almost) always up-and-running, the same cannot be said for Pods. If a Pod fails, gets destroyed, or gets evicted from a Node, it will not be rescheduled. At least, not without a Controller. Similarly, if a whole node is destroyed, all the Pods on it will cease to exist. Pods do not heal by themselves. Excluding some special cases, Pods are not meant to be created directly.
