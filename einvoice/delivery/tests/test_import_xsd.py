# test_import_xsd.py

import os
from os.path import join, dirname
from dotenv import load_dotenv
import xmlschema
from einvoice.discovery.app_logging import create_logger
from delivery.import_xsd import get_xsd_from_file, get_xsd_from_internet
from delivery.import_xsd import ImportXSD
"""Test module for import_xsd.py."""

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)


def test_import_xsd_from_file():
    """Test the import_xsd module fetching from file"""
    log1 = create_logger("test_import_xsd_from_file")
    filename = os.getenv("EBMS_XML_FILE")
    importer = ImportXSD()
    schema = xmlschema.XMLSchema(importer.get_xsd_from_file(filename))
    log1.info(schema)


def test_import_xsd_from_uri():
    """Test the import_xsd module fetching from internet"""
    log2 = create_logger("test_import_xsd_from_uri")
    uri = os.getenv("EBMS_XML_URL")
    importer = ImportXSD()
    schema = xmlschema.XMLSchema(importer.get_xsd_from_internet(uri))
    log2.info(schema)
