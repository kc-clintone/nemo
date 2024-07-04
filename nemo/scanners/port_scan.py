#!/usr/bin/python3
"""
Posrt scanning
"""

import nmap
import subprocess
import xml.etree.ElementTree as ET


def port_scan(ip, port_range):
    """
    Port scanning function
    """
    try:
        # Call nmap with sudo
        nmap_output = subprocess.check_output(
            ['sudo', 'nmap', '-sV', '-oX', '-', f'{ip}', f'-p{port_range[0]}-{port_range[-1]}'],
            universal_newlines=True
        )
        dom = ET.fromstring(nmap_output)
        open_ports = []
        for port in dom.findall('.//port'):
            if port.find('state').get('state') == 'open':
                service = port.find('service')
                open_ports.append({
                    'port': port.get('portid'),
                    'service': service.get('name'),
                    'version': service.get('version', 'unknown'),
                    'product': service.get('product', 'unknown')
                })
        return open_ports
    except subprocess.CalledProcessError as e:
        print(f"Failed to run nmap: {e}")
        return []
    except ET.ParseError as e:
        print(f"Failed to parse nmap output: {e}")
        return []

