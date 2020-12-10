EC2 - Elastic Compute Cloud
EC2 what is it, how it works and everything else on EC2.

Elastic Compute Cloud (EC2) - Is a web service that provider re-sizable compute capacity in the cloud.

AWS EC-2 reduces the time required to obtain and boot new server instance to minutes allowing you to quickly scale capacity, both up and down, as your computing requirement charge.

In the old world if you needed an app server or db server. You would first need to table to your developer, size what you needed how many cores and then talk to your procurement team and by the time the server is in your data center it could take 2+ months.

Now with EC2, you have this with a click of a button. This also means from a startup perspective you do not have the upfront cost of buying all the hardware you need.

EC2 changes the economics of computing by allowing you to pay only computing by allowing you to pay only for the capacity that you actually use. You also have several tools at the disposal of the developers to build the applications to be resilient and isolate them from failure scenarios.

In the above architecture diagram, you manage Identity and access control via IAM and deploy some EC2 instances in your VPC. These instances are typically your app servers that then would store data in one or more EBS within one Availability Zone.

You would then send periodic EBS snapshots to your S3 buckets that get replicated at a regional level. You could use this architecture for any simple 3 tire architectural that has AZ level redundancy.

EC2 Purchase Options
On-demand – Fixed rate by the hour or by the second with no commitment

Reserved Instance - You reserve an EC2 instance for your use this gives you a discount. 1 year or 3-year teams

Spot – Enables you to bid whatever price you want to pay for an instance capacity. This is used if your application has flexible start and stop times. e.g. Big Data computation that is not time sensitive

Dedicated Hosts - Can be purchased on-demand, used for regulatory requirements that may not support multi-tenant virtualization


Elastic Load Balancers (ELB)
Get a quick overview of AWS ELBs, Cloud Watch, CloudTrails, and EC2 Placement groups, how they help in when you design your applications.

Elastic Load Balancers - Is a virtual appliance that is used to distribute traffic across your multiple application instances.

Instances are checked by the LB and they re-route the traffic if they find an application is not returning any data back.

All AWS Load Balancers have their own DNS name.

Cloud Watch

Monitoring and setting up alarms that notify the user if an AWS threshold is hit.

Events in cloud watch help you to respond to a state charge of your resources.

Cloud watch Logs – helps you aggregate monitor and store logs. This done by installing an agent on your EC2 server.

CloudTrail – Audits what is created or modified in terms of AWS infrastructure

EC-2 Placement Groups
Logical grouping of instances within a single availability zone. You can have placement groups that enable applications to participate in low latency, 10 Gbps network.

Placement groups are recommended for applications that benefit from low latency and high network throughput or both.

Take for example a Hadoop cluster or a No SQLDB where you need really high network throughput or low latency between your NoSQL DB nodes.

Lambda - Serverless Architecture
lean about Lamdba our new best friend and how you can make your architecture cheaper and easy to use.

The evolution of Lambda or the timeline looks something like this On-Prem DataCenter –> IAAS –> PaaS –> containerisation /Docker –> Serverless

Lambda is a compute services where you can upload your code and create a Lamdba function AWS Lambda takes care of provisioning and managing the servers that you use to run the code. You do not have to worry about operating systems, patching, scaling etc.

It is essentially described as an event-driven compute service where AWS Lambda runs your code in response to events. These events could be changes to the data in an Amazon S3 bucket or an Amazon Dynamo DB table.

Lambda events can trigger other Lamdba events or call other AWS services like SQS or SNS.

Why use Lambda?

The Lambda runtime is fully managed by AWS. Once a function is uploaded and configured, Lambda is responsible for managing the resources required to run the code.
Developers are free from the traditional overhead of configuring and maintaining server instances.
Lambda will immediately scale to meet spikes in demand.
Lambda is cost effective as you only pay for the computational resources used. This is, of course, true for other AWS compute services, but the cost model for Lambda is more granular than EC2 for example, with resources being charged per 100 milliseconds.
Lambdas event-driven model means you can integrate nicely with a range of AWS services, but still ensure loose coupling.
Very low cost the first 1 million request are free. 0.20 per 1 million requests there after!!

Duration the execution time of your code and memory as well but it’s almost insignificant in most cases.


Angular Client allows the user to add and delete images from S3. It also calls an API Gateway endpoint to retrieve details for all images uploaded.

Save/Delete Lambda Function will handle image upload and delete events from S3. It will be invoked by S3 when a new image is uploaded - the function will use the supplied event data to call back to S3 and retrieve the image. The image details will be saved to DynamoDB. As an image is deleted the function will use the supplied event data to identify the deleted image and remove the associated details from DynamoDB.

Retrieve Image Details Lambda Function will retrieve image details from DynamoDB and return JSON result.

Dynamo DB a single Dynamo DB table will be used to persist image details. All interactions with DynamoDB will happen via the Lambda functions.

API Gateway an API Gateway endpoint will be used as a bridge to the Retrieve Image Details Lambda function, from the web app.

That should give you a good overview of how Lambda functions work. Also, note that some cloud providers call this as “Function as a Service” FaaS.



Elastic Container Service (ECS)
AWS Elastic Container Service (ECS) is one of the most used services today. Learn what the advantages of ECS are and get a short overview of AWS Fargate.

AWS Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster.

Elastic Container Service
What is Docker : - Docker is a software platform that allows you to build, test, and deploy application quickly.

Docker is highly reliable
Docker is highly scalable
Docker package software is standardized into units called containers
Containers allow you to easily package an application code, configurations, and dependencies into easy to use building blocks that deliver environmental consistency operational efficiency, developer productivity and version control.

You can create Amazon ECS clusters within a new or existing VPC. After a cluster is up and running, you can define task definitions and services that specify which Docker container images to run across your clusters. Container images are stored in and pulled from container registries, which may exist within or outside of your AWS infrastructure.

AWS Fargate is an easy way to deploy your containers on AWS. To put it simply, Fargate is like EC2 but instead of giving you a virtual machine you get a container. It’s a compute engine that allows you to use containers as a fundamental compute primitive without having to manage the underlying instances.

