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


def log_creation(logger):
    """Test to validate logging is writing properly to a log."""
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    app_log_file = str(os.getenv("APP_LOG_FILE"))
    log = logger
    assert os.path.exists('../app.log')
    log.info("assert os.path.exists(" + app_log_file + "): true")


def log_insert(logger):
    """Test to validate logging is writing properly to a log."""
    log = logger
    log.info("Insert test message")


# Another quick test of the log functionality as a baseline - has handlers.
def log_handlers(logger):
    """Test to validate the log handlers are being created."""
    log = logger
    assert log.hasHandlers()
    if log.hasHandlers():
        log.info("Logger has handlers.")


def test_app_logging():
    """Function to execute other tests."""
    logger = create_logger()
    log_creation(logger)
    log_insert(logger)
    log_handlers(logger)


def test_log_insert(caplog):
    """This is a pytest to validate logging is writing properly to a log."""
    log = create_logger()
    log_test_uuid = str(uuid4())
    log.info(f"Adding uuid to log for testing {log_test_uuid}")
    for record in caplog.records:
        log.info(caplog.text)
        assert record.levelname != "CRITICAL"
        assert log_test_uuid in caplog.records
    if log_test_uuid in caplog.text:
        log.info("Found uuid %s in log", log_test_uuid)
