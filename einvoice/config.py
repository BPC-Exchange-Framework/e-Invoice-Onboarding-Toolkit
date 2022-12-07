#!/usr/bin/env python3
#
# File: config.py
# About: Project level configuration file per
# 'https://docs.python.org/3/faq/programming.html
# #how-do-i-share-global-variables-across-modules'
# Development: Kelly Kinney
# Date: 2022-12-03 (December 3rd, 2022)
#
"""Configuration file with global values and single logging instance."""
from einvoice.discovery.app_logging import create_logger

LOGGER = __name__


class Logger():
    """Define and instantiate a logging object for the entire package."""

    def __init__(self):
        """Entry point to the application and define application variables."""
        self.log = None

    def create_logger(self):
        """Create an instance of a logger for the entire application.."""
        self.log = create_logger(LOGGER)
        self.log.info("Called log file instance in config.")
        return self.log


def get_logger(self):
    """Return the currently instantiated log."""
    return self.log
