#!/usr/bin/env python3
#
# File: cert_logging.py
# About: Logging provider
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
"""
A class to standardize log formatting across all application artifacts.

Define common loggers and format to be used across the application.

    Usage: (not meant to be called directly)
    log = create_logger("app_logging")
    log.info("This message will be logged.")

"""
import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv


def create_logger(name):
    """This function creates a logger template for all packages.

    This function creates a consistant format and location for
    all application log files to write to.
    """

    dotenv_path = join(dirname(__file__), './.env')
    load_dotenv(dotenv_path)
    log_file_out = str(os.getenv("LOG_FILE"))
    # if !isinstance(type(log_file_out), str):
    print(f'Location of log file: {log_file_out}')

    # print("Create logger with name %s" % name)
    logger = logging.getLogger(name)

    # It's okay to run INFO in Dev.  Turn it down to DEBUG for QA
    # and WARN for Prod unless troubleshooting an issue.
    logger.setLevel(logging.INFO)

    # create file handler which writes to a file.
    file_logger = logging.FileHandler(log_file_out)
    file_logger.setLevel(logging.INFO)

    # create console handler with a higher log level
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)

    # Create a custom formatter and add it to the handlers
    _format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"
    formatter = logging.Formatter(_format, datefmt)

    file_logger.setFormatter(formatter)
    console_logger.setFormatter(formatter)

    # Associate the the handlers to the loggers
    logger.addHandler(file_logger)
    logger.addHandler(console_logger)

    return logger
