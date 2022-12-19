#!/usr/bin/env python3
#
# File: app_logging.py
# About: Logging provider
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
"""Standard log formatting across all application artifacts.

Define common loggers and format used across the application.
These logs are localized and non-persistent.
If used with a Docker container, they cease to exist when the container does.
    Usage: (not meant to be called directly)
    log = create_logger("app_logging")
    log.debug("This message will be logged.")
"""

import logging
import logging.config
import os
from os.path import join, dirname
from dotenv import load_dotenv
import yaml


def create_logger():
    """Implement a logger template.

    This function creates a consistent format and location for
    all application log files to write to.
    """
    dotenv_path = join(dirname(__file__), "../.env")
    load_dotenv(dotenv_path)
    log_config = str(os.getenv("LOG_CONFIG_FILE"))

    with open(log_config, 'r', encoding='utf-8') as file_name:
        config = yaml.safe_load(file_name.read())
        logging.config.dictConfig(config)
        print(config)

    log = logging.getLogger(__name__)

    return log
