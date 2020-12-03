The Resource Owner password credentials grant type is used in cases where the resource owner trusts the client and is ready to share its credentials with the client. The authorization server should take special care when enabling this grant type and only allow it when other flows are not viable.

This flow was introduced to migrate existing clients using direct authentication schemes such as HTTP Basic or Digest authentication to OAuth by converting the stored credentials to an access token. Today, there is no case in which this flow should be used, as it is very insecure.

In HTTP Basic authentication, the server requests the client to present a username and password combination as part of the HTTP Basic challenge-response mechanism. With HTTP Basic Authentication, the client’s username and password are concatenated, base64-encoded, and passed in the Authorization HTTP header. The server can then authenticate this user against a user profile stored in the server’s local repository, a database, or an LDAP directory.

Resource Owner Credentials grant working #
Step 1 => Token request #
In this flow, the client collects the credentials from the user and sends a POST request to the authorization server.

The query parameters sent with the request are:

response_type: The value for this flow is “password”.
client_id: The client id.
client_secret: The client secret.
username: The username of the user.
password: The user password.
scope: Defines the resources to be accessed.
The requests sent looks as below:

POST /token/endpoint HTTP/1.1

  Host: authserver.dummy.com

grant_type=password
&client_id=12345
&client_secret=gh5Gdkj743HFG45udbfGfs
&username=Jone@xyz.com
&password=abcde
&scope=images_read
Step 2 => Token response #
If the client credentials and user credentials are valid, then a token is returned by the authorization server.

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
