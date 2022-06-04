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
from einvoice.discovery.app_logging import create_logger


class ImportXSD:
    """Import an XSD file from a uri or local file."""

    def __init__(self):
        """Define and instantiate variables."""
        self.filename = ""
        self.log = create_logger("import_xsd")
        self.schema_xsd = None
        self.schema = {}
        self.request = ""

    def get_xsd_from_file(self, filename):
        """Import the specified XSD file."""
        self.schema_xsd = xmlschema.XMLSchema(filename)
        self.log.info(f"Loading schema from file {filename}")
        self.log.info(self.schema_xsd)
        # self.log.info("Begin enumeration of schema elements.")
        # for component in self.schema_xsd.iter_components():
        #     self.log.info(f'{component}')
        # self.log.info("Finished enumeration of schema elements.")
        return self.schema

    def get_xsd_from_internet(self, uri):
        """Import the xsd from an URI."""
        self.schema_xsd = xmlschema.XMLSchema(uri)
        self.log.info(f"Loading schema from uri {uri}")
        self.log.info(self.schema_xsd)
        # self.log.info("Begin enumeration of schema elements.")
        # for component in self.schema_xsd.iter_components():
        #     self.log.info(f'{component}')
        # self.log.info("Finished enumeration of schema elements.")
        return self.schema_xsd
