OAuth 2.0 is designed only for authorization. It is used for granting access to data and features from one application to another. In OAuth, the client is given a token which it uses to access the data on the resource server, but it doesn’t get to know anything about the user. OAuth was used for authentication as well, but since it was not designed for authentication it was extended further to support authentication.

OpenID Connect is an extension of OAuth. It is a thin layer above OAuth which adds support for authentication.

You may have seen that when you try to login to an app, then the app can prompt you to authenticate using your Facebook or Google account. In this case, the app is probably using OpenID Connect. OpenID Connect allows a range of clients, including web-based, mobile, and JavaScript clients, to request and receive information about authenticated sessions and end-users.

Local user authentication #
Let’s suppose we are not using OpenID Connect or any Identity Provider (discussed in the next section) for authentication. In that case, our application will have to maintain a local database in which we will store user information and credentials. This seems like an easy solution but there are a few problems:

If our organization has lots of applications, then maintaining a database for each application is a tedious task. It requires resources and staff to manage.
Users find the task of signing up as cumbersome. First, they need to remember so many passwords, and second, it is likely that they’ll use the same password everywhere. If that password gets compromised, all the applications that the user uses with that password will also become compromised.
Identity Providers #
To solve the problem of local authentication, Identity Providers came in the picture. As the name suggests, Identity Providers take care of your authentication needs while you focus on your main business. They provide the identity of the user so that organizations can directly onboard the user without asking for any details.

It is a win-win situation for both the user and the organization. The organization is not required to store the personal data of its user, and the users are saved from creating an account each time they need to use some application.

What is OpenID Connect? #
There should be a standard way for client apps to communicate with the Identity Providers. OpenID Connect is one of those standards that defines how a client and Identity Provider should interact.

The OpenID had two earlier versions, OpenID 1.0 and OpenID 2.0. Its third iteration is called OpenID Connect. OpenID Connect is the most widely used, due to its simplicity and usability. Since the information is passed in the form of JWT, OpenID connect can be used across different implementations.

Participants in OpenID Connect #
End User: End User refers to the entity for which the client is requesting identity information. This is called Resource Owner in OAuth.

Relying Party: This is the party that relies on the authorization server to provide the identity of the End User. This is called client in OAuth.

Identity Provider: This is a server that provides identity information about the End User. This is called Authorization Server in OAuth.

TERMINOLOGY

Identity token #
While discussing OAuth, we discussed the authorization code and access token. In the case of OpenId Connect, there is one more token that we can request. This token is called the identity token, which encodes the user’s authentication information.

In contrast to access tokens, which are only intended to be understood by the resource server, ID tokens are intended to be understood by the client application. The ID token contains the user information in JSON format. The JSON is wrapped into a JWT.

When a client receives the identity token, it should validate it first. The client must validate the following fields:

iss - Client must validate that the issuer of this token is the Authorization Server.
aud - Client must validate that the token is meant for the client itself.
exp - Client must validate that the token is not expired.
Here is some sample user information in the form of JSON present in an identity token.

{
  "iss": "https://server.example.com",
  "sub": "24400320",
  "aud": "s6BhdRkqt3",
  "nonce": "n-0S6_WzA2Mj",
  "exp": 1311281970,
  "iat": 1311280970,
  "auth_time": 1311280969,
  "acr": "urn:mace:incommon:iap:silver"
}
Let’s look at what these values mean:

iat - The iat claim identifies the time at which the JWT was issued. This claim can be used to determine the age of the JWT. Its value must be a number containing a NumericDate value.
auth_time - Time when the End-User authentication occurred. Its value is a JSON number representing the number of seconds from 1970–01–01T0:0:0Z as measured in UTC until the date/time.
nonce - ID token requests may come with a nonce request parameter to protect from replay attacks. When the request parameter is included, the server will embed a nonce claim in the issued ID token with the same value of the request parameter.
The Identity token contains only basic information about the user. To get the complete user information, the client must send the access token (please note access token should be sent not identity token) to UserInfo endpoint.

Scope #
The Identity Provider may have a lot of information about a user. Some of this information can be shared freely with the client apps and some information might be shared under special circumstances.

The client app must also tell the Identity Provider about what user information it is looking for. This information can be provided through the scope field. There are four types of scopes defined in OpenID Connect. Each of these scopes defines certain attributes.

When a particular scope is requested, then all the attributes defined under that scope are returned.

Please note that there is one more scope value, i.e. openid. This value is mandatory if the client app needs an identity token in the response.

Claims #
Simply put, claims are name/value pairs that contain information about a user. For example, a family_name claim is used to send the family name of a user. The benefit of claims is that each client knows what claims to look for to get particular user information. The client app can either request the category of a claim by providing the scope field or it can request individual claims using the optional claims request parameter.

Endpoints #
The authorization server defines some endpoints that are used by the client to request some data.

The core endpoints are defined below:

1. Authorization endpoint

We have discussed this endpoint in OAuth as well. This endpoint returns the authorization code after the user authenticates and provides their consent to the authorization server (called the Identity Provider in case of OpenID).

2. Token endpoint

This endpoint is used to exchange an authorization token with an access token and identity token. The identity token contains some basic user information. More on this later.

In the case of OAuth flow, we used to only get the access token. Now, we are getting an additional identity token which contains basic user information. To get this additional token, some changes are made in the request. We will discuss this in the next lesson.

3. UserInfo endpoint

The UserInfo endpoint is used by the client to request user profile information that was previously granted access to. To access this information, the client needs to send an access token with the request. The user fields are returned in the form of JSON which may or may not be encapsulated in a JWT.

Following is a sample response from this endpoint:

HTTP/1.1 200 OK
Content-Type: application/json

{
  "sub"            : "Joe",
  "email"          : "Joe@dummy.net",
  "email_verified" : true,
  "name"           : "Joe Frank"
}

Authorization Code Flow for Authentication

The Authorization code flow for OpenID Connect is similar to the Authorization Code Flow that we discussed in the OAuth 2.0 chapter. The only difference is the change in the value of the scope field. It must contain openid as one of the values, followed by other scope values based on what type of user data the client wants.

There are two questions that can be raised:

What would happen if the client does not provide an openid in the scope field while sending a request to the authorization server?
The answer is that in this case, the flow will work as a normal authorization flow. The client app will not get access to the user information as it will not receive the identity token.

Can user information be fetched from the UserInfo endpoint by sending the access token in the request even if openid was not provided in the scope field when an access token was requested?
The answer is NO. When we send a request to the token endpoint to fetch the access token, then we must send openid in the scope field. We must also send other scope values like email or address if we want to get this information. The access token that is returned is based on the scope values that were sent with the request. When we hit the UserInfo endpoint, then only that user information is returned which the access token is authorized to get.

Let’s say that while sending a request to the token endpoint, the scope value is “openid email”. The client sends this request and gets an access token. If the client sends this access token to the UserInfo endpoint, it will get only email information. It will not get an address or any other information.
