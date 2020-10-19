The web, simply put, is a network spread across the globe that connects a multitude of devices and allows them to communicate with one another. Websites on the Internet are hosted on devices referred to as servers, and when you’re interacting with a webpage on the Internet, what you’re essentially doing is exchanging data with the server that the website is hosted on. The device that you’re accessing the webpage using is referred to as the client in the context of the web. In short, the web enables the exchange of data between clients and servers through several elaborate mechanisms that we will be discussing in this chapter.

Network layers #
Since the web is an immensely intricate and widespread network, machines within the network are typically divided into abstract layers, each of which performs a specific task that aids in the overall communication process. The layers are enumerated below:

Application Layer
Transport Layer
Network Layer
Data Link Layer
Physical Layer
Each layer is built on top of the previous layer and has protocols that implement specific functionalities that are involved in the data exchange process.



Physical layer #
The physical layer of a machine refers to the physical wiring and circuits that go into making the machine available on the network.

Data link layer #
The data link layer is responsible for transmitting data from any given machine to a device or machine that is exactly one link away.

Network layer #
The network layer is responsible for connecting any two machines on the Internet. It provides global connectivity and allows for end-systems to communicate with one another on a large scale, beyond what the data link layer has to offer.

Transport layer #
The transport layer is responsible for connecting applications on the Internet. It demultiplexes data coming in from a single source and transmits it to the application it is intended for. The basic purpose of the transport layer in the context of the web is that it provides process-to-process communication; it allows two individual processes on either the same machine or separate machines to send messages to each other. To do so, it uses sockets, which are essentially just the gateway to a process. In other words, sockets are the means through which messages are received and sent out by a process.

Application layer #
The application layer is responsible for process-to-process communication across the Internet. It is the topmost layer in the hierarchy, and the application itself is built on top of this. The application layer provides a communication interface and end-user services to the application for its communication with single processes.

**Ports** are the endpoints of the communication between clients and servers. That is to say; ports are where messages from the network arrive on an end-system. We briefly discussed sockets earlier and talked about how they are the gateways to processes; sockets are opened on ports in order to allow processes to send and receive messages. Ports are designated by numbers, and all ports below 1024 are associated with a specific protocol each by default. The port number for HTTP, for instance, is 80, and what this means is that any messages you send or receive on the web come in to and leave your machine on a socket at port 80. Ports above 1024 are open ports available to programmers to use for any process they want to communicate with a network. They can build sockets on these ports and define the structure and type of messages this socket can cater to through socket programming. Socket programming is an aspect of Computer Networks 
