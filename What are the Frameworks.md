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


**Angular** is a JavaScript framework created by Google that has been designed specifically for creating dynamic web applications. AngularJS addresses the limitations of HTML dynamic views in web applications and allows you to extend HTML vocabulary for your application. The resulting environment is highly expressive, readable, and quick to develop. Angular is used primarily to update the user interface in real time and provide a highly interactive website. 

**Bootstrap**, which can easily be categorized as the most used open-source framework in the world, was created by Twitter developers and primarily served to ease up the process of adding CSS to HTML. Bootstrap, like any other front-end framework, includes CSS, HTML, and JavaScript components. It adheres to responsive web design standards, and thus, allows users to develop responsive websites of all complexities and sizes.

**React** is a JavaScript library for building user interfaces. While there are doubts about whether it is an actual framework, it is a highly popular library that is used to build the View layer of an MVC application and warrants discussion in the context of front-end development. React is a component-based library that allows users to build encapsulated components, each of which manages its own state, and then compose them to make complex User Interfaces. The benefit of this is that when data changes, React makes sure that only the concerned components are updated.

**Backbone.js** is an extremely light framework that allows you to structure your JavaScript code in an MVC (Model, View, Controller) form. Backbone makes use of models, views, and collections to ensure that your program does not become entangled in a myriad of callbacks and other extraneous pieces of code that make changes complicated. Instead, the models represent the data of the application and Backbone ensures that any changes to these models automatically trigger changes to any views that display these models.

While **Semantic-UI** is a relatively new framework, it stands out in a number of ways. The primary distinction this particular framework enjoys is its simplicity. Semantic-UI uses natural language, and the code is, therefore, largely self-explanatory, thus making it highly desirable for beginners, particularly those with little or no coding experience. In addition to this, Semantic-UI is also integrated with a myriad of third-party libraries. This means that the development process becomes much easier because, for simpler applications, all the libraries you might require might already be integrated with the framework. Semantic-UI, therefore, is a great starting point for developing the front-end of beginner level websites. However, its package sizes are considerably larger than those of Foundation and Bootstrap, and it may not be a viable option when developing websites with more complex structures.

