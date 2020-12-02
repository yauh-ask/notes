In the previous lesson, we discussed that in session-based authentication, the user information is stored on the server. This resulted in lots of issues related to performance and scalability. But what if we don’t want to save the user information on our server? We can’t save the user information in cookies as they have a size limit and also it is not safe.

We have an alternative to cookies, and that alternative is tokens. A token can store all the user information in an encrypted format and this token can be stored on the client-side.

Here is the basic flow of token-based authentication:

The client sends a request to the server with a username/password.
The application validates the credentials and generates a secure, signed token for the client.
The token is sent back to the client and stored there.
When the client needs to access something new on the server, it sends the token through the HTTP header.
The server decodes and verifies the attached token. If it is valid, the server sends a response to the client.
When the client logs out, the token is destroyed.

Benefits of token-based authentication #
The following are the benefits of using token-based authentication:

1. Scalability and Statelessness #
The token-based authentication is truly stateless. The server does not store any client information. Each time a request is made, the client sends the complete information through a token. This is very useful if our application is deployed on multiple servers.

2. More Secure #
The token is encrypted, so it is much more secure than cookies. Also, the token expires after some time so the user will have to login again.

3. Can be generated anywhere #
It is not necessary that the server or application which is validating the token should also generate it. The token generation process can be done on a separate server or by a different company.

4. Helpful in Authorization #
Within the token payload, you can easily specify what resources a user can access. For example, if a third-party API wants to access my Gmail account then I can provide a token that will allow that API to collect only my contact information from Gmail. It will not be able to access other resources.

Types of Tokens #
There are basically two token types:

Access Tokens
Refresh Tokens
Access tokens are used to grant access to a protected resource. When a client first authenticates it is given both types of tokens, but the access token is set to expire after a short period. By doing this, even if someone manages to get access to your token, it can be used only for some time.

Refresh tokens are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with an identical or narrower scope. It does not need the credential information again. The refresh token is also valid for some duration, but it is much more than an access token.

Although the refresh token does not need the user’s credentials again to generate an access token, it still requires the client id and client secret (we will look at these terms in OAuth lessons). So even if attackers get a refresh token, they will not be able to get the access token.

