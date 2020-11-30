Does the cloud provider already have a customer on board similar to your business? #
This is a very important factor in making up your mind to pick a certain cloud provider. For instance, say you need to deploy an augmented reality game like Pokemon Go, naturally you would want it to blow up just the same. This gives Google Cloud an edge up in your research because the GCP team has already scaled a service like yours to the moon and is well aware of the nitty-gritty and domain-specific issues related to it. Similarly, Fortnite has made it big running on AWS.

These kinds of success stories prove that your business won’t face any sort of performance, security, scalability, or high-availability issues when the service is subjected to a heavy traffic load on these respective platforms.

https://cloud.google.com/customers

Be thorough on the technology requirements and the resources you have #
If you do not want to be overwhelmed with the range of technology offerings and different pricing models cloud vendors offer when you open their website, you need to be crystal clear about what you want.

There is no workaround for this.

Do the math on how much you are willing to invest in the cloud infrastructure required to run your app and ascertain if you have the required resources.

https://cloud.google.com/products/calculator/
https://azure.microsoft.com/en-in/pricing/calculator/

Technology offerings of the cloud vendor in context to your use case #
It is pretty obvious that the cloud provider should have an end-to-end technology offering for running our service. Also, the hardware and the software they provide should be state-of-the-art, secure, and continually upgraded. Nobody wants to run their service on archaic infrastructure.

_What do I mean by an end-to-end technology offering?

Let’s say you pick a _ Database as a Service (DBaaS)_ to store data for your online service. Everything appears to be good. However, when your online service starts gaining traction, the log management, monitoring, disaster recovery, and other similar additional cloud services related to DBaaS let you down. You begin to feel the technological limitations of the platform. These limitations are a hurdle to your efficiency. It doesn’t matter how good their DBaaS is. If you cannot monitor DB logs efficiently, using their service is pretty pointless.

Another thing to consider is what if you decide to transition your data to a different database solution, or let’s say you want to move out of the cloud entirely and deploy your service on another cloud platform or on-prem. Does the vendor let you do that seamlessly?

Finally, let’s assume the database service and the end-to-end infrastructure stack are top-notch. The service is running smoothly, but now you need to implement machine learning on your data either for analytics or to pull out specific information from petabytes of images that you have.

Here is where state-of-the-art technology offerings, continual upgrade of the infrastructure, and staying ahead of the curve matters. A good cloud provider should be able to set up a machine learning data analytics for you smoothly.

Ultimately, you should think ahead about what additional products and technologies, besides the core product, you would need in the future to grow your business, and ask yourself “does the cloud provider fulfill all those requirements?” before you pick the right service.

Run a Proof of Concept (POC) before going all in #
Once you zero in on a cloud vendor, the best way to acquire insight into the technology, the platform, and the pricing model is to run a Proof of Concept (POC) on the cloud platform.

Let the POC run for a while, and then do a stress test on the app. Check if you are happy with the monitoring, analytics, logging, and other services. There is no better way to gauge the issues and the risks that you might have to deal with in future than this.

When you run your app on the cloud, the pricing models aren’t that straightforward and simple. For instance, if a vendor says you have x hours of instance time in a particular quota, that doesn’t mean you’ll get x instance hours, no matter what. Chances are you might not. Reason being, there are request-response data limits associated with the instance hour limit too.

If your request-response data limits get exhausted, you might not be able to use even x/10 instance hours. Once you run a POC, you’ll understand all these intricacies of the platform.



Check out the smaller niche players in the market #
If you have very specific needs, you can check out other smaller cloud vendors in the market that cater to those specific needs such as serverless, static hosting, and so on.

An upside of working with smaller providers is that they offer very competitive pricing models, features, tools, and customer support in comparison to the bigger players.

Vendor lock-in #
I can’t stress this enough, always look for an open-source solution first before you make up your mind to move forward with proprietary cloud technology. This reduces your vendor lock-in risk significantly.

When you are not locked in, if you don’t like a service, you can move to another vendor. However, when using a proprietary service, you are in for some serious code refactoring.

Vendor lock-in is something that is unavoidable when using a vendor-managed proprietary technology. If our business faces any sort of issue with the proprietary technology in the future, be it a technical limitation or a billing issue, it’s super hard to bail out because the code is tightly coupled with the proprietary tech.

To transition to a new cloud service, we may even have to write things from scratch, which can eat up quite a lot of business resources and time.

When we are locked-in, we have to rely on the vendor to roll out new features of the proprietary product. Since the code is closed source, we cannot write any custom features on our own. This strongly limits our ability to move fast.

Speaking of security, complying with the security protocols and regulations regarding the implementation of the proprietary product is, again, on the vendor.

On the contrary, when using open source, we have the freedom to write custom features and leverage other open industry frameworks, tools, and libraries that are continually patched by a dedicated global community.

Consider multi-cloud deployment - Break down your architecture into modules #
A multi-cloud deployment simply means do not put all your eggs in one basket. If you aren’t an indie dev or a small startup and have a comparatively bigger service to deploy, you can consider deploying your application across multiple cloud platforms.

This is only possible if your application has a loosely coupled architecture consisting of several microservices. These services can be deployed across multiple platforms eventually having no single point of failure in terms of cloud platforms. We are not locked in with just one cloud vendor.

The upside of doing this is that the developers and the operations teams get familiar with different cloud platforms, including their intricacies, pricing models, etc… In the future, it becomes easier to bail out on a certain platform and transition to another since things don’t have to be learned from scratch.



Security #
For many businesses, security is a decisive factor when making the decision to migrate to the cloud or not. If we work in finance, military, healthcare, or other similar domains and have sensitive data, we should go through the security policies of the cloud vendor thoroughly.

This is the reason most companies prefer a hybrid cloud architecture. The sensitive data is stored on-prem and the rest goes out to the public cloud. Moving data, also known as data in transit, is vulnerable to security breaches.

Here is a checklist of questions with respect to data security that you should put before the cloud provider you pick to run your service:

Is the cloud provider encrypting your data? Both at rest and in transit?
Does the provider ensure that only authorized accounts have access to your data? By authorized accounts, here I mean the accounts of cloud engineers of the platform managing your data.
Does it have a security marketplace with security products from different vendors in case you need it? How easy is deploying those tools on the platform?
Does the cloud provider comply with security standards and certifications applicable to your business domain?
What’s the vendor’s policy with respect to government legal requests for data?
Has there ever been any major security breaches or failures in the past?
How secure the data would be in case you implement a hybrid architecture and stream your data over to the cloud?
Does the provider have a dedicated security team to resolve issues as soon as they are encountered?
How are the data centers physically secured?
How are the users authenticated? What is the process for preventing network intrusions?
What are the data deletion policies?
Support #
Support is another important factor to consider when giving business to a cloud vendor. Do they have a dedicated technical support team? What’s the support policy? Is the support paid? If yes, what’s the support pricing model?

Cloud marketplace #
All the big cloud platforms have respective marketplaces that offer third party utilities, developer tools, solutions, and services to accelerate the development. Before writing a utility from the ground up, businesses generally look into the marketplace for that utility to save resources and time.

