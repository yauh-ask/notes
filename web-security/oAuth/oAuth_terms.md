Resource owner #
The resource owner is the owner of the resource that is being accessed. When you log in to PicsArt App using your Facebook account, you are granting access to PicsArt to access your images. In this case, you are the resource owner.

Client #
The client is an application that accesses protected resources on behalf of the resource owner. The client could be hosted on a server, desktop, mobile, or other devices. In our example, the PicsArt app is the client.

Resource server #
The server that is hosting the protected resources and is capable of accepting and responding to requests by clients using access tokens. In our example, Facebook is the resource server.

Authorization server #
The server which issues access tokens after successfully authenticating a client and resource owner is called authorization server. In our example, the Facebook server was issuing the access token. Normally, there is a separate server that does this task.

Authorization grant #
An authorization grant is a credential representing the resource owner’s authorization (to access its protected resources) used by the client to obtain an access token. The OAuth specification defines four grant types, which we will discuss in the upcoming lessons.

Authorization code #
In our example, we showed that the Facebook App shared a token with the client. In some OAuth flows, the authorization server does not give the access token directly. It first issues an authorization grant. The client then sends this grant with the client secret (more on this later) to the authorization server. After this, the authorization server gives access token to the client.

Access token #
Access tokens are credentials used to access protected resources. An access token is a string representing an authorization issued to the client. Tokens represent specific scopes and durations of access, granted by the resource owner, and enforced by the resource server and authorization server.

Scope #
Scope defines the permissions of a token. It defines what resources can be accessed using a given access token. In our example, the client app wants to access only images, so the images are scope.
