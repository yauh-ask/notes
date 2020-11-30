Monitoring is implemented in different components of our distributed system to ensure the efficient functioning of these components continually over a long period of time. These components are typically the database component, application server, web server, APIs, deployment pipelines, and so on. Monitoring ensures the reliability and quality of the service.

Below are a few different types of monitoring systems commonly implemented in large scale distributed applications:

Infrastructure monitoring
Database monitoring
Database transaction monitoring
Data storage monitoring
API monitoring
Application server monitoring
External application monitoring
End-to-end application monitoring
CI/CD deployment pipeline monitoring
Why monitor different components of the system? #
Monitoring our system helps us understand the long-term trends by tracking the processes and events happening over a period of time. The event data that is stored to monitor a service over a period of time is known as the time-series data.

The analysis of this data enables a business to tweak its system for performance, scalability, high availability, etc. It also assists in making better data-driven decisions.

Monitoring when applied in the database component helps us understand the rate of growth of the size of our database. This helps in provisioning the right amount of hardware without risking the service crumbling under the heavy load.

Monitoring also helps us understand how quickly the users are growing in the system and what the latency trends of different services are. It also helps engineers track metrics like CPU consumption, error rates, response times, disk usage, network bandwidth consumption, throughput, and so on.

When running distributed systems, there are a plethora of tools that help us monitor our system efficiently. Typically, all the monitoring data is streamed to a web-based dashboard in the form of graphs and charts to make it easy for a decision-maker to consume.

Continuous monitoring #
Continuous monitoring means all the monitoring that is implemented in the system runs in the auto mode without any sort of human intervention. If anything goes amiss, the system raises an alert and sends the notification to the concerned members of the team via email or on the Slack channel.

Monitoring applied in the deployment pipelines helps teams track errors that occur during the automated deployment process, such as the build fails, test failures, the build not triggering when the code is pushed to the remote repo, and so on.

Now, let’s have a look at some of the popular tools that are used in the industry to monitor the distributed systems infrastructure.

Infrastructure monitoring tools #
cAdvisor, Prometheus, and Grafana #
These three tools, cAdvisor, Prometheus, and Grafana are used in conjunction to set up a monitoring system that monitors and analyzes a service.

cAdvisor is an open-source tool for running performance analysis and collecting usage data from the containers.

cAdvisor stands for container advisor. As its name suggests, it provides resource usage, performance characteristics, and related information about the containers running in the cloud. cAdvisor runs as a daemon process in the background collecting, processing, and aggregating useful DevOps information.

The tool has native support for Docker, and it enables us to track historical resource usage with histograms and so on. This helps us understand the resource consumption and memory footprint of the code running on the servers. This information helps us discover performance bottlenecks if there are any. It also helps track which processes are too hungry for memory.

When used with Kubernetes, the cAdvisor is integrated into the Kubelet binary. It is pretty intelligent to auto-discover all the containers running in the machine and collect the CPU, memory, file system, and network usage statistics. It also provides comprehensive, overall machine usage by analyzing the root container.

After cAdvisor comes to Prometheus, it’s an open-source data monitoring tool that is largely used with cAdvisor and Grafana to set up a data analytics and monitoring system. This is kind of a de facto combination is used in the industry.

Grafana is an open-source monitoring dashboard tool that enables us to study monitoring data fetched from a certain data source. In our use case, the data source is Prometheus. Prometheus, besides being a monitoring system, is also a time series database.

Grafana dashboards help us track user behavior, application behavior, error frequency in production or other environments, types of errors popping up, and so on.

StackOverflow uses Grafana to enable their developers and site reliability teams to create tailored dashboards for visualizing data and optimizing their server’s performance.

Digital Ocean uses Grafana to build a common visual data-sharing platform that enables developers to share visualization data between their teams.

GRAFANA DEMO - https://play.grafana.org/d/000000012/grafana-play-home?orgId=1

The flow #
Our services run in containers and the container information is streamed into Prometheus from cAdvisor. cAdvisor exposes container statistics as Prometheus metrics intrinsically. Jobs are configured in Prometheus to connect with cAdvisor.

All the container data is displayed on custom Grafana dashboards. Queries fired from the dashboard hit Prometheus, which is plugged-in to Grafana as a data source.

Grafana dashboards contain a gamut of visualization options such as geo maps, heat maps, histograms, and all the varieties of charts and graphs that a business typically requires to study data.

Monitoring logs with ELK #
ELK stands for Elastic Logstash Kibana. Elasticsearch was the first and product originally released by the developers of the ELK stack. It’s a search and analytics engine. Logstash and Kibana were released later.

Logstash is a data processing pipeline that ingests data from multiple sources and then converts the ingested data into a standard format to be stored in the Elasticsearch datastore. The Elasticsearch store is a document-oriented store.

In our use case, Logstash will ingest logs in different formats from various components in our application, such as database, application server, web server, message server, and so on, and will convert all the logs in a single standard format to be stored in the Elasticsearch datastore.

Kibana is the visual dashboard that acts as a centralized log dashboard for all the logs that are ingested from the different components in the application. With the help of Kibana, developers can easily debug the issues in any component of the application by going through the log details of that component in the Kibana dashboard.



To build a more customized and complex pipeline intended to handle a large amount of data, we can also set up a message queue like RabbitMQ or Kafka before the Logstash component.

Again, there is no standard rule for setting up a data ingestion pipeline, we can always set it up according to our business requirements.

AWS and Google Cloud both provide managed ELK stack service.

Though the ELK stack is primarily used for log analysis, it’s not limited to just that. The Elasticsearch ecosystem provides a complete application observability solution that entails log monitoring, infrastructure monitoring, application performance monitoring, and so on.

What is DevOps? #
DevOps stands for Developer Operations which is Development + Operations. We are aware of the role of the developers, and operations entail everything right from the point the code is pushed to the remote repository to the point the live application is monitored in production.

Operations include things like:

Setting up, managing, and monitoring the deployment pipeline; setting up the build server and end-to-end automation for all the builds and deployments

Setting up different deployment environments such as Dev, Staging, and Production; provisioning the infrastructure and managing the IaC

Monitoring different components of the system with the right tools

Setting up and scaling application storage, diagnosing system issues, and disaster recovery

Practicing continuous delivery and deployment in the project and adhering to the organization’s processes, guidelines, etc.

The concept of DevOps originates from Agile software development methodology. Agile methodology facilitates early feedback from the stakeholders or customers on the software that is being built by organizing and managing the development process into sprints.

In a sprint, which generally spans two weeks, developers write code, build new features, and showcase it to the customer for feedback.

This approach enables teams to develop software quickly and in a more reliable way, fulfilling the expectations of the customer.

The DevOps methodology tries to achieve the same results by facilitating better collaboration between the development and the operations team.

The DevOps people are in continual contact with the dev team during the whole development and the application deployment process. This enables both teams to fix issues, like system bottlenecks, come up with the right strategy to scale the system, and more. With DevOps, the dev and the operations teams work in collaboration as opposed to working in isolation. This approach helps ship software fast.

There is another term for DevOps that floats around in the industry known as SRE (Site Reliability Engineering). The term was coined at Google, where software engineers handle the operations, ensuring the smooth functioning of all the services running at Google. The role of SRE engineers is pretty much the same as the DevOps.

There are different stages of a deployment pipeline earlier. To review, that are coding, building the code, running tests, packing the application, releasing the code, configuration management, and production monitoring.

As a DevOps engineer, we are expected to have an understanding of all these stages of the deployment pipeline. We should be aware of what technologies and tools should be leveraged to build a deployment pipeline, what build server to pick for a certain use case, what code management system would fit best with respect to the organization’s requirements, and so on.

Based on the resources that the business has, it can have a dedicated DevOps team or have the developers perform the DevOps related tasks. This generally happens if the team size is small, like in a startup.
