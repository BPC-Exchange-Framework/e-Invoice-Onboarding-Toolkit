#!/usr/bin/env python3
# pylint: disable=W1203
# lazy % formatting
# File: test_import_xsd.py
# About: E-Invoice testing suite; import xsd.
# Development: Kelly Kinney
# Date: 2022-01-19 (January 19th, 2022)
"""Run tests for import_xsd.py."""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from einvoice.delivery.import_xsd import ImportXSD
from einvoice.config import Logger

LOGGER = __name__

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

test_logger = Logger()
log = test_logger.create_logger()

def test_import_xsd_from_file():
    """Test the import_xsd module fetching from file."""
    filename = "ebms-header-3_0-20220119.xsd"
    log.info(f'Filename to load: {filename}')
    importer = ImportXSD()
    schema = importer.get_xsd_from_file(filename, log)
    log.info(schema)
    log.info(type(schema))
    log.info(f'Schema attributes: {dir(schema)}')


def test_import_xsd_from_uri():
    """Test the import_xsd module fetching from internet."""
    uri = os.getenv("EBMS_XSD_URL")
    log.info(f'File to load from internet: {uri}')
    importer = ImportXSD()
    schema = importer.get_xsd_from_internet(uri, log)
    log.info(schema)
    log.info(type(schema))
    log.info(dir(schema))
    assert schema.is_valid
