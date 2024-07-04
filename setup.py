#!/usr/bin/python3
"""
This is a setup file for the netmon project
"""

from setuptools import setup, find_packages

setup(
    name='nemo',
    version='1.0.0',
    description='Advanced Network Scanning and Monitoring tool',
    author='kc-clintone',
    author_email='kayseeclintone@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'scapy',
        'python-nmap',
        'psutil',
        'termcolor',
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'nemo=nemo.cli:main',
        ],
    },
)

