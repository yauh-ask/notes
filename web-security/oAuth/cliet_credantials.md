This grant type is used for machine to machine authorization. There is no user involved in this flow. Suppose we have an application that follows the microservices architecture. The application is divided into small parts and each part is deployed on a separate server.

If one internal server needs to access some data from the other server, then they can use the client credentials grant type.

Client Credentials grant type working #
Now, we will look at the detailed working of Client Credentials grant type.

Step 1 => Token request #
In this flow, there is a direct token request. Since no user is involved, the client directly sends an HTTP Post request to the authorization server.

The query parameters sent with the request are:

grant_type: Since we are requesting the access token using the client credentials, this parameter will contain client_credentials.

client_id: The client id of the app.

client_secret: The client secret of the app.

scope: The optional parameter defining the resources being requested.

The complete request looks like this:

POST /token/endpoint HTTP/1.1

  Host: authserver.dummy.com

grant_type=client_credentials
&client_id=12345
&client_secret=gh5Gdkj743HFG45udbfGfs
&scope=images_read
Step 2 => Token response #
If the client credentials are valid, a token is returned by the authorization server.

The response from the server is as shown below:

HTTP/1.1 200 OK
Content-Type: application/json

{
  "access_token":"YT3774ghsghdj6t4GJT5hd",
  "token_type":"bearer",
  "expires_in":3600,
  "refresh_token":"YT768475hjsdbhdgby6434hdh",
  "scope":"images_read"
}
