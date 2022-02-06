#!/usr/bin/env python3
# pylint: disable=W1203
# lazy % formatting
# File: test_import_xsd.py
# About: e-Invoice testing suite; import xsd.
# Development: Kelly Kinney
# Date: 2022-01-19 (January 19th, 2022)
"""Run tests for import_xsd.py.

    Execute tests for importing from a file and pulling XSD off the
    internet.
"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from einvoice.discovery.app_logging import create_logger
from einvoice.delivery.import_xsd import ImportXSD


dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

def test_import_xsd_from_file():
    """Test the import_xsd module fetching from file"""
    log1 = create_logger("test_import_xsd_from_file")
    filename = "ebms-header-3_0-20220119.xsd"
    log1.info(f'Filename to load: {filename}')
    importer = ImportXSD()
    schema = importer.get_xsd_from_file(filename)
    # log1.info(len(schema))
    log1.info(schema)
    log1.info(type(schema))
    log1.info(f'Schema attributes: {dir(schema)}')
    # for items in enumerate(schema):
    #     log1.info(f'index: {schema.__getitem__}')


def test_import_xsd_from_uri():
    """Test the import_xsd module fetching from internet"""
    log2 = create_logger("test_import_xsd_from_uri")
    uri = os.getenv("EBMS_XSD_URL")
    log2.info(f'File to load from internet: {uri}')
    importer = ImportXSD()
    schema = importer.get_xsd_from_internet(uri)
    # log2.info(len(schema))
    log2.info(schema)
    log2.info(type(schema))
    log2.info(dir(schema))
    assert schema.is_valid
