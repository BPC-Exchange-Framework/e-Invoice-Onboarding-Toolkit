#!/usr/bin/env python3
# pylint: disable=W1203
# Lazy % loading.
# # File: import_xsd.py
# About: Import an XSD file.
# Development: Kelly Kinney
# # Date: 2022-01-19 (January 19th, 2022)
#
"""Import an XSD file for use by a calling application.

Return a string version of XSD pulled off the web.

"""
import xmlschema

LOGGER = __name__

class ImportXSD:
    """Import an XSD file from the Internet."""

    def __init__(self):
        """Define and instantiate variables."""
        self.filename = ""
        self.schema_xsd = None
        self.schema = {}
        self.request = ""

    def get_xsd_from_file(self, filename, log):
        """Import the specified XSD file."""
        self.schema_xsd = xmlschema.XMLSchema(filename)
        log.info(f'Loading schema from file {filename}')
        log.info(self.schema_xsd)
        return self.schema

    def get_xsd_from_internet(self, uri, log):
        """Import the xsd from an URI."""
        self.schema_xsd = xmlschema.XMLSchema(uri)
        log.info(f'Loading schema from uri {uri}')
        log.info(self.schema_xsd)
        return self.schema_xsd
