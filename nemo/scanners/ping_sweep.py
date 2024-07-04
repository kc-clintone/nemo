#!/usr/bin/python3
"""
Ping sweep module
"""

from scapy.all import ARP, Ether, srp

def ping_sweep(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    hosts = {}
    for sent, received in answered_list:
        hosts[received.psrc] = received.hwsrc  # IP address to MAC address

    return hosts

