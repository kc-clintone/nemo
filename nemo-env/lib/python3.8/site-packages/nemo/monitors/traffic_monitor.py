#!/usr/bin/python3
"""
Network traffic monitoring tool
"""

import psutil
import time


def monitor_traffic(interval=1):
    """
    Monitoring module
    """
    old_value = psutil.net_io_counters()
    while True:
        new_value = psutil.net_io_counters()
        sent = new_value.bytes_sent - old_value.bytes_sent
        recv = new_value.bytes_recv - old_value.bytes_recv
        print(f"Bytes Sent: {sent} Bytes Received: {recv}")
        old_value = new_value
        time.sleep(interval)

