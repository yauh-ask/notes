#!/usr/bin/env python

import scapy.all as scapy

# 1. Create arp request directed to broadcast MAC asking for IP:
# - Use ARP to ask who has target IP
# - Set destination MAC to broadcast MAC


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # 2. Send packet and receive response.
     # 3. Parse result.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
   for el in answered_list:
       # print(el[1].show()) # to see the response in [1] and decode it via .show()
       print(el[1].psrc) # source or IP of the device
       print(el[1].hwsrc) # hardware source or MAC
       print("-------------------") # to split

    # arp_request_broadcast.show()

    # print(arp_request.summary())

    # scapy.ls(scapy.ARP) to list the names of the fields
    # scapy.ls(scapy.Ether) to list dst, src, type


scan("10.0.2.1/24")
