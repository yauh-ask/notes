The Implicit grant type is designed for single-page JavaScript apps that do not have a backend. In the previous lesson, we discussed Authorization Code grant flow, in which the client app used the client_secret and authorization code to get the access code.

The problem with JavaScript apps (without a backend) is that they have no way to store client secrets. Storing the client secret in the JavaScript code is not as safe, because anyone can access it. Therefore, we use the Implicit flow for these apps. In Implicit flow, the authorization server directly returns the access token instead of returning the code.

This flow type should be used only if there is no alternative option, because it is not safe. The exchange of token happens at the front end and an attacker can access the token.

Implicit grant type working #
Now we will look at the detailed working of implicit grant type.

Step 1 => Authorization Request #
This step is similar to the first step in the previous flow. The only difference is that the redirect_url parameter will contain a token as value.

The query parameters sent with the request are:

response_type: Since we are requesting for the access token directly, this parameter will contain a token.

client_id: The client id of the app.

redirect_uri: This is the uri to which the authorization server redirects once it has finished interacting with the resource owner.

scope: The optional parameter defining the resources being requested.

state: This parameter is optional in this flow as well.

The complete request looks like this:

https://authorization.server.dummy.com/authorize
?response_type=token
&client_id=12345
&redirect_uri=https://client.dummy.com/callback
&scope=images.read
&state=abcde
Step 2 => Authorization Response #
Once the user authenticates and provides permissions to the authorization server, it will redirect the browser to redirect_url specified by the client app in the request. The authorization server will then add a token and state to the fragment part of the URL.

Please note that the client will receive an access token, whereas in the previous flow it was receiving authorization code.

The token is returned in the URL fragment instead of in the query string. The reason for this is to ensure that the app will be able to access the value from the URL.

Here is what the response looks like:

https://authorization.server.dummy.com/callback
#access_token=hhdf6hsbhjG66hgtgfGGHJGCHJ
&token_type=bearer
&expires_in=500
&state=abcde
The expiration time of this token is kept a little less because this flow is not safe.

Note: This grant does not return a refresh token because the browser has no means of keeping it private.
