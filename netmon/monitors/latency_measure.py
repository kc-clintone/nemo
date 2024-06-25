#!/usr/bin/python3
"""
Latency measure module
"""

import subprocess
from termcolor import colored

def measure_latency(host):
    """
    Measure the latency to a given host using the ping command.

    Parameters:
    host (str): The hostname or IP address to ping.

    Returns:
    float: The average latency in milliseconds.
    """
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
        for line in output.splitlines():
            if 'avg' in line:
                avg_latency = line.split('/')[4]
                latency = float(avg_latency)
                print(colored(f"Average latency to {host}: {latency} ms", 'green'))
                return latency
    except subprocess.CalledProcessError as e:
        print(colored(f"Error measuring latency to {host}: {e}", 'red'))
        return None

# Example usage:
# if __name__ == "__main__":
#     measure_latency('google.com')
