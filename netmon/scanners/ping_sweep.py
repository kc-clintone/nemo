#!/usr/bin/python3
"""
Ping sweep module
"""

import scapy.all as scapy


def ping_sweep(ip_range):
    """
    Ping sweep function
    """
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    live_hosts = []
    for element in answered_list:
        live_hosts.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    return live_hosts

