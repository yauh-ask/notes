What is a container? #
In cloud computing, containers are a technology that enables developers to package their software, including application code, dependencies, and configurations with specific versions of frameworks, programming languages, libraries, and so on, in a module as one standard unit.

This standard unit of software can be deployed across different environments, such as a public cloud, on-prem, or a developer’s laptop, smoothly without facing any environment-specific errors.

Containers encapsulate the application from the environment it runs in and ensures a consistent runtime for the software across different platforms. This increases the developer’s productivity by notches.



Containerization provides an abstraction from the environment the application runs in.

Containers are the go-to tech in today’s modern application development landscape because of the deployment benefits they offer. All the large-scale services like YouTube, Google Search, Pokémon Go, and modern banks run on containers.

https://cloud.google.com/blog/products/gcp/bringing-pokemon-go-to-life-on-google-cloud

VM vs Containers

As you can see in the diagram, virtual machines provide an abstraction to the applications at the hardware level. They have their own CPUs, OS, memory, etc. On the contrary, containers provide an abstraction at the operating system level. This makes them more lightweight.

Since every container doesn’t have its own copy of OS, they are more lightweight, in terms of the disk memory they consume. They are more performant as there is no OS boot time involved when running the VMs’ containers.

There is a significant difference between the boot time of a container and a VM. The startup time of a VM may take seconds to minutes. The startup time of a container is in milliseconds.

Also, technically, both technologies are different and are not really comparable. Since VMs provide an abstraction at the hardware level, they are more secure than containers.

Containers are dependent on the underlying OS; this puts a limit on using other operating systems. All the containers have to share and run on the same operating system.

So, if we have a use case where we need to run multiple instances of the application on the same OS, containers are a good fit. Containers are preferred when the business needs a more agile lightweight solution with less boot time.

VMs are preferred when the business needs more security and flexibility in terms of operating systems running in each VM.

A cloud provider ideally leverages both of the technologies together to fulfill the desired deployment approach. Containers can also be deployed on VMs. This largely depends on how the provider wants to run their infrastructure. Most of the Kubernetes deployments have containers running on VMs.

Imagine running multiple instances of many microservices directly on VMs. Every VM will need a separate OS and a larger disk memory to run. This will have licensing costs, as the number of OS running in the infrastructure is high. From a cost standpoint, running containers is less expensive than running the VMs.

Containers are also intrinsically portable. If a service is running on-prem using containers, it’s easy to migrate the service to a public cloud platform or any other platform, as opposed to migrating a service to run directly on VMs on-prem.

https://netflixtechblog.com/the-evolution-of-container-usage-at-netflix-3abfc096781b

https://thenewstack.io/docker-helped-turbocharge-ubers-deployments/


SUMMARY

Why is the cluster infrastructure layer in the cloud computing infrastructure stack needed?

The cluster infrastructure layer manages the cluster of instances. It facilitates distributed node co-ordination, data synchronization, and so on.


What is true about the noisy neighbor problem?

The noisy neighbor is a multi-tenant application hosting problem.
A noisy neighbor hogs up all the resources of the machine it runs on.


Why do businesses choose shared hosting when it brings the noisy neighbor problem with it?

Shared hosting is economical in comparison to dedicated hosting due to the economies of scale.


When should we pick a native hypervisor?
When performance is a top priority when creating virtual machines.

Which is true about container technology?
Containerization provides an abstraction from the environment the application runs in.
Containers are more lightweight than VMs.
Containers are dependent on the underlying OS. They have to share and run on the same operating system.

When should we run our applications directly on VMs running on a bare metal server?
When we need more security and flexibility in terms of operating systems running in each VM
When we need to run multiple operating systems in the same machine


Deploying different services with containers #
Once we are done writing code and our microservices are ready, the next step is picking the right technology to deploy our code. In this use case, we’ll leverage the container technology to deploy our microservices.

Why deploy in containers and not directly on VMs?

We’ve already discussed the differences between the VMs and containers in the previous lesson. We know that running containers is cost-effective, lightweight, & consumes fewer resources. It’s also easier to manage and scale the system than running the services directly on VMs.

Some stats: Uber runs over 4000 microservices.

According to an InfoQ article, posted back in 2014, Google starts over two billion containers per week, three-thousand per second. You can imagine the container count at Google today.

Imagine running all that code in VMs and the resources it would require.

For container technology, we can pick Docker to run our services. To deploy one single microservice, we will first create a Docker image for it; the image will contain the application code, dependencies, configuration, libraries, and everything required to run that particular service. This step is known as containerizing the application.

Once the image is created, we will deploy that image on the machine from the command line tool. Mounting images and running them as containers is done by the container engine.

The container ecosystem also contains image registries that can be both public and private, just like the GitHub repositories. These registries contain container images as templates that can be reused with or without modifications at a later point in time.

Revisiting the why containers and not VMs discussion, containers save engineering teams a solid amount of time by letting them off the hook for making the machine ready to run a particular service built with a certain technology stack.

When built using microservices, the entire system isn’t built using one particular technology. All the different services are written using different technology stacks. Speaking of our social network application, we can write different modules using different technologies such as C++, Java, RoR, Go, Python, and so on.

If it wasn’t for container technology, the operations team would have to ascertain that the machines are ready with respect to compatibility with a particular technology before the application is deployed.

Now, when the number of microservices and their instances reaches the hundreds of thousands, this can become a huge pain.

Additionally, a microservice that runs on a certain technology cannot be deployed on the machine prepped up for any other technology without making serious modifications to the environment.

However, with containers, we don’t have to worry about all this stuff as they keep the environment isolated from the application code.

Every microservice has its own specific configuration, dependencies, deployment requirements like scalability requirement, resource monitoring requirement, and so on.

When there is a large number of microservices, containers cut down a great deal of hassle in application deployment and can assist the business decrease the time it takes to ship the software.

The primary ways of deploying and running applications on the cloud are:

Running the application directly in a virtual machine
Running the application directly on bare-metal
Running the application in a container running on either bare-metal or a virtual machine

Multiple microservices per host #
In this microservice deployment pattern, multiple microservices are deployed in a single host. The host can be a single virtual machine or a single physical bare-metal server.

One straight-forward upside of doing this is the efficient use of the host resources.

One downside of using this deployment approach is the noisy neighbor problem.

Single microservice per host #
In this deployment approach, only one microservice is deployed in a single host. There is no noisy neighbor problem in this approach. A single microservice has access to 100% of the host resources, making the approach more secure and reliable in comparison to the former approach.

As the number of containers running gets higher, the infrastructure complexity increases. We need a system that we can leverage to easily manage so many containers. This is where container orchestration tools like Kubernetes, Docker Swarm, and Apache Mesos come in.

https://www.cncf.io/case-studies/uber/
https://dzone.com/articles/why-bare-metal-is-challenging-vms-in-microservices


