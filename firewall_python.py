# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:56:10 2024

@author: karth
"""

from scapy.all import sniff

# Define filtering rules
rules = {
    "allow_ips": ["192.168.1.5"],
    "block_ips": ["192.168.1.10"],
    "allow_ports": [22, 80],
    "block_ports": [23]
}

def packet_filter(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]

        # Block packets from blocked IP addresses
        if ip_layer.src in rules["block_ips"]:
            print(f"Blocked packet from {ip_layer.src}")
            return False

        # Allow packets from allowed IP addresses
        if ip_layer.src in rules["allow_ips"]:
            print(f"Allowed packet from {ip_layer.src}")
            return True

        # Block packets with blocked destination ports
        if packet.haslayer("TCP") and packet["TCP"].dport in rules["block_ports"]:
            print(f"Blocked packet on port {packet['TCP'].dport}")
            return False

        # Allow packets with allowed destination ports
        if packet.haslayer("TCP") and packet["TCP"].dport in rules["allow_ports"]:
            print(f"Allowed packet on port {packet['TCP'].dport}")
            return True
        
     # Default action: allow the packet and log that it was allowed by default
    print(f"Allowed packet from {ip_layer.src} (default rule)")
    return True  # Default to allowing packet if no rules match

# Capture and filter network packets
sniff(prn=packet_filter, store=0)
