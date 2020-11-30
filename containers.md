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
