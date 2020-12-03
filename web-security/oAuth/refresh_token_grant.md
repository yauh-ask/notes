As we have seen earlier, the access token is valid only for a certain time frame and it expires after the frame has ended. The reason for this is to ensure security because if the refresh token gets stolen, the attacker can use it until it expires (which takes a long time) or it is blacklisted on the server.

If the client asks the user to authenticate and authorize every time the access token expires then it will be very frustrating. To avoid this, the client app can use a refresh token. A refresh token is a token that can be used to get the access token when it expires. This should be kept highly confidential, because if an attacker gains access to refresh token then the attacker gets unlimited access to the resources.

There are different settings for refresh tokens which are defined by the authorization server. Some tokens are single-use only and others can be used multiple times. Also, the refresh token expires after some time, but this time is much longer than the expiration time of the access token.

Refresh tokens are usually subject to strict storage requirements to ensure they are not leaked. They can also be blacklisted by the authorization server.

Refresh token grant working #
Step 1 => Refresh token request #
If the client already has a refresh token, then it can exchange the refresh token for a new access token by making the HTTP POST request to the authorization server.

The following parameters will be sent with the request:

grant_type: The value for this flow is refresh_token.
refresh_token: The client id.
client_id: The client id.
client_secret: The client secret.
The complete request looks like:

POST /oauth/v2/accessToken HTTP/1.1
Host: authserver.dummy.com
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=k3hjJE5x1lZh-zjU-02w8EJW6l2jnuP8F1uXMgkm8nzjPfnaJR
&client_id=12345
&client_secret=hhdHFgggdFGfhd

Step 2 => Refresh token response #
If the client credentials are valid and the refresh token has not expired, then an access token is returned.

The response from the authorization server is as shown below:

POST /token/endpoint HTTP/1.1

  Host: authserver.dummy.com

  "access_token": "dgfYTGFVygPtyqytVfyGFtyF",
  "expires_in": 3600,
  "refresh_token": "GHcdkHJjcbhhBHJGbhjfgkHghB",
  "refresh_token_expires_in": 500000
  
  Which flows allow refresh token grants? #
Out of all the four flows that we discussed earlier, two do not allow refresh token grants:

Implicit grant type - In this grant type, the client is not able to store the client_secret. We can’t expect that it will be able to store the refresh token, which is highly confidential. Therefore, this flow doesn’t support refresh token grant flow.

Client credentials grant type - In this grant type there is no user, so the need for refresh token doesn’t arise. The client can just send its client id and client secret to get the access token.

