What is an instance in the cloud? #
A server running our application in the cloud is called an instance. We can think of one server as one instance. The terms server and instance can be used interchangeably but in the cloud computing universe, the term instance is preferred over the server. Instance, server, node, server node, they all mean the same thing.

Simplifying it even further, imagine a simple _ Create Read Update Delete (CRUD)_ – based app hosted by an Apache Tomcat server on our local machine, that is our laptop. Now, when we deploy the app to the cloud, in the cloud computing jargon that app becomes the workload and the Tomcat server node becomes an instance.

Instances are automatically spun up and down all the time by the cloud platform based on the compute requirements of the workload. This is known as auto-scaling.

Instance groups #
A workload can be hosted by one single instance or a cluster of instances. They can also be spread out geographically in different availability zones across the globe. Using a cluster of instances enables us to make our system fault-tolerant and achieve high availability.

Instance groups enable us to enforce common policies, rules, and configuration across multiple instances. These policies can be configured on high availability, auto-healing, load balancing, applying updates, and so on. Overall these instance groups make the instance management easier.

Instances have no dependency on the workload and vice versa. Both are loosely coupled. This allows them to spin up and down according to demand. Also, having no dependency makes the workload portable. It can be moved around from on-prem to cloud and across different cloud platforms without much hassle.

Generally, instances in the cloud are virtual machines that run the images of operating systems like Linux and Windows. We can also create custom images based on our requirements or import existing images and run them on our cloud instances.

Instances can also run containers with container optimized operating systems. Using instance templates, we can clone new instances with the existing configuration eventually saving a lot of time.

When deploying our workload on the cloud, we can choose the hardware properties of our instances, such as the number of virtual CPUs, memory, storage capacity, and so on. Instances are categorized into several different types by the cloud providers where each category of instances serves certain specific use cases.

Types of instances #
Standard instances #
These instances are configured for general use cases, including running web apps, microservices, etc. They have a balance between the resources allocated to them such as CPU, memory, and so on. Standard instances fit best for hosting general compute workloads.

High-CPU instances #
These instances are specifically built to provide the high computing power required to run compute-intensive workloads such as distributed analytics, batch processing, machine learning algorithms, scalable multi-player gaming, graphics rendering, etc.

High-memory instances #
These instances are built for running memory-intensive workloads such as real-time data ingestion, big data analytics, high-performance databases, running distributed in-memory caches & so on.

Instances with GPU #
These instances provide the power of GPU for advanced computing requirements such as running data-intensive machine learning algorithms, data processing, 3D rendering, animation, virtual reality applications, autonomous vehicles, fluid dynamics, blockchain computations, and so on.

Pre-emptible instances #
Pre-emptible instances are instances that are offered at a lower rate than the rate of regular instances by the cloud provider.

Lower rate? Why?

Their availability is not guaranteed at all times, and cloud providers offer these instances based on their availability. They can be terminated at any time from our workload and can be allocated to other high priority tasks.

Wait, what?

The provider can pull out instances running my service at any time? Why on earth would I ever opt for such kinds of instances?

Well, often we have use cases that are not really mission-critical and high priority like image processing, analytics, file processing, etc. These processes are batch processes, and they run in the background like a daemon.

Pre-emptible instances can be used for running these tasks, even if the instances are terminated and pulled away. The slowing down of these tasks does not impact the service much as a whole, and the business can save money in the process.

Instances and storage #
Ephemeral storage #
Instances also have memory attached to them, known as the ephemeral storage, which can be augmented based on the requirement. This helps retain the running state in case the instance goes down due to failure or reboots. This memory is local to the compute instance and is purged after the instance is terminated.

Ephemeral storage is ideal for storing temporary data, including such as the local cache, buffers, OS, runtime data, and so on.

Persistent storage #
There is another type of storage known as persistent storage. The scope of this memory is beyond individual compute instances. Newly spun up instances in the cluster can easily access the running state of the cluster from the persistent storage and continue the task without having the end-user notice the instance swap.

Instance life cycle #
Right from the point an instance is provisioned, it goes through various stages in its life cycle such as being provisioned, staged, in the running state, terminated, and spun up again.

Provisioned #
In this stage, the instances are not running yet. They are allocated to run a workload based on the configuration.

Staged #
Cloud resources get allocated to an instance in this stage. The instance gets prepped up for the launch.

Running #
The instance starts hosting the workload. If multiple instances are already running in the cluster, the new instance shares the load with the other already running instances.

Terminated #
The instance is down either due to failure or manually done by the user. It can be reset, restarted, or deleted at this stage.

What is auto-scaling? #
Auto-scaling is the cloud platform’s ability to react to the variation in the live traffic load on the workload by spinning instances up and down on the fly.

The ability to auto-scale enables the cloud to augment or reduce the computing power of the instance cluster based on the demand, ensuring smooth handling of the traffic surge and slump. Therefore, when additional instances are added on the fly, they share the load of the already running instances, diminishing the risk of them crumbling under the heavy traffic load.

When the traffic subsides and the workload needs comparatively less computing power, the cloud auto-scaler obliges by freeing instances by shutting them down.

Benefits of auto-scaling #
Autoscaling has several benefits. The most important of them is high availability.

If a few instances in the cluster go down due to some kind of failure, new instances are automatically spun up to share the load on the cluster. Due to this behavior, the service stays available. This is also known as fault tolerance. I’ll discuss fault tolerance and high availability in detail later in the course.

Autoscaling provides the ability to the platform to handle node failures smoothly without any human intervention. Another upside of auto-scaling its cost-effectiveness.

When the traffic subsides, additional instances, that were added earlier, are terminated and removed from the fleet. Therefore, the businesses only have to pay for the compute that the service utilizes.

Auto-scaling is also known as auto-provisioning. The cloud auto-scaler logic runs on a predefined set of rules and policies. But why do we need to set rules and policies upfront when deploying our workload on the cloud?

Auto-scaling configurations #
Scheduled auto-scaling #
The cloud auto-scaler mechanism runs on predefined rules and policies simply due to the reason that businesses, especially startups, have limited resources. They can’t just keep adding up server instances on the fly. Computing power costs serious money. We do have to set the rules and configurations as per our budget.

Scheduled auto-scaling is proactive scheduling where we set up all the configuration upfront like the maximum number of instances that can be summoned in the fleet for the support, maximum CPU utilization, and so on.

The scheduled auto-scaling policy holds all the data that commands the auto-scaler on how to react when the workload is hit with a traffic surge. There are various ways to make auto-scaling as effective as possible for services running on the cloud, including predictive and dynamic auto-scaling.

Predictive auto-scaling #
Predictive autoscaling makes use of machine learning to study recent and historical traffic patterns for respective workloads. Based on the study, the right number of instances are provisioned to serve the anticipated traffic.

Dynamic auto-scaling #
Dynamic autoscaling is the method where instances are spun up on the fly based on several different metrics such as CPU utilization of the instances, load balancer utilization, and monitoring metrics.

CPU utilization #
In the autoscale policy, the threshold for the CPU utilization of the cluster is set, for instance, to 75%, beyond which new instances start spinning up to share the load on the workload.

Load balancer utilization #
Another trigger to spin up instances is the requests handled per second by the load balancer. Depending on the value set, an instance can be spun up or terminated.

Monitoring metrics #
Besides the above two metrics, monitoring metrics like the container stats, are also considered when setting up the autoscale policy.

To set an effective auto-scale policy all the above ways are ideally used in conjunction to achieve the best results.

