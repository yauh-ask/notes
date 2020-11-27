A cluster is a group of servers put together to make the system highly available, fault-tolerant, and scalable. Multiple servers running in conjunction also facilitate parallel processing of tasks.

Every large-scale internet service runs on single or multiple clusters to ensure minimum downtime.

What is high availability? #
High availability, also known as HA, is the system’s ability to stay online despite having failures at the infrastructural level in real-time.

High availability ensures the uptime of the service is much more than the normal time. It improves the reliability of the system and ensures minimum downtime.

The sole mission of highly available systems is to stay online and stay connected. A very basic example of this is having back-up generators to ensure continuous power supply in case of any power outages.

In the industry, HA is often expressed as a percentage. For instance, when the system is 99.99999% highly available, it simply means 99.99999% of the total hosting time the service will be up. You might often see this in the _ Service Level Agreements (SLA)_ of cloud platforms.

What is fault tolerance? #
Fault tolerance is the ability of the system to stay up despite taking hits. A fault-tolerant system is equipped to handle faults. Being fault-tolerant is an essential element in designing life-critical systems.

A few instances, out of several, running the service go offline and bounce back all the time. In case of these internal failures, the system could work at a reduced level, but it will not go down entirely.

A very basic example of a system being fault-tolerant is a social networking application. In the case of backend node failures, a few services of the app such as image upload, post likes, etc. may stop working. However, the application as a whole will still be up. This approach is also known as fail soft.

At the application level, to achieve high availability and fault-tolerance, a big monolith service is architecturally broken down into smaller, loosely coupled services called microservices.

The upsides of splitting a big monolith into several microservices are:

Easier management
Easier development
Ease of adding new features
Ease of maintenance
High availability and fault tolerance
Every microservice takes the onus of running different features of an application such as image upload, comment, instant messaging, user tagging, and so on. So, even if a few services go down, the application as a whole is still up.

Redundancy – Active-passive HA mode #
Redundancy is duplicating the components or instances and keeping them on standby to take over in case the active instances go down. It’s the fail-safe, backup mechanism.

Getting rid of single points of failure #
Distributed systems became so popular because we can use them to get rid of only the points of failure present in a monolithic architecture.

A large number of distributed nodes work in conjunction with each other to achieve a single synchronous application state. When so many redundant nodes are deployed, there are no single points of failure in the system. In case a node goes down, redundant nodes take its place, and the system as a whole remains unaffected.

Single points of failure at the application level mean bottlenecks. We should detect bottlenecks in performance testing and get rid of them as soon as we can.

Monitoring and automation #
Systems should be well monitored in real-time to detect any bottlenecks or single points of failure. Automation enables instances to self-recover without any human intervention. It gives instances of the power to self-heal.

Furthermore, the systems become intelligent enough to add or remove instances on the fly as per the requirements. Since the most common cause of failures is human error, automation cuts down failures significantly.

Replication – Active-active HA mode #
Replication means having a number of similar nodes running the workload together. There are no standby or passive instances. When a single or a few nodes go down, the remaining nodes bear the load of the service. Think of this as load balancing.

This approach is also known as the active-active high availability mode. In this approach, all the components of the system are active at any point in time.

Geographical distribution of workload #
As a contingency for natural disasters, regional data-center power outages, and other big-scale failures, workloads are spread across different data centers across the world in different geographical zones.

This avoids the single point of failure with respect to a data center. Also, latency is reduced by quite an extent due to the proximity of data to the user.

All the highly-available, fault-tolerant design decisions are subjective to how critical the system is? What are the odds that the components will fail?.

Businesses often use multi-cloud platforms to deploy their workloads, ensuring further availability. If things go south with one cloud provider, they have another to fall back over.
