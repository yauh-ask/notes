#!/usr/bin/env python

# use pip to install scapy, eg `pip install --pre scapy[basic]`

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Target IP / IP range.")
    options = parser.parse_args()
    return options

# 1. Create arp request directed to broadcast MAC asking for IP:


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)   # Use ARP to ask who has target IP
    # Set destination MAC to broadcast MAC
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # print(arp_request.summary())

    # scapy.ls(scapy.ARP) to list the names of the fields
    # scapy.ls(scapy.Ether) to list dst, src, type

    arp_request_broadcast = broadcast/arp_request

      # arp_request_broadcast.show()

    # 2. Send packet and receive response.
     # 3. Parse the response + print the result.
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]

   clients_list = []
   for el in answered_list:
       client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc}
       clients_list.append(client_dict)
       # print(el[1].show()) to see the response in [1] and decode it via .show()
       # print(el[1].psrc + "\t\t" + el[1].hwsrc) - IP of the device
       # print(el[1].hwsrc) # hardware source or MAC
   

      return clients_list

def print_result(results_list):
     print("IP\t\t\tMAC_Address\n----------------")
     for client in results_list:
         print(client["ip"] + "\t\t" + client["mac"])




options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
