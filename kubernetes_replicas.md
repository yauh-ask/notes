[commands](https://gist.github.com/vfarcic/f6588da3d1c8a82100a81709295d4a93)

> ReplicaSet’s primary function is to ensure that the specified number of replicas of a service are (almost) always running.

Pods are not fault tolerant. If a Pod is destroyed, Kubernetes will do nothing to remedy the problem. That is if Pods are created without Controllers.

The first Controller we’ll explore is called ReplicaSet. 
Its primary, and pretty much only function, is to ensure that a specified number of replicas of a Pod matches the actual state (almost) all the time. 
That means that ReplicaSets make Pods scalable.

We can think of ReplicaSets as a self-healing mechanism. 
As long as elementary conditions are met (e.g., enough memory and CPU), Pods associated with a ReplicaSet are guaranteed to run. 
They provide fault-tolerance and high availability.

