#!/usr/bin/python3
"""
Advanced scan
"""

import nmap


def advanced_scan(ip):
    """
    Advanced port scan function
    """
    nm = nmap.PortScanner()
    scan_result = nm.scan(ip, arguments='-O -sV')
    result = {
        'hostname': scan_result['scan'][ip].get('hostnames', [{}])[0].get('name', 'unknown'),
        'os': scan_result['scan'][ip].get('osmatch', [{}])[0].get('name', 'unknown'),
        'open_ports': []
    }

    if 'tcp' in scan_result['scan'][ip]:
        for port in scan_result['scan'][ip]['tcp']:
            port_info = scan_result['scan'][ip]['tcp'][port]
            result['open_ports'].append({
                'port': port,
                'service': port_info['name'],
                'version': port_info.get('version', 'unknown'),
                'product': port_info.get('product', 'unknown')
            })
    return result

