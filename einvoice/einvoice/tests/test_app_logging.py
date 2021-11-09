#!/usr/bin/env python3
#
# File: test_app_logger.py
# About: e-Invoice testing suite; app_logger.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest.

"""
from einvoice.app_logging import create_logger


# Test the logging functionality using built-in Pytest "caplog"
def test_log_insert():
    """This is a pytest to validate loggig is writing properly to a log."""
    log1 = create_logger("test_app_logging")
    message = ("Insert test message")
    log1.info(message)
