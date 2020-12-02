What is HTTPS? #
Since the beginning of the Internet, HyperText Transfer Protocol (HTTP) has been used to transfer information between the client and the server. The data is transferred in plain text format through HTTP. This means an attacker can get access to the data that is being transferred over the Internet. In the initial years of the Internet, the data that was transferred was mostly static HTML pages and did not raise any security concerns. As the Internet became more widely used for sensitive tasks like banking, more people felt the need for a secure way to transfer their data.

In 1994, Netscape Communications enhanced HTTP with some encryption. They introduced a new encryption protocol named Secure Socket Layer (SSL) and added it on top of HTTP. This combination of HTTP and SSL is called HTTPS (HTTP Secure).

In 1999, Transport Layer Security (TLS) protocol was introduced. This was more efficient than the SSL protocol, so SSL is no longer used.

Benefits of using HTTPS over HTTP #
There are few benefits of using HTTPS instead of HTTP:

1. Authenticity #
HTTPS ensures that the client is talking to the intended website. It is not possible for an attacker to respond to the client’s requests. In HTTPS, the website provides its identity to the client.

2. Confidentiality #
HTTPS ensures that the data that is being transferred between the client and server is secure and an attacker cannot read it. This is achieved by encrypting the data in HTTPS.

3. Message Integrity #
HTTPS ensures that the data is not modified by an attacker while it is being transferred over the Internet. It gives the client and server a way to verify that the data has not been tampered with.

How does HTTPS work? #
In HTTPS, before transferring any data, the client first verifies that the server it is talking to is the correct server and how the data will be encrypted. This process is called the TLS handshake.

TLS handshakes are a series of datagrams, or messages, exchanged by a client and a server. A TLS handshake involves multiple steps, as the client and server exchange the information necessary for completing the handshake and making further conversation possible.

The exact steps within a TLS handshake will vary depending upon the kind of key exchange algorithm used and the cipher suites supported by both sides.

Now, we will look at each step of the TLS Handshake with TLS 1.2 and the RSA algorithm.

Step 1 -> The ‘client hello’ message #
The client initiates the handshake by sending a “hello” message to the server. The message will include:

The TLS version the client supports.
The cipher suites supported.
A string of random bytes known as the client random.
A cipher suite is a set of encryption algorithms that are supported by the client. The client and server need to agree upon which cipher suite will be used for each handshake.

Step 2 -> The ‘server hello’ message #
If the capabilities of the client and server match, then it replies to the client with the following information:

The cipher suite it has selected for communication.
An SSL Certificate.
A randomly selected prime number is called a server random.
Step 3 -> Certificate Validation #
The client verifies that the SSL certificate provided by the server is valid. The client verifies the following properties of the certificate:

The certificate’s digital signature.
The certificate has not expired or revoked.
The certificate contains the correct domain name.
The client browser has a trust store where it stores certificates from some of the most popular Certificate Authorities.

Step 4 -> Pre-master secret #
The client generates a random string of bytes called a pre-master secret. The client encrypts it with the server’s public key and transmits it to the server. The client gets the server’s public key from the SSL certificate.

The client encrypts the pre-master secret with the server’s public key. This can be decrypted with only a private key which is present with the server.

Step 5 -> Session Key creation #
Now both the client and the server calculate the session key using the client random, server random, and the pre-master secret. They both will obtain the same session key.

Step 6 -> Client Finished #
The client sends a finished message encrypted by the session key.

Step 7 -> Server Finished #
The server sends the finished message encrypted by the session key.

Step 8 -> Symmetric encryption successful #
Now the client and the server will encrypt their messages with the same session key. Secure communication is achieved.

Let’s suppose an attacker is listening to all the messages while a connection is being established. The attacker can get client random and server random, but it cannot get the pre-master secret. This is because the pre-master secret is encrypted using the server’s public key. Only the server can decrypt it, using its private key. So, the attacker will not be able to calculate the session key.

