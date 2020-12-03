What is OAuth 2.0? #
OAuth 2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity while providing specific authorization flows for web applications, desktop applications, mobile phones, and living room devices.

As the definition suggests, OAuth is a protocol that simplifies the process of providing authorization to clients to access secured resources.

In other words, OAuth is an authorization framework that allows a client app (PicsArt App) to retrieve information from another system using a token which is valid for a limited time. The application users authorize the client app to retrieve information on their behalf.

Some developers have some confusion about whether OAuth is used for authentication or authorization or both. The answer is that OAuth is specifically meant for authorization. It has an extension called OpenId Connect which can be used for authentication. But OAuth should only be used for authorization.

The second example that we discussed above can be implemented through OAuth. OAuth defines various specs and flows using which clients can access the secured resources.

Why shouldn’t OAuth be used for authentication? #
During authentication, a client app will need some user information. The client app can send the token to the resource server (Facebook in our example) to get the user information, but it is a bad idea because there is no standard way to send the user information back to the client. If applications use OAuth for authentication, then every implementation will be different, which will be a problem. This is the major problem using OAuth for authentication.

On the other hand, OpenId Connect defines a standard way to return user information. It defines a UserInfo endpoint which can be used to access user information.

