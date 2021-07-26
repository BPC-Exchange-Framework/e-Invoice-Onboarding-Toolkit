#!/usr/bin/env python3
#
# File: ei_logging.py
# About: Logging provider
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
# LICENSE
# Copyright (C) 2021 Business Payments Coalition
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
A class to standardize log formatting across all application artifacts.

Define common loggers and format to be used across the application.
NOTE: These logs are localized and non-persistent.
If used with a Docker container,
they cease to exist when the container does.

    Usage: (not meant to be called directly)
    log = create_logger("ei_logging")
    log.debug("This message will be logged.")

"""
import logging


def create_logger(name):
    """This function creates a logger template for the einvoice package.

    This funtion creates a consistant format and location for
    all application log files to write to.
    """
    print("Create logger with name %s" % name)
    logger = logging.getLogger(name)

    # It's okay to run INFO in Dev.  Turn it down to DEBUG for QA
    # and WARN for Prod unless troubleshooting an issue.
    logger.setLevel(logging.DEBUG)

    # create file handler which writes to a file.
    ei_file_logger = logging.FileHandler("ei_output.log")
    ei_file_logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ei_console_logger = logging.StreamHandler()
    ei_console_logger.setLevel(logging.INFO)

    # Create a custom formatter and add it to the handlers
    _format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"
    formatter = logging.Formatter(_format, datefmt)

    ei_file_logger.setFormatter(formatter)
    ei_console_logger.setFormatter(formatter)

    # Associate the the handlers to the loggers
    logger.addHandler(ei_file_logger)
    logger.addHandler(ei_console_logger)

    return logger


# log = create_logger("ei_logger")
# log.info("ei_logger log instance created")
