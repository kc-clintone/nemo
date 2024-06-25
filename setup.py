#!/usr/bin/python3
"""
This is a setup file for the netmon project
"""

from setuptools import setup, find_packages


setup(
    name='netmon',
    version='1.0.0',
    description='Advanced Network Scanning and Monitoring CLI Tool',
    author='kc-clintone',
    author_email='kayseeclintone@gmail.com',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'python-nmap',
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'netmon=netmon.cli:main',
        ],
    },
)

