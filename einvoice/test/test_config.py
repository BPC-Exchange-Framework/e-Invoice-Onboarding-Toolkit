#!/usr/bin/env python3
# pylint: disable=W1203
# Not using lazy logging.
# File: test_config.py
# About: E-Invoice testing suite; config file
# Development: Kelly Kinney
# Date: 2022-12-05 (December 5th, 2022)
#
"""This is a test file to be run using pytest."""
from einvoice.config import Logger


def test_config():
    """Pytest case for test_accessor."""
    log = Logger().create_logger()
    log.info("Testing config")
