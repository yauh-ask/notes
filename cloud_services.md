There are typically four popular cloud service models in the industry that are offered by most of the cloud providers. These are:

IaaS – Infrastructure as a Service
PaaS – Platform as a Service
SaaS – Software as a Service
FaaS – Function as a Service

Infrastructure as a Service (IaaS) #
Infrastructure as a Service (IaaS) is a cloud service model that offers the highest level of control over the compute infrastructure of all the cloud service models. It enables us to pick the data centers’ servers, storage, networking, and location - housing the infrastructure, and so on. We don’t have to set up anything ourselves, all the hardware that we pick is managed by the cloud provider.

We can scale up and down according to demand and can pay as we go. Using an IaaS, means getting access to the entire data center infrastructure over the web. In an IaaS service model, a business typically manages the OS running on the server, the middleware, runtimes, and so on. The physical end of the infrastructure is managed by the provider.

An IaaS service model is ideal for businesses that need control over the software that runs on their hardware. They don’t have to set up anything on-premise, and they don’t have to pay anything for the hardware upfront. They just have to access all the infrastructure over the web and setup and manage their software on it.

Typically, all the big cloud providers like AWS, GCP, Azure, and DigitalOcean offer the IaaS service model.

In a Platform as a Service model, we build and run our applications leveraging the platform provided by the cloud provider. The platform is a full suite of services required to develop and host an application. We get a cloud-based environment to build, test, and run our service. All we have to do is use the platform’s APIs, write our code, and deploy our service.

In PaaS, we have no control over the infrastructure. We run our applications using the technology stack offered by the provider. The technology stack can contain both open source and proprietary products, which are managed by the provider.

Though a PaaS offering has a wide range of services, it supports multiple programming languages, frameworks, and so on. Still, we don’t have much choice or flexibility picking our technology stack and integrating third-party tools of our choice. When writing our app using a PaaS, there is also an element of vendor lock-in. It’s a trade-off between saving time and convenience and having control over the infrastructure.

The full suite of services of a PaaS cuts down the app development time by notches. We don’t have to worry about OS upgrades, installing security patches, and so on. I would say application development using a PaaS is pretty convenient. Google App Engine is one example of a PaaS.

Software as a Service (SaaS) #
Think of using a SaaS model as accessing a full-fledged web service run by a third-party provider. The service can be a search service, a web-based workplace communication tool, or any service that runs on the web.

Let’s understand SaaS with the help of an example. Say you need to add a product search module on your e-commerce platform to enable users to easily search the products. There are two ways to pull this off. Write the search service all by yourself and manage it continually or leverage a ready-made, customizable third-party search service via a SaaS service model and integrate it with your application.

Using a third-party search service would make sense if you are looking for a quick, easy-to-use, and fully managed search solution for your platform. SaaS is also known as on-demand software and is made available via third-party providers on a subscription basis or license. These SaaS services are plug and play in nature and can be integrated with our product using their APIs or the Web-hooks. The integration largely depends upon the nature of the service.

The provider of a SaaS manages everything. The users of the service don’t have to worry about the technology stack the service is built on, how the service is deployed, the scaling strategies, software upgrades, and so on.

The trade-offs involved when using these services are:

The business has to share its data with the service provider. Not ideal for a business looking to keep everything on their premise.

There is a limit to the customization flexibility and the features a business has access to.

If the service goes down or has high latency, the business can’t do much from an engineering point of view.

Functions as a Service #
FaaS is a cloud service model that enables developers to run their code as functions in the cloud. When using FaaS, a developer simply has to upload the business logic in functions to the cloud and the cloud platform takes care of the rest of the stuff such as running the code, managing the servers, scaling, provisioning of resources, monitoring, integration with other services and so on.

The idea behind using FaaS is to have the privilege to focus solely on the business logic and let the cloud take care of the rest. This eventually speeds up the development process. Besides allowing you to completely focus on creating value, there is also a cost-related reason associated with the FaaS service model.

When using FaaS, a business doesn’t have to provision the servers; there is no need to run the servers continually. FaaS is an event-driven service model. The functions are only triggered when an event occurs. That event can be an HTTP web request, a backend job, a message being delivered from a queue, a user clicking on an element on a web page, and so on.

Therefore, the service gets triggered and the platform spins up a server only when an event occurs. As a result of this event-driven flow, the business only pays for the compute the service consumes during the time that particular event occurred, as opposed to paying for an instance that runs the entire day.

The platform tracks this compute time very minutely, even upto milliseconds, so that businesses don’t have to pay anything extra.

Some examples of FaaS are AWS Lambda, Google Cloud Functions, and Azure Functions. 

Functions as a Service architecture #
FaaS - A step further from microservices #
Originally, we had application monoliths. Then, we split those monoliths into microservices that helped us scale and make our architecture loosely coupled. It gave us the confidence that making a change to one module of the system won’t negatively impact or even bring down the entire service for that matter. The split enables us to manage the system more efficiently.

FaaS is a step further from microservices. It’s a more granular approach. With this service model, a microservice is split into functions, giving away deployment control to the cloud platform. When using FaaS, we do not have to manage the containers, as we did earlier, to deploy our microservices or worry about implementing monitoring and so on.

EXAMPLE

Architecture of a simple application using FaaS #
Here is a very basic architecture of an online service using FaaS to give you a better understanding of the service model.

Imagine a simple social media marketing service that enables publishers and advertisers to work together by connecting them online.

To achieve this, it encourages both the parties, i.e., the advertisers and the publishers, to enter their business information via its web service. Once the user enters the information on the website and clicks submit, it is processed on the backend and stored in the database.

If we were building a regular application using a PaaS, for example, we would have two separate APIs – one for the advertiser and other for the publisher. Then, we would implement both our APIs on the backend. When building our service using FaaS, we have to focus on writing the business logic in functions. That’s about it.

We will create two separate functions - one for the advertiser and the other for the publisher, containing the business logic. We are aware of the fact that we do not have access to the server on which our code will run; we just have to write the business logic and upload it to the platform, letting it take care of the rest.

Our architecture will have an API Gateway to entertain the requests from the front end. An API Gateway is a managed service that takes care of all the API related tasks such as managing, publishing, monitoring the APIs, dealing with traffic bursts, and taking care of authorization, authentication, and so on. AWS API Gateway and Google Cloud Endpoints are examples of fully managed API Gateways.

The API Gateway will receive the requests from the front-end and will route the request to the respective function based on the handler configuration provided in the Gateway. In this scenario, the passing of a request to the appropriate function is an event. When the event occurs, the platform spins up the server, runs the function, and returns the response to the API Gateway to be returned to the client.

Now, this is a very simple use case with just two functions. Depending on the application size, as the number of functions increase, the complexity of managing them increases too. To manage this effectively, we have frameworks like Serverless.

The Serverless Framework is an open-source, end-to-end solution for building and operating Serverless applications.

So, you just saw how with FaaS the complete application development work is reduced to just coding functions. If you’ve ever worked on the first version of Spring Framework, you would know that the application required so much XML configuration and multiple project files just to run a hello world web page. Just a slight typo in configuration made us pull our hair, trying to figure out what really went wrong.

FaaS doesn’t doesn’t expect you to manage anything of that sort, making this service model amazing, right? Having the ability to focus on writing business logic and not worry about anything else. Having to pay based on the compute time only and not for the idle running server instances.

Things to be aware of when choosing FaaS service model #
Cold start problem #
Since FaaS is an event-driven model, the server only spins up when an event occurs; it’s not always running. There is a boot time associated, every time the server spins up, and this eventually adds a bit of latency to the response. This behavior is known as the cold start problem.

The server’s boot time varies depending on several factors such as the service provider, environment configuration, memory footprint of the code, the technology the service is built with, and so on.

So, if you are trying to build a low latency application like a stock trading app using FaaS, you should be aware of the cold start problem.

If the service running on FaaS keeps receiving requests continually, the cold start won’t be an issue because the server that spun up for the first request will keep processing the queued requests. However, think of an application that receives intermittent traffic. In this scenario, every time the event occurs the platform has to spin up a new server instance. Every user will feel that additional latency when interacting with the service.

Giving up control #
The second trade-off when using FaaS is that you have to give up a lot of control. Although all kinds of applications can be deployed using a FaaS service model, it doesn’t fit best with every use case. It’s not a one size fits all service model. It has its pros and cons and should be picked wisely. I’ll discuss more on this in the FaaS use case section.

Also, though the developer is not expected to manage the servers, they still have to have the knowledge of how their code runs in the system, how it interacts with the other services, and so on. They have to have an idea of the overall system architecture. Imagine having scalable functions with a bottleneck in the data persistence flow. Auto-scaling functions wouldn’t be any good in this scenario.

Not having to manage anything might sound pretty cool from 35K feet, but when you hit the ground, you start seeing the little details of everything. Then to tweak stuff, you would need control.

Complexity of managing so many functions #
When you have so many functions running on the cloud, this adds up to the complexity of the service. Monoliths are simple to manage but difficult to scale. Stateless functions are easy to scale but too many of them add up to the complexity of the project. Individual functions may be simple to scale, but the project as a whole becomes complex.

Also, since FaaS is a relatively new service model the tools available for scaling are limited. The developers have to rely on the tools provided by the platform to manage and monitor their code.

Alright, with this being said, let’s move on to the use cases of Functions as a Service.

FaaS – Use cases #
FaaS is perfect for services that are triggered only for a certain duration, say for a few hours in a day or a few days in a week or a month. Examples of these services would be modules that execute tasks initiated by a background batch job, including a medical bill processing module, an automated tax processing module, chatbots, etc. Since these services only run for a certain duration, it’s best to spin up the servers only when required as opposed to keeping them running continually. FaaS enables us to do just that.

Stateless processes, like image compression, video analysis, data processing, and high volume big data analytics, can be isolated from the system and can be built using FaaS.

If your application has an event-driven architecture FaaS can be a good fit for your application. Then again, if low latency is important for you, you have to consider other options. A lot of thought should go into the process of designing your application, picking the right cloud service model, and the technology stack.

