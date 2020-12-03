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

Although JWT is a robust mechanism, it is still prone to attacks. In this lesson, we will discuss what happens if a JWT is stolen. We will also discuss how a hacker can make changes in a token and mislead us in believing that it is a valid token.

What would happen if JWT is stolen #
If a hacker somehow gets access to our JWT, then there are two issues that we face:

1. Hacker can view sensitive information available in the token #
As we discussed earlier, a JWT string is just base64 encoding of the header, payload, and signature. If a hacker gets access to the token, then they can decode it and see the information within the token. Thus, it is advisable for the tokens to not contain any sensitive information like passwords.

2. The token can be used to access the application #
If your JWT is stolen or compromised, then the attacker has full access to your account. The attacker can send requests to applications, pretending to be you, and can make potentially harmful changes. One good thing is that the tokens expire after some time, so the hacker will only be able to use the token for a limited amount of time.

Where to store your JWTs #
As we know, a token is sent by the server which is stored on the browser for future requests. Now the question is, where should the token be stored on the browser? We have a couple of options:

1. Web Storage (local storage or session storage) #
If tokens are stored inside local storage, they are accessible by any script inside your page and thus vulnerable to cross-site scripting (XSS) attacks. In XSS attacks, the hackers can inject a malicious JavaScript code on your page. When this code runs, it can access the content of your local storage. Therefore, it is advisable to not store any sensitive information in the web storage.

2. Cookies #
When cookies are used with the HttpOnly flag, they are good candidates for storing JWTs as they are immune to XSS attacks. Additionally, we can use the Secure cookie flag to guarantee that the cookie is only sent over HTTPS.

However, cookies are also not completely safe as they are prone to CSRF attacks, as we have already discussed in previous lessons. Most modern web frameworks provide mechanisms to prevent CSRF attacks so we can consider storing our tokens in cookies.

How to invalidate a JWT #
If our JWT is somehow compromised, then we need some mechanism to invalidate our token. In session-based authentication, we can just close the browser and the session is destroyed. Unfortunately, it is not that easy in case of token-based authentication.

One option that we have is that the server should change its secret key. However, this will invalidate the tokens for all the users. This approach should be used if the application owner thinks that the JWTs of a large number of users are stolen.

Another option is maintaining a blacklist of all the invalid tokens. If a client suspects that the token is stolen, then they can logout from the browser. On doing this, the token for that user will be deleted from the browser storage and will be added to the blacklist present on the server. When the hacker sends a request with the stolen JWT, the server will find it in the blacklist and throw an unauthorized error.

Cryptographic Key Management

Let us look at some questions that can be raised regarding keys.

Will the secret key always remain the same, or will it be changed after regular intervals?

If the secret key is changed, then what would happen to the tokens signed by older keys?

If we are using asymmetric signing and the private key is changed, how will we share the new public keys with all the applications?

We will answer each of these questions one by one.

Will the secret keys rotate? #
Definitely yes! It is not safe or advisable to use the same key for a long time. If someone accidentally gets ahold of our applications key, then the attacker can send malicious requests to our server and we might not even know. If we rotate our keys regularly then we decrease the window of unauthorized access that an attacker gets.

Now the question is, how often should we change the keys? There is no definite answer to this, as it depends on the application. Some might change them every hour and others might keep the same key for a month. It depends on how many tokens you generate and how vulnerable your application is to attacks.

What would happen to old JWT once a key is changed? #
Changing the secret key is easy, the hard part is validating the tokens that were signed by the previous key. We can’t just invalidate the old tokens every time we change the key. There is a way to handle this problem. What if while generating the token, we also mention the key that was used for signing inside the header of the token? When we receive this token, we can check the header to see what key was used to sign it.

I know what you are wondering: if we write the key in the token itself, then an attacker can easily read our token and will get to know about the key. Here comes the trick. We will not write the actual key in the token but only an identifier. We will maintain a list of keyIds and corresponding keys in our memory or DB. When we receive a token, we will fetch the keyId from the token. Then we will look up our memory or DB for the actual key.

The JWT header supports a kid parameter to hold a key identifier. It can take any value, as it is just used to identify the actual key.

What would happen if the private key is changed in asymmetric signing? #
As we know that in the case of asymmetric signing, the private key is used to sign the token and it can be verified by all the applications that have the public key. If we keep rotating the private key, then the public key will also change. How will an application get to know which public key to use?

We can associate each public key with a keyId and provide this keyId in the kid parameter of the token header. But in that case, each application will have to maintain a set of public ids for lookup. This is not a feasible option.

We have a JSON Web Key specification that offers a way to represent cryptographic keys in a JSON format. A JWK can be included in a JWT token as a way to distribute the public key. We have two ways in which we can include the public keys in our token header:

1. Directly embedding the public key #
As the name suggests, public keys are public. So even if we add them into the token, it is not a security threat, as everyone can easily access the public key.

However, we don’t add the public key directly into the token. We can convert the public key into JSON format using any of the available libraries. A JSON object that represents a cryptographic key is called JWK.

A JWK can be included in the token header using jwk parameter.

2. Embedding a URL which contains the key #
We can maintain the complete list of all the public cases at a particular location. Then in the token header, we can provide the URL of this location along with the key identifier. There are two claims available which help us in doing this. The first is kid, which we have discussed earlier also. It will contain the key identifier. The second claim is jku. It contains the URL of the location where all the keys are stored.

Hacking JSON Web Tokens

At this point, we have discussed the ins and outs of JWTs. We have seen how they are generated, validated, and how their keys are managed. We have also discussed what would happen if an attacker steals our JWT. But there is one thing which we have not discussed yet: is it possible for an attacker to create a JWT (without knowing your secret key or private key) and making you believe that this is a valid token?

In other words, is it possible for an attacker to change the data within a token, and have it still be validated by our server? Unfortunately, there are some ways through which an attacker can do this. Some of these issues have been caught already and fixed and some require extra caution from the token generator.

We will discuss each of these methods below:

1) Brute Force Approach #
In symmetric signing, we use a secret key to sign the token. If an attacker gets our secret key, the attacker can change the data in the token, sign it again using the secret key, and send it with the request.

If an attacker has our valid JWT then the attacker can brute force various symmetric keys and compare the signature result to the known-valid signature. If there is a match, then the attacker has discovered the symmetric key and can modify and forge JWTs at will. There are plenty of libraries for doing this.

To save ourselves from a brute force attack, we should carefully select our secret key. It should not be too easy to guess.

2) None Algorithm #
In the alg claim, we provide the algorithm that is used to sign or encrypt the token. Earlier this claim was allowed to take None as value. If a token has None value in alg claim, then it means that this token need not be validated.

Any attacker can create a token with alg claim as None and get access to our resources. This issue was fixed in 2015 but there still might be some libraries that allow None value in alg claim.

3) Modify the algorithm RS256 to HS256 #
We already know that HS256 uses a secret key to sign and validate the token. We also know that RS256 uses a private key to sign the token and public key to validate it. Now if an attacker has access to our token (which is signed using RS256) then the attacker can change the token data using the following steps:

Change the algorithm in alg parameter from RS256 to HS256.
Make changes in the payload.
Sign the token using the public key (assuming the attacker has access to the public key). Please note here that the public key cannot be used for signing. But, since the algorithm is changed to HS256, the public key will act as a secret key.
When this token will be received by the application, it will see that the algorithm is HS256. It will use the public key as a secret key and the malicious user will get access to the application.



