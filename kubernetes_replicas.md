[commands](https://gist.github.com/vfarcic/f6588da3d1c8a82100a81709295d4a93)

> ReplicaSet’s primary function is to ensure that the specified number of replicas of a service are (almost) always running.

Pods are not fault tolerant. If a Pod is destroyed, Kubernetes will do nothing to remedy the problem. That is if Pods are created without Controllers.

The first Controller we’ll explore is called ReplicaSet. 
Its primary, and pretty much only function, is to ensure that a specified number of replicas of a Pod matches the actual state (almost) all the time. 
That means that ReplicaSets make Pods scalable.

We can think of ReplicaSets as a self-healing mechanism. 
As long as elementary conditions are met (e.g., enough memory and CPU), Pods associated with a ReplicaSet are guaranteed to run. 
They provide fault-tolerance and high availability.

### Sequential Breakdown of the Process 
The sequence of events that transpired with the kubectl create -f rs/go-demo-2.yml command is as follows.

Kubernetes client (kubectl) sent a request to the API server requesting the creation of a ReplicaSet defined in the rs/go-demo-2.yml file.

The controller is watching the API server for new events, and it detected that there is a new ReplicaSet object.

The controller creates two new pod definitions because we have configured replica value as 2 in rs/go-demo-2.yml file.

Since the scheduler is watching the API server for new events, it detected that there are two unassigned Pods.

The scheduler decided which node to assign the Pod and sent that information to the API server.

Kubelet is also watching the API server. It detected that the two Pods were assigned to the node it is running on.

Kubelet sent requests to Docker requesting the creation of the containers that form the Pod. In our case, the Pod defines two containers based on the mongo and api image. So in total four containers are created.

Finally, Kubelet sent a request to the API server notifying it that the Pods were created successfully.
