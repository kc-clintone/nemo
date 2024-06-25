#!/usr/bin/python3
"""
Report generator module
"""

import json
import csv


def generate_report(data, filename, format='json'):
    """
    Report generator function
    """
    if format == 'json':
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    elif format == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())
