Node coordination scenario #

The nodes are aware of each other with the help of regular heartbeat signals sent to each other, primarily using IP Multicast communication.

Every heartbeat has a timeout duration; if a certain node doesn’t respond to the heartbeat signal within a stipulated time, it is assumed offline. The cluster always maintains a list of active servers.

Generally, every cluster has a node that acts as a leader taking care of the communication, and the onus of reaching a consensus among all the nodes in the cluster is on the cluster leader.


We’ll now walk through a scenario where we have the two nodes in the cluster Node A and Node B up and running, ready to receive user requests.

When the user sends a request to the backend, the load balancer routes the request to Node A. The job of the load balancer is to distribute the traffic intelligently across the nodes in the cluster. The web server that is Node A creates a user session, say US_1, and begins processing the user request.

During the request processing, assume a technical glitch brings down Node A, and the server goes offline. The cluster detects that Node A has gone offline; it then re-routes the request to Node B. Node B is a replica of Node A.

Two nodes are used in the cluster in active-active replication mode to make the service highly available. So, in case one of the two nodes goes down, the other can take over.

And that’s what exactly happens. Node A goes down due to a failure, but the service is still up, and Node B takes over, handling the traffic load of the service.

Persistent session storage #
Both nodes in the cluster persist the session information in in-memory persistent session storage. Persistent session storage is useful because if any of the nodes go down, another node can take over by accessing the session information of the offline node from the memory. It then can return the response to the end-user without them noticing anything.

Session replication #
The session state is replicated across the nodes by the cluster when a request is processed by a certain node. An important thing to remember here is that despite multiple nodes running in the cluster, it still has to act as a single system.

All the nodes should have a common state at any point in time. The end-user interacting with the service doesn’t care if the service is run by one server or a thousand servers. The cluster just has to maintain a consistent session state across all the nodes by replicating the sessions.

Session replication modes #
Session replication can happen either synchronously or asynchronously. In the synchronous replication mode, the session state is replicated across all the nodes in the cluster before the response is returned to the user.

In the asynchronous replication mode, the session replication happens in a separate thread. It’s decoupled from the response. The response is returned to the user even if the session replication fails.

Choosing between sync and async session replication mode is a trade-off. Synchronous replication has a performance cost since the response has to wait for the session to be replicated across the nodes in the cluster. This adds latency to the response, but it also ensures a consistent session state across the nodes.

On the contrary, async session replication mode has no additional latency; the response is returned immediately. However, the consistent session state across the cluster is not guaranteed.

There is one more concept involved in this, the concept of sticky sessions.

Sticky sessions #
Sticky sessions mean that the load balancer will route all the requests for a particular session to the server that processed the first request of that session.

Synchronous session replication works with or without sticky sessions, but they are important when we pick the asynchronous session replication approach. Since the consistent session state across the cluster is not guaranteed when using async session replication, another request for a certain session landing on a different node can cause inconsistency issues. This is why all the requests for a particular session are routed to the original server.

However what if the original node processing the requests for a certain session goes down when using the async replication strategy?

In this case, the load balancer has to route the request to a different node. The new node has to contain the latest session state to avert any kind of inconsistency issues. This is an important thing to keep in mind when implementing the asynchronous session replication approach.

One downside of using sticky sessions is that it can add unwanted load to a particular server. The load balancer will keep on routing requests to it even if it is already piled up with requests.

Back to the node coordination scenario #
Let’s jump back to the scenario we were discussing. Node A goes down; Node B receives the request; it reads Node A’s session info from the persistent session storage, processes the request, and returns the response.

Now, when Node A comes back online, it gets in touch with the cluster, invalidates the session* US_1* it created, and gets ready to receive the new requests.

This is how nodes communicate with each other and process requests in a cluster.

I’ve tried to present a very simple example of this so that you can get a bird’s eye view of how the nodes work in conjunction and so on. In reality, things are much more complicated, especially with cloud computing/distributed systems.



The whole point of having multiple instances in a cluster is to make the system scalable, highly available, and fault-tolerant. When a service is scalable, a large number of concurrent users can perform read-write operations on the service without experiencing any sort of latency as the traffic builds up.

Consensus #
Now, when a high number of concurrent users interact with the system hosted by thousands of nodes deployed across the globe, all the nodes get updated concurrently in real-time. That means at any point in time different nodes may have different values for a certain object. Also, among those nodes, a few might even fail.

When a user requests the value of a certain object from the system, the system is expected to give a single, consistent value of that object despite the several different values that the thousands of nodes running in the cluster hold for that particular object.

How does the system achieve this?

By reaching a consensus among all the nodes in the cluster on the value of that object.

To return a single data value to the user, the system has to make all the nodes agree on a common value. All the nodes have to reach a consensus. This mechanism of reaching a consensus in a cluster has several applications such as facilitating database transactions in distributed systems, atomic broadcasts, state machine replication, and so on.



Consensus from a database transaction standpoint #
When the application is expected to receive a large amount of traffic, it has to scale horizontally on the fly to avert any kind of latency that arises due to the heavy traffic load.

NoSQL databases became popular solely due to their ability to auto-scale dynamically; something that was not so trivial to achieve with the traditional relational databases.

Data consistency models #
When the databases run in a distributed environment, there are two data consistency models that apply to the transactions. When I say transactions here, it doesn’t necessarily mean a financial transaction. A transaction can be the persistence of any kind of event. It may be an increment in the Like-counter on a post made by a user on a social network or the writes performed by players in an online multiplayer game.

The two data consistency models involved in this are the eventual consistency and the strong consistency. Eventual consistency means that when thousands of nodes deployed across the globe hold different values of an object the system, after a short span of time, will reach a consensus and have one single value for the object across all the nodes running globally. The value of that object will eventually be consistent.

On the contrary, strong consistency means that at any point in time all the nodes deployed across the globe should have the same consistent value of an object. The strong consistency data model is key when implementing financial services.

Cloud providers generally keep the nodes that ensure consistent data in the same availability zone.

There is also a theorem called the CAP Theorem that is key when writing services that would run using a distributed system such as a NoSQL database. CAP stands for consistency, availability, and partition tolerance. As per the CAP Theorem, when the nodes in our system fail, we have two choices: we can keep our service available, and the users can continue to perform the write operations on it. Or, we can disable the writes in our system until the nodes bounce back online. The latter choice ensures a strong consistency of data in our system.

Reaching a consensus among the nodes is vital for the reliability of distributed systems and for the decentralized tech like blockchain and the cryptocurrencies built on it.

