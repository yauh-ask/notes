Software processes #
Now that we have a basic idea of what goes into developing a website and what its multiple components are, we will proceed to discuss the different ways in which we can structure the development process.

A software process is defined as a set of related activities that leads to the production of a software product, such as a website. The software processes we will be discussing in this chapter are all concepts that fall under professional software engineering that entails building large scale web applications. However, these are all important concepts that you should be familiar with if you are looking to take up web development professionally or eventually planning to deploy your website since they provide a methodology to the process that allows you to organize your work into logical stages.

There are several different software processes that we will discuss in this chapter; however, we will first outline the four fundamental software engineering activities that all of them must comprise of:

1.Software specification: Defining the intended functionality of the software and potential constraints on its operation. In the case of a starter web application, this would be the stage where you define the features you want to implement on your website.

2.Software design and implementation: Producing the software according to the specifications articulated. This is the stage where the actual application is developed.

3.Software validation: Ensuring the software does what users want it to do. During this stage, you make sure the features you wanted to implement have been implemented correctly.

4.Software evolution: The ability of the software to adapt with evolving user requirements. This is an ongoing stage where you continuously come up with features that you think would make your application better and implement them.


All process models can be categorized as one of the following:

- Plan-driven
- Agile

A plan-driven process is one where all of the process activities are planned in advance, and progress is measured against this plan.
An agile process is one where planning is incremental, and it is easier to change the process in accordance with changing customer requirements.

**The WaterFall Model**

The waterfall model is the first published model of the software development process, and it consists of representing the fundamental activities
of specification, development, validation, and evolution as separate, sequential process phases.

There are multiple stages involved in the waterfall model, and theoretically, every stage must be completed before the next one can be “cascaded” on to, 
which is why the model is referred to as the waterfall model.

## Analyse and define requirements

The system’s intended services, potential constraints, and goals are established and then defined in detail. 
These requirements then serve as a product specification, according to which the website is then developed.

## Design software

The design process entails allocating the requirements realized in the previous stage to different software components by establishing an overall system 
architecture. Software design involves identifying and describing the fundamental software system abstractions and the relationships amongst them that your
website will require.

## Implement and test units

During this stage, the software design is translated to a set of programs or multiple program units. 
Unit testing involves verifying that each unit meets its specifications.

## Integrate units and test system

The individual program units are integrated and tested as a complete system to ensure that the software requirements have been met. 
After testing, the software system is delivered to the customer. In the case of your own website, you would deploy it at this point.

## Operation and maintenance

Normally (although not necessarily), this is the longest life cycle phase. 
The system is installed and put into practical use. Maintenance involves correcting errors that were not discovered in earlier stages of the life cycle, 
improving the implementation of system units and enhancing the system’s services as new requirements are discovered.

_Conclusion_

The waterfall model is categorized as a plan-driven process since it requires a detailed plan to be in place before each stage can be executed. 
This model works best in large organizations that have several people working on large-scale projects which need detailed paperwork and records to coordinate 
with one another. However, in the case of personal websites or small projects, this approach may prove to be unnecessarily meticulous and extraneous since 
there is no need to keep elaborate records in that situation.


**Agile**

The incremental development approach is a fundamental agile process that entails interleaving the activities of specification, development, and validation. The system is then developed as a series of versions or increments, with each version adding functionality to the previous version.

The underlying idea in the incremental development process is to develop an initial version of your website, open it to feedback, and then incrementally develop newer versions based on this feedback. In this case, the specification, development, and validation phases all happen concurrently and feed into one another.

Incremental software development is better suited than a waterfall approach to most business and personal systems. This is because incremental development is a more intuitive way of solving problems. It is the equivalent of moving toward a solution in a series of steps, backtracking on mistakes, and iteratively reaching a solution. Moreover, developing the software incrementally means it is cheaper and easier to add changes to it while it is still being developed instead of having to wait for problems to be discovered after undergoing the entire development process.

## Incremental development vs. waterfall model

As we have already seen, the incremental development model is more intuitive than the waterfall model for developing the most common website use cases. In addition to this, there are a number of other benefits that incremental development has compared to the waterfall model, and they are enumerated as follows:

The cost of accommodating changing customer requirements diminishes significantly in this case as the amount of analysis and documentation that has to be redone is much less than in the waterfall model.
It is easier to get customer feedback on the development work that has been done since they can comment on physical demonstrations of the software and see how much has been implemented as opposed to judging from software design documents.
More rapid delivery and deployment of useful software to the customer is possible, even if all of the functionality has not been included. Customers are able to use and gain value from the software earlier than is possible with a waterfall process.
