ARP - address resolution protocol, helps to connect the client with another client via IP and MAC addresses. ARP links IP address to MAC address.

Client sends a broadcast message with ARP request, e.g. who has 10.0.2.6? All clients on this network will receive this packet. All the devices will ignore the request except the one with the requested IP address. The requested device will get back with its MAC address.

So all the requests and responses are facilitated via ARP, so IP address could be 'translated' to MAC address.
