#!/usr/bin/env python3
# pylint: disable=R0903,
# File: config.py
# About: Project level configuration file
# Development: Kelly Kinney
# Date: 2022-12-03 (December 3rd, 2022)
#
"""Configuration file with global values and single logging instance."""
from einvoice.discovery.app_logging import create_logger


class Logger():
    """Define and instantiate a logging object for the entire package."""

    def __init__(self):
        """Entry point to the application and define application variables."""
        self.log = None

    def create_logger(self):
        """Create an instance of a logger for the entire application.."""
        self.log = create_logger()
        self.log.info("Called log file instance in config.")
        return self.log

def get_logger(self):
    """Return the currently instantiated log."""
    return self.log
