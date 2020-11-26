Public cloud #
Public cloud as the name implies is “open to all,” I mean the product offerings of the cloud are available to indie developers, startups, mid-sized businesses, enterprise businesses, or anyone looking for a cloud platform to deploy their service.

A few examples of public cloud are AWS, GCP, IBM Cloud, and Microsoft Azure. We’ve discussed before that public clouds generally offer a freemium plan and are very economical. Therefore, an indie developer developing an online multiplayer game will prefer a public cloud, like AWS, to deploy their service as opposed to picking another form of cloud deployment model.


Private cloud #
Private cloud, as the name implies, is private in nature. It runs the infrastructure only for a single business. A private cloud is way more expensive than a public cloud because there are no economies of scale involved. The cost of running the entire infrastructure has to be taken care of just by a single organization.

A business can choose to run a private cloud on its premises, commonly known as on-prem, or it can lease a data center of a third-party cloud provider to run its services. Generally, when running a private cloud, businesses prefer to run their infrastructure on-prem.

What is on-prem? #
On-prem means the service of the business runs from within the confines of the organization. The business has complete control over the infrastructural setup. Data stays in its own private network. Nobody other than the authorized individuals has access to the information.

The need for on-prem #
Security and control #
The primary reason for on-prem deployment is security. When companies use a third-party cloud service, the data of the organization gets shared with the vendor of the service. This opens up potential data breach possibilities. Data is critical to the existence of businesses, especially if they are in the finance, military, or health care domain.

Customization #
Besides security another reason to get your own data center is the ability to customize your own setup. There are instances when businesses need unique solutions catering to their needs that a third-party cloud vendor does not offer.

Vendor lock-in #
Another reason to set up your own infrastructure is to avoid vendor lock-in. Many third-party cloud providers offer their own high-performance proprietary solutions that can power our service. Now, to integrate our code with a proprietary solution, we would need to write a lot of custom code with respect to that proprietary product.

Google Cloud Datastore is one unique proprietary offering of GCP. If we use Google Cloud Datastore as our database, we have to write persistence code specifically for that product, and our data model has to be designed with regards to how Google Cloud Datastore works.

In the future, if we want to migrate to an open-source solution like MongoDB or something, we have to rewrite the entire code dealing with persistence in the application. Therefore, when using a proprietary solution, we cannot immediately make the switch to another product. The switch requires a major restructuring of code and quite the re-investment of resources. We are sort of locked with the proprietary product of the vendor. This situation is known as vendor lock-in.

In this scenario, our persistence layer is locked in with the proprietary database of Google, and to move out, we have to redesign the data model from scratch. To avoid this situation, many businesses prefer to set up their own infrastructure and run open-source tech to have a cent-per-cent control. They have a long-term vision in mind.

https://www.datacenterdynamics.com/en/opinions/buying-cloud-scale-lessons-lyft-and-uber/


Hybrid cloud #
A service running on a hybrid cloud will have a few modules that run on a private cloud and other modules that run on a public cloud. Hybrid cloud architecture is a combination of public and private clouds, and it enables businesses to leverage the benefits of more than one cloud deployment model.

There are instances where businesses choose to keep sensitive data on-premises and leverage a public cloud to run other operations. Additionally, businesses running everything on-prem sometimes leverage the hybrid-cloud deployment model to augment their computing power.

Twitter is one good example of a business that leverages hybrid cloud architecture.

Multi-cloud #
Multi-cloud simply means leveraging multiple public cloud platforms to run a service. The upsides of deploying our service across multiple public cloud platforms are avoiding having dependence on a single cloud provider, leveraging different product offerings of multiple platforms, and having a degree of flexibility in cloud architecture.

There are also instances, generally in large corporations, where multiple teams work on dedicated modules of one big service, and they choose to deploy their module on a certain specific cloud platform. The business eventually ends up having its service deployed across multiple cloud platforms.

Being deployed on multiple platforms makes the businesses aware of the intricacies of every platform, and this helps significantly when making a decision to switch from one platform to another due to economic, technical, and any other reasons.

Here is one example of this. Gitlab made the switch from Microsoft Azure to Google Cloud Platform to run its services on Kubernetes.

Though one downside of having a multi-cloud architecture is the increase in complexity of the system. In this scenario, we have to manage services on different platforms. Big companies often hire platform specialists for every platform its service runs on to manage its system.

Community cloud #
A community cloud is a cloud infrastructure that caters to a certain community. It may be Fintech, Gaming, E-commerce, or another community. A community cloud focuses on providing solutions with respect to a certain domain.

For instance, a group of banks or financial institutions would join forces to set up a community cloud to address the common infrastructural needs of all the businesses running in the same domain. Open Science Data Cloud is one example of this. It’s a petabyte-scale scientific community cloud providing the resources for analyzing, storing, and sharing petabyte-scale scientific datasets.


