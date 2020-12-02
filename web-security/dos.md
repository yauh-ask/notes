A denial of service or DoS, attack is a type of attack in which the attacker tries to crash an application so that the legitimate users are not able to access the application. The attacker does not gain any benefit from this attack. The main purpose of this attack is to harm an organization, and is often carried out by a competitor or mischievous hacker.

The first DoS attack was done by 13-year old David Dennis in 1974. Dennis wrote a program using the external or ext command that forced some computers at a nearby university research lab to power off.

Types of Denial of Service Attacks #
The denial of service attacks can be categorized into two types:

1. Flood Attack #
In a flood attack, the attacker overwhelms the application with a flood of requests. The application has a limit to the number of requests it can handle per second, and if the number of requests increases exponentially, the server will slow and eventually crash.

There are two types of flood attacks:

ICMP flood – In this attack, the attacker leverages misconfigured network devices by sending spoofed packets that ping every computer on the targeted network, instead of just one specific machine. The network is then triggered to amplify the traffic. This attack is also known as the “smurf attack” or the “ping of death”.

A SYN flood – In this attack, the targeted server receives a request to begin the handshake, but the handshake is never completed. That leaves the connected port occupied and unavailable to process further requests. The attacker continues to send more and more requests, overwhelming all open ports and shutting down the server.

2. Crash Attack #
This attack is not very common. In this attack, the attacker transmits a bug to the server which then takes advantage of the vulnerabilities of the server.

Distributed denial of service. #
In a distributed DoS attack, multiple systems orchestrate a synchronized DoS attack to a single target. With this method, the target is attacked from many locations at once instead of being attacked from a single location.

The distributed DoS attack is hard to stop because of the following reasons:

The attack can be done by systems throughout the world, so it becomes difficult to find the location of the attack.
It is difficult to counter-attack multiple machines.
Steps to stop DoS attack #
1. Black Hole Routing #
If an application owner sees that the application is experiencing an unprecedented load of traffic, then all of the traffic can be routed to a black hole route. In this defense mechanism, the legitimate and illegitimate requests are sent to a black hole, so the application goes down regardless. The benefit is that it gives some time to application owners to look into the origin of the attack and take appropriate action.

2. Rate Limiting #
Limiting the number of requests a server will accept during a certain window of time is also a way of mitigating denial-of-service attacks. Although this may lead to some valid requests being denied, the benefit of this method is that the system will not be overwhelmed.
