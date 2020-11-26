Network Fundamentals

The network is nothing but an area that allows somebody to reach others with defined permissions and protocols.

Network terminologies and commands

There are some terminologies used in Networking. Some of them are:

- Hostname: This is the most-frequently-used word. It’s the name of the machine to identify it in a network.

- ping: ping <hostname>/<ip> command is used to check the connectivity of machine from the machine from which the command is run.

- subnet: This is a small isolated part of a network. It is like creating boundaries to a particular part in the same network.

- DNS: This is like a phone directory. All the reachable hosts are mapped in this domain name service/system using IP and hostname so that you can
either reach them by name or IP.

- /etc/hosts: This is the important file. This file has all the reachable hosts with their IP addresses.




Docker Communication

By default, all containers run in the default network space of Docker. Hence, every container can communicate with others.
We can create network isolation if it is needed.

When you initially install Docker, the platform automatically configures three different networks that are named none, host, and bridge.

The none and host networks cannot be removed, they’re part of the network stack in Docker, but not useful to network administrators since they have 
no external interfaces to configure. Admins can configure the bridge network, also known as the Docker0 network.
This network automatically creates an IP subnet and gateway.

All containers that belong to this network are part of the same subnet, so communication between containers in this network can occur via IP addressing.

A drawback of the default bridge network is that automatic service discovery of containers using DNS is not supported. 
Therefore, if you want containers that belong to the default network to be able to talk to each other, you must use the --link option 
to statically allow communications to occur. Additionally, communication requires port forwarding between containers.

To see the networks run the command `docker network ls`.
