*A web framework* is defined as a package made up of a structure of files and folders of standardized code (HTML, CSS, JS documents, etc.), which can be used to support the development of websites as a basis to start building a site. Essentially, frameworks provide some basic, standard starter code that allows developers to build the meat of their website on.

Most websites share a very similar structure, and the aim of frameworks is to provide this common structure as a starting point so that developers don’t have to redo it from scratch and can reuse the provided code. Frameworks, therefore, serve to simplify the web development process.

# MVC architecture #
Before we introduce some of the common types, frameworks, can be categorized in, let’s discuss the underlying architecture of frameworks. Most, if not all, web application frameworks rely on the Model View Controller architecture. The pattern serves to separate the application logic from the user interface, thus forming the three components that the name is comprised of.

**Model**

The Model stores all information about the content and structure of an application. Upon receiving user input data from the Controller, it communicates any required interface updates to the View component.

**View**

This refers to the application’s front-end, or what is more commonly known as the user interface. It contains information about the layout and the way users can interact with any of its parts. The View receives user input, communicates it to the Controller for processing, and updates itself according to the instructions it, in turn, receives from the Model.

**Controller**

The Controller is an intermediary between the Model and the View. It receives user input from the View, processes it, and mediates required changes between the two.


# Types of frameworks #
There are both front-end and back-end frameworks that are very popularly used, and you may already have heard of them. 
Additionally, there are multiple isomorphic frameworks available that work on both the front-end and the back-end and serve as a bridge between the two.

- Front-end (client-side) frameworks
Angular JS
Bootstrap
React.js
Backbone
Semantic-UI

- Back-end (server-side) frameworks

Express (JavaScript)
Symfony (PHP)
Django (Python)
Ruby on Rails (Ruby)
ASP .NET (C#)

- Isomorphic (client-server) frameworks

Meteor JS
Lazo.js
Rendr


____
FRONTEND

**Angular** is a JavaScript framework created by Google that has been designed specifically for creating dynamic web applications. AngularJS addresses the limitations of HTML dynamic views in web applications and allows you to extend HTML vocabulary for your application. The resulting environment is highly expressive, readable, and quick to develop. Angular is used primarily to update the user interface in real time and provide a highly interactive website. 

**Bootstrap**, which can easily be categorized as the most used open-source framework in the world, was created by Twitter developers and primarily served to ease up the process of adding CSS to HTML. Bootstrap, like any other front-end framework, includes CSS, HTML, and JavaScript components. It adheres to responsive web design standards, and thus, allows users to develop responsive websites of all complexities and sizes.

**React** is a JavaScript library for building user interfaces. While there are doubts about whether it is an actual framework, it is a highly popular library that is used to build the View layer of an MVC application and warrants discussion in the context of front-end development. React is a component-based library that allows users to build encapsulated components, each of which manages its own state, and then compose them to make complex User Interfaces. The benefit of this is that when data changes, React makes sure that only the concerned components are updated.

**Backbone.js** is an extremely light framework that allows you to structure your JavaScript code in an MVC (Model, View, Controller) form. Backbone makes use of models, views, and collections to ensure that your program does not become entangled in a myriad of callbacks and other extraneous pieces of code that make changes complicated. Instead, the models represent the data of the application and Backbone ensures that any changes to these models automatically trigger changes to any views that display these models.

While **Semantic-UI** is a relatively new framework, it stands out in a number of ways. The primary distinction this particular framework enjoys is its simplicity. Semantic-UI uses natural language, and the code is, therefore, largely self-explanatory, thus making it highly desirable for beginners, particularly those with little or no coding experience. In addition to this, Semantic-UI is also integrated with a myriad of third-party libraries. This means that the development process becomes much easier because, for simpler applications, all the libraries you might require might already be integrated with the framework. Semantic-UI, therefore, is a great starting point for developing the front-end of beginner level websites. However, its package sizes are considerably larger than those of Foundation and Bootstrap, and it may not be a viable option when developing websites with more complex structures.


______________
BACKEND

The back-end refers to the server-side of a web application. The back-end spans everything from the initial creation of the server to the handling of user requests on the application. 


**Express.js** often referred to as the “de facto standard server framework” for Node.js, is a minimal and highly flexible Node.js web application framework that provides a robust set of features for web applications. The idea behind Express is to simplify the back-end development process enough to reduce basic back-end features such as creating an HTTP server from multiple, unintelligible lines of Node.js code, to a single instruction, while simultaneously keeping the core syntactical and logical characteristics of Node.js intact.

**Symfony** is a web development framework for PHP. The key idea behind Symfony is that it is essentially a set of reusable components. The benefits of this are obvious; with over 30 standalone components at your disposal, the process of writing an application becomes considerably simplified and, consequently, much easier and more efficient. Symfony, like the previous frameworks we have discussed, allows for more compact, readable, and simple code. This is beneficial because it allows you to focus on the higher-level functionality you want to implement as the more mundane tasks become confined to much smaller pieces of code that do not need to be thought about from scratch.

**Django** is a high-level Python web framework that enables the rapid development of secure and maintainable websites. Django, like Express, takes care of reducing code for basic functionalities to simple instructions, so you can focus on writing your application and implementing more specific functionality without needing to reinvent the wheel and getting caught up in needlessly long bouts of code in doing so!

Ruby on Rails, also known as Rails, is a server-side web application framework written in Ruby. Rails is built on the Model View Controller architecture that we have previously studied, and it provides default structures for everything that goes into each component, including databases, several common web services as well as web pages themselves. Ruby on Rails, therefore, separates the process of web development into simplified components and provides a basic structure for each element any given component comprises of, thus making it immensely convenient for users to build their own specific functionality on top of these provisional structures without having to worry about starting from the very basics.

ASP.NET is an open-source, server-side web development framework for building modern web applications and services using .NET or any language supported by .NET. ASP .NET was developed by Microsoft to facilitate the process of developing dynamic web pages, and it has, therefore, considerably simplified the process of creating websites based on HTML5, CSS, and JavaScript. As a result, it has made it possible for users to create websites that are not only simple and fast but also have the capacity to scale to millions of users.

Client-server frameworks, or isomorphic frameworks, are frameworks that support both front end and back end development, thus allowing developers to write their entire application in a single framework without having to worry about integrating multiple components written in different frameworks.

Meteor JS #
Meteor, or Meteor JS, is an open-source client-server JavaScript framework that has been written in Node.js. In addition to having the benefit of being a stand-alone framework that allows for development on both the front and back end of an application, Meteor also allows for prototyping, which means that it allows for versions of the same application to be stored and tested. In addition to this, Meteor also produces code that can span multiple platforms including Android, iOS, and the web itself.

On the server-side, Meteor integrates with MongoDB and follows protocols to create a database management mechanism that enables data changes to be propagated directly to the client-side without having to write any synchronization code on both ends explicitly.

On the client-side, Meteor has its own templating engine called Blaze that allows users to choose from templates for the user interface to customize, thus making the front end development much easier. Alternatively, Meteor can also be used with some of the front-end frameworks we have already studied. It can be integrated with the Angular or React frameworks to seamlessly produce user interfaces that don’t require too much work.

Lazo.js #
Lazo.js is a client-server web development framework built on Node.js that has the benefit of providing front-end developers with a simple, and relatively familiar syntactical structure that they can use to create MVC structured web applications that are separated as multiple sophisticated components that come together to form the complete front-end. LazoJS has the added benefit of providing an optimized first-page load, something that is often a key determinant of user experience. These benefits are achieved using a combination of tools comprised of Backbone.js, RequireJS, and jQuery.

Lazo was initially created to address the issues that spring from creating an entire website front ends as a single unit or single page applications instead of separating the user interface into mutually exclusive components. Lazo, in turn, not only provides front-end engineers with a familiar environment for creating complete web applications but also ensures that components are separated as such to avoid overly complicated application logic. Pages are constructed via reusable, testable components that have their own life cycles, thus allowing developers to easily create complex views for the interface while providing excellent encapsulation and separation of concerns.

Rendr #
Rendr is a small library that allows you to run your Backbone.js applications on both the client and the server, depending on the specific needs of the web application you are developing. This means that Rendr provides users with mechanisms to build entire applications on either the client or server end in addition to the ability to distribute the code on both the client and server and using Rendr on both ends. Essentially, Rendr allows your web server to serve fully-formed HTML pages to any link within your application, while simultaneously preserving the feel of a traditional Backbone.js client-side MVC application.

In recent times the bulk of applications have been moving increasingly to the client side. However, this is not always suitable and may cause some problems. As a solution to this, Rendr is intended to be a building block along the way to create web applications that can be run on either side of the wire according to the specific needs of your application.

