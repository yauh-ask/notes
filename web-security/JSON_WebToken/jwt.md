What is JWT? #
A JSON Web Token (JWT) is a standard that defines a safe, compact, and self-contained way of transmitting information between a client and a server in the form of a JSON object. A JWT can either be signed (JWS) or encrypted (JWE) or both. If a JWT is neither signed nor encrypted, then it is called an insecure JWT.

JWT is one way of creating an access token. There are few alternatives to JWT such as Branca, Pasito, and Macaroon.

By signing the JWT, its integrity will be maintained. Other parties will be able to see the data in the JWT but will not be able to modify it.

By encrypting the JWT, its secrecy is maintained between two parties. Other parties will not be able to see the data, but if they change anything then we will not be able to find out.

In this lesson, and in further lessons, we will be discussing signed JWTs. Encrypted JWT is a more complex topic and is out of the scope for this course.

Common use cases for using JWT #
Here are some use cases in which JSON Web Tokens are useful:

1) Authorization

One of the most important use cases of JWT is the authorization. Suppose we are using an application that needs some data from our Gmail. We can authenticate ourselves on the Gmail authentication server by providing credentials. Gmail will provide us with a JWT, which our application can use to get data from Gmail. The token will contain information regarding what data can be accessed.

2) Information Exchange

JWT can also be used to share certain information between two parties secretly.

JWT Structure #
A JSON Web Token is basically three strings separated by a . (dot)

We will discuss each part of the JWT and see what they mean.

1. Header #
This is the first part of JWT. It is also known as the JOSE header (JSON Object Signing and Encryption). This header describes what algorithm is used to sign or encrypt the data contained in the JWT.

The header defines two attributes:

a) alg: the algorithm used to sign or encrypt the JWT.

b) typ: the content that is being signed or encrypted.

Now when we encode it to base64encode, we get the first part of our JSON web token. This is just encoding and not encryption. Anyone can easily decode this string and get the JSON.

2) Payload #
This is the second part of JWT. It contains the main information that the server uses to identify the user and permissions. The payload consists of claims. Claims are statements about an entity (typically the user) and additional data.

There are three types of claims.

a) Registered Claim Names

These are reserved names that provide a starting point for a set of useful, interoperable claims.

iss: identifies the principal that issued the JWT.

sub: identifies the principal that is the subject of the JWT.

aud: identifies the recipients that the JWT is intended for.

exp: identifies the expiration time at or after which the JWT MUST NOT be accepted for processing.

nbf: identifies the time before which the JWT MUST NOT be accepted for processing.

iat: identifies the time at which the JWT was issued.

jti: The JWT ID is a unique identifier for the JWT. The identifier value MUST be assigned in a manner that ensures that there is a negligible probability that the same value will be accidentally assigned to a different data object. It can be used to prevent the JWT from being replayed. This is helpful for a one-time use token.

Suppose a JSON web token is assigned to a user with jti as 1234. This user will use this token once, and suppose an attacker gets access to the token. When the attacker sends this token again, then the server will check the jti field and it will get to know that the token has been used earlier. It will not allow the token to be used again. Another benefit of the jti field is that it can be used to blacklist the tokens.

b) Public Claim Names

Public claim names are JSON Web Token Claims that can be defined at will by those using JWTs. However, in order to prevent collisions, any new claim name SHOULD either be defined in the IANA Registry, JSON Web Token Claims Registry, or be defined as a URI that contains a collision resistant namespace.

c) Private Claim Names

A producer and consumer of a JWT may agree to any Private claim name that is not a Reserved claim name or a Public claim name. Unlike Public claim names, these Private claim names are subject to collision and should be used with caution.



Now when we encode it to base64encode, we get the second part of our JSON web token.

3) Signature #
The third and final part of JWT is the signature. It is created by combining the header and payload parts of JWT and then hashing them using a secret key.

Since this is a signature, if someone tries to decode it they will not be able to get the JSON.

JWT VALIDATION:

Here is the basic flow of JWT authentication:

The client sends a request to the server with user credentials.
The server generates a signed JWT for the client if the credentials are valid.
The server sends the token back to the client which is stored in the browser.
For every subsequent request, the client sends the token back to the server.
The server validates the token, and if it is valid then grants access to the client.

How tokens are signed #
There are two mechanisms to sign a token:

1. Symmetric Signatures

When a JWT is signed using a secret key, then it is called a symmetric signature. This type of signature is done when there is only one server that signs and validates the token. The same secret key is used to generate and validate the token. The token is signed using HMAC.

HMAC stands for Hashing for Message Authentication Code. It’s a message authentication code obtained by running a cryptographic hash function (like MD5, SHA1, and SHA256) over the data (to be authenticated) and a shared secret key

2. Asymmetric Signatures

This signature is suitable for distributed scenarios. Suppose there are multiple applications that can validate a given JWT. If we use a secret key to sign a JWT, then these applications will need that key to validate the token.

It is not possible to share the secret key amongst all the applications, as it may get leaked. To solve this issue, asymmetric signing is done. Asymmetric signing uses a private-public key pair for signing. There is one server that has the private key. This server generates the tokens, signs them using the private key, and shares it with the client.

Now the client can send this token to any application and they can validate it using the public key. This signature is done using RSA. It is asymmetric encryption and a digital signature algorithm.

How is token validated #
Let us now look at how a server validates a JWT. We already know that a JWT has three parts: a header, a payload, and a signature.

When a server receives a token, it fetches the header and payload from that token. It then uses the secret key or the public key (in the case of asymmetric signing) to generate the signature from the header and payload.

If the generated signature matches the signature provided in the JWT, then it is considered to be valid.

Claims validations #
It is not sufficient to just validate the signature of the token. There are a few other security properties that need to be validated as discussed below:

Check if the token is still valid. This can be validated through exp claim.
Validate that the token is actually meant for you through the aud claim.
Check if the token can be used at this time using the nbf claim. NBF stands for not before which means that this token should not be used before a particular time.

