Cloud providers deploy our service across the globe in different regions and availability zones to keep the service available, having a contingency plan for disasters and placing the code near the end-user to cut down network latency.

A region is a geographic area. For instance, Las Vegas, Delhi, Melbourne, and Toronto are different regions. A region contains multiple availability zones also called AZs. Further, these AZs contain multiple data centers. Regions may also contain multiple local zones or LZs.

Taking AWS Global Infrastructure as a reference; its Ohio region contains three availability zones, the Tokyo region contains four availability zones. Meanwhile, the Oregon region contains four availability zones and one local zone, and so on.

Local zones are an extension of a region in case additional computational power or other infrastructural resources are required in a region. LZs can be set up near the end-user to augment the regions’ power and to cut down the latency. A local zone set up near the end-user helps deploy latency-sensitive services like stock trading, online multiplayer games, and so on.

If we have deployed our service in a region and want to cut network latency down, we can take advantage of local zones. Though not all the regions have the ability to set up local zones. The availability of an LZ in a region largely depends on the cloud provider

Communication between regions, availability zones, and data centers #
Regions are kept physically isolated and independent of each other in terms of power supply, water supply, hardware etc. This ensures service availability and fault-tolerance from a regional perspective. If any single region goes down, it doesn’t impact the other regions.

Also, there are often legal constraints on companies dealing with sensitive data to keep it within a certain region. Having isolated deployments in different regions enables them to comply with the law. The government and other legal entities do not want their data to be replicated to other regions across the globe for obvious security reasons.

The availability zones contain multiple data centers. Every individual availability zone is run by its own set of data centers. Data centers are not shared between the availability zones to ensure service availability and fault-tolerance at the zonal level. If an AZ goes down due to a local disaster, the other availability zones are not impacted due to this. An availability zone is generally run by two to three data centers. A large availability can also be run by five to six data centers.

Within an availability zone, the data centers are connected to each other via a low latency network. Even the network is made redundant to cope with any sort of failure. When we deploy our application on the cloud, we are prompted by the cloud provider to select a region and an availability zone to run our application in.

Ideally, the region and the AZ nearest to our end users is selected to keep the network latency low.

The cloud deploys our application spanning multiple availability zones to avoid a single point of failure from an AZ standpoint. Even if an entire zone goes offline, the requests will be routed to a different zone. This is achieved with the help of a load balancer that runs at a regional level outside the zones. These load balancers have a regional scope.

This is the standard setup of regions, availability zones, and data centers. Businesses can always tweak their deployments based on their requirements with the help of cloud providers.

Efforts involved in going multi-regional #
When running a service on the cloud, the efforts required to go multi-regional largely depend on:

The cloud service deployment model being used. For instance, if the service is completely deployed using the serverless approach, the efforts required for the multi-regional deployment would be minimal.

The expectations of the business from their global deployment, for instance, the latency expectations and the architectural complexity of their service. It’s generally a trade-off between the latency and the increase in complexity of the architecture due to the efforts put in to achieve a certain latency number across the regions.

Multi-regional deployments require:

- architectural changes
- configuration changes
- the pricing policy of the cloud providers to vary based on the geographic locations
- the service to stay in compliance with the local data laws
- configuring the primary and the secondary regions
- the data replication policies between the regions have to be written
- implementing geo-aware routing and multi-regional cluster monitoring
- making sure the infrastructure we want is available in the regions we want to deploy our service and so on.

Single region to multi-regional deployment of an online multiplayer game #

Taking that online multiplayer game example further, it was originally deployed in a single region. Now, we want to expand the deployment to multiple regions across the world.

To have a multi-regional deployment we are required to comply with the local data laws. Therefore, a couple of big changes that we have to make in our system are:

- We need to update our data persistence and log management flow.

- We need to rebuild our deployment pipeline.


Data persistence and log management #
Originally, all the logs were being stored in a single region, but now we have to split the logs and store them region-wise to keep the data within that specific region. This means updating the log management module. Also, regarding storing the data of users, we have to tweak the flow that takes care of on-boarding new users, as we now have to keep their information, like the payment information for in-game purchases, in the region closest to them. We may also have to move all the existing data we have to the regions closest to the users.

Why are we doing this?

To reduce the latency and to comply with the data laws.

Since the data of the user stays in the region closest to others, the network latency to fetch that data would be minimal.

In compliance with the data law of some regions, we may also have to remove some fields in the user registration form. To deal with this, we may have to create separate onboarding pages for different regions and then route the users to region-specific pages something along the lines of how e-commerce websites route us to the local region-specific versions of their websites.

Cloud vs. traditional computing infrastructure #
Traditional computing infrastructure #
In the traditional computing model, we generally have big monolithic applications hosted by bare metal servers. We would put up a load balancer, arrange some bare metal servers in the replication and redundant mode, and happily run our service.

Over time, as the world came online, the traffic on the websites started piling up, and the complexity of applications increased, we split big monoliths into service-oriented architecture and microservices. We needed a more robust infrastructure to host our services, and this led to the adoption of cloud computing.

Cloud computing infrastructure #
As opposed to behaving like one big single service, the cloud has several individual services, accessible via APIs, running in parallel and working in conjunction with each other. These services are spread across the globe horizontally. This enables them to stay loosely coupled and scale on the fly.
ferent cloud services, be it the database service, load balancing service, or the compute service, all are spread horizontally across different availability zones and regions across the globe. This design facilitates availability, fault-tolerance, cost-effectiveness, and scalability.



https://cloud.google.com/about/locations/#europe





