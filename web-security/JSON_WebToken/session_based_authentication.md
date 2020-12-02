HTTP is a stateless protocol. This means that each HTTP request is considered an independent request and no information from the previous request is saved. If the application is static and it is available to everyone, then we don’t have any problems. We just need to inform the server which page we want to access, and we will get the result. If the application is dynamic, then we may need to send additional information regarding who is accessing the page.

Let’s say, for example, that we are shopping on Amazon. If we add certain items to our cart, then we should be able to see all the items even after we navigate to a different page. In this case, each time a request is sent to the Amazon server from the client, the client needs to send its identity.

In the below image Jane has sent a request to a web server to add an item to her cart. Jane is sending her credentials along with the request.

Jane is sending a second request but since HTTP is stateless, she needs to send her credentials again.

Introducing Session-based authentication #
If you look at the above example, we need to send our login information each time an HTTP request is made to the server.

This is not a good practice and can be frustrating for the user. To solve this issue, session-based authentication comes into the picture. It is also known as cookie-based authentication.

Below are the steps to create a session between a user and a web server.

The user (normally a browser) sends a request to the server. The request contains the login credentials of the user and the info it is requesting.
The web server authenticates the user. It creates a session and stores all the information about the user in memory or a database and returns a sessionId to the user.
This sessionId is stored by the user in browser cookies. The next time the user makes a request it sends the cookies as well in the HTTP header.
The web server looks at the sessionId and checks if it has any info regarding this sessionId.
If the sessionId is valid then the web server recognizes the user and returns the requested information.

Limitations of Session-based authentication #
There are a few limitations of the session-based authentication. We will discuss them here:

1. Problems faced in Distributed Systems #
We know that in session-based authentication, the session details are saved on the server. However, in a distributed system, it is not necessary that a request from a given user will always go to the same server. It’s quite possible that one request is handled by one particular server and the next request is handled by another server.

In this case, we can’t use session-based authentication as we can’t save the session info on both servers.
E.g. browser => load balancer => server1 || server2 || server3

2. Performance Issue #
Storing and retrieving the session information from the database or memory is a costly process. Each time a new user authenticates, we need to store their information. And whenever a user sends a sessionId with the request then we need to validate it from the database or memory. This leads to a lot of back and forth.

3. Cookie Fraud #
It is possible that a malicious user or a website could gain access to your cookies and then perform some malicious operations on a website. This is also known as CSRF attack, which we have discussed earlier.




