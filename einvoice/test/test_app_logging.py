#!/usr/bin/env python3
# pylint: disable=W1203
# Not using lazy % formatting
# File: test_app_logger.py
# About: E-Invoice testing suite; app_logger.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest.

Args:
NA

Attributes:
NA

Raises:
NA

Returns:
NA
"""
from uuid import uuid4
import os
from os.path import join, dirname
from dotenv import load_dotenv
from einvoice.discovery.app_logging import create_logger


# Test the logging functionality using built-in Pytest "caplog"
def test_log_creation():
    """This is a pytest to validate loggig is writing properly to a log."""
    dotenv_path = join(dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)
    app_log_file = str(os.getenv("APP_LOG_FILE"))
    web_response_file = str(os.getenv("WEB_RESPONSE_FILE"))
    log1 = create_logger("test_log_creation")
    log1.info("Insert test message")
    assert os.path.exists(app_log_file)
    assert os.path.exists(web_response_file)


# Test the logging functionality using built-in Pytest "caplog"
def test_log_insert_1():
    """This is a pytest to validate loggig is writing properly to a log."""
    log2 = create_logger("test_app_logging")
    log2.info("Insert test message")


# Test the logging functionality using built-in Pytest "caplog"
def test_log_insert_2(caplog):
    """This is a pytest to validate loggig is writing properly to a log."""
    log3 = create_logger("test_log_insert_2")
    log_test_uuid = str(uuid4())
    log3.info(f"Adding uuid to log for testing {log_test_uuid}")
    for record in caplog.records:
        assert record.levelname != "CRITITAL"
    assert log_test_uuid in caplog.text
    if log_test_uuid in caplog.text:
        log3.info("Found uuid %s in log", log_test_uuid)


# Another quick test of the log functionality as a baseline - has handlers.
def test_log_handlers():
    """This is a pytest to validate the log handlers are being created."""
    log4 = create_logger("test_log_handler")
    assert log4.hasHandlers()
    if log4.hasHandlers():
        log4.info("Logger has handlers.")
