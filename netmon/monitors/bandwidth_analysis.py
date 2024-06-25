#!/usr/bin/python3
"""
Bandwidth scan module
"""

import psutil
import time
from termcolor import colored

def get_network_io():
    """
    Get the current network I/O stats.
    """
    io_counters = psutil.net_io_counters(pernic=True)
    return {iface: {'bytes_sent': stats.bytes_sent, 'bytes_recv': stats.bytes_recv}
            for iface, stats in io_counters.items()}

def bandwidth_analysis(interface, duration=1):
    """
    Calculate the bandwidth usage for a given network interface over a specified duration.
    Parameters:
    interface (str): The network interface to monitor (e.g., 'eth0').
    duration (int): The duration over which to measure bandwidth usage (in seconds).

    Returns:
    dict: A dictionary containing bytes sent and received.
    """

    start_stats = get_network_io()
    time.sleep(duration)
    end_stats = get_network_io()

    if interface not in start_stats or interface not in end_stats:
        print(colored(f"Interface {interface} not found.", 'red'))
        return None

    bytes_sent = end_stats[interface]['bytes_sent'] - start_stats[interface]['bytes_sent']
    bytes_recv = end_stats[interface]['bytes_recv'] - start_stats[interface]['bytes_recv']

    usage_stats = {
        'interface': interface,
        'bytes_sent': bytes_sent,
        'bytes_recv': bytes_recv,
        'duration': duration
    }

    print(colored(f"Interface {interface} usage over {duration} second(s):", 'green'))
    print(colored(f"Bytes Sent: {bytes_sent}", 'green'))
    print(colored(f"Bytes Received: {bytes_recv}", 'green'))

    return usage_stats

# Example usage:
# if __name__ == "__main__":
#     calculate_bandwidth_usage('eth0')
