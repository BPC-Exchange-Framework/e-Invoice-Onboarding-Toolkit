#!/usr/bin/env python3
#
# File: app_logging.py
# About: Logging provider
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
"""
A class to standardize log formatting across all application artifacts.

Define common loggers and format to be used across the application.
NOTE: These logs are localized and non-persistent.
If used with a Docker container,
they cease to exist when the container does.

    Usage: (not meant to be called directly)
    log = create_logger("app_logging")
    log.debug("This message will be logged.")

"""
import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv


def create_logger(name):
    """This function creates a logger template for the einvoice package.

    This function creates a consistant format and location for
    all application log files to write to.
    """
    dotenv_path = join(dirname(__file__), './.env')
    load_dotenv(dotenv_path)
    einvoice_log_file = str(os.getenv("EINVOICE_LOG_FILE"))
    web_response_file = str(os.getenv("WEB_RESPONSE_FILE"))

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create file handler which writes to an application log view.
    file_logger = logging.FileHandler(einvoice_log_file)
    file_logger.setLevel(logging.INFO)

    # create console handler which writes to the console
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)

    # create a logger to handle responses
    response_logger = logging.FileHandler(web_response_file)
    response_logger.setLevel(logging.INFO)

    # Create a custom formatter and add it to the handlers
    _format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"
    formatter = logging.Formatter(_format, datefmt)

    file_logger.setFormatter(formatter)
    console_logger.setFormatter(formatter)

    # Create a custom formatter for the response_logger
    response_format = "%(asctime)s - %(message)s"
    response_datefmt = "%Y%m%d:%H:%M:%S"
    response_formatter = logging.Formatter(response_format,
                                           response_datefmt)

    response_logger.setFormatter(response_formatter)

    # Associate the the handlers to the loggers
    logger.addHandler(file_logger)
    logger.addHandler(console_logger)
    logger.addHandler(response_logger)

    return logger
