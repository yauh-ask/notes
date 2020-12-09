Step functions makes it easy to coordinate the components of any distributed application that uses microservices this also uses visual workflows. A step function is an easy way to coordinate component and step through functions of your application.

Amazon MQ: is a managed message broker service. that makes it easy to set up and operate message brokers in the cloud.

Message brokers allow different software systems–often using different programming languages, and on different platforms–to communicate and exchange information. Messaging is the communications backbone that connects and integrates the components of distributed applications, such as order processing, inventory management, and order fulfillment for e-commerce.

AWS MQ manages the administration and maintenance of ActiveMQ, a popular open-source message broker.



SNS – Simple Notification Service: Provides a low-cost infrastructure for mass message delivery for mobile users.



SQS – Simple Queue Service.

This is an Amazon managed queuing service that makes it easy to decouple and scale micro-services or distributed systems or serverless applications.

Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.


SWF – Simple WorkFlow Service is used to trigger a workflow. For example, imagine that you have an expense report that needs to be approved by 3 people.

When you submit an experience report the workflow is triggered and the workflow services keeps track of each individual who needs to approve for your expenses report to be fully approved.


Availability Zones & Regions
AWS has 16 Regions & 44 Availability zones.

A Region is a geographically distinct area e.g. West coast of USA

Availability zones are Datacenters within a region. The availability zones are fault tolerant between each other. Each Availability Zone (AZ) has its own power, and are independent to other AZ within that region.

Ideally, you design your application to be across more than one AZ that way if one AZ goes down you have another.

When designing application you try to have redundancy between the three AZs. That way if AZ1 goes down due to a power failure, AZ2 will be alive and will not be affected and in turn, your applications and its underlying data are not affected.

