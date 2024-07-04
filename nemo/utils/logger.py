#!/usr/bin/python3
"""
Logger util
"""

import logging


def setup_logger():
    """
    Logger function
    """
    logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s')
    logging.info('Logger initialized')

