#!/usr/bin/env python3
# pylint: disable=
#
# # File: import_xsd.py
# About: Import an XSD file.
# Development: Kelly Kinney
# # Date: 2022-01-19 (January 19th, 2022)
#
'''Import an XSD file for use by a calling application.

   Return a string version of XSD pulled off the web.

'''
from requests import get
import xmlschema
from einvoice.discovery.app_logging import create_logger


class ImportXSD:
    """Import an XSD file from the Internet.
    """

    def __init__(self):
        """Define and instantiate variables."""
        self.filename = ""
        self.log = create_logger("import_xsd")
        self.schema = None
        self.request = ""

    def get_xsd_from_file(self, filename):
        """Import the specified XSD file."""
        self.schema = xmlschema.XMLSchema(filename)
        self.log.info(self.schema)
        return self.schema

    def get_xsd_from_internet(self, uri):
        """Import the xsd from an URI"""
        self.request = get(uri)
        self.request = self.request.content.decode('utf-8')
        self.schema = xmlschema.XMLSchema(self.request)
        return self.schema
