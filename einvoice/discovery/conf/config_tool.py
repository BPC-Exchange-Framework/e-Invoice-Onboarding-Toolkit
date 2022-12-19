#!/usr/bin/env python3
# pylint: disable=W1514, E1120
# False positive on requiring explicit encoding, method could be a function
# known bug with E1120 false positive
# File: config_tool.py
# About: Create default einvoice values in correct format
# if none are known.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-17 (July 17th, 2021)
#
"""The classes and functions which support programmatic configuration updates.

The configuration values are stored in a dictionary written to a JSON file.
The values are read on demand by other package and module files as necessary.
This allows for the programmatic maintenance of the file.

Args: str
ei_conf_fn: the file name containing the values to load.
This is filename can be dynamically saved to support multiple versions.

Attributes:
None

Raises:
None

Returns:
None

"""
import os.path
from json import dumps

LOGGER = __name__


class EInvoiceConfig:
    """Configure default settings for E-Invoice.

    This class creates some baseline configurations for E-Invoice handling.py

    Attributes:
    defaults: obj
    This is a dictionary {} object to hold config key/value pairs
    f_n: str
    filename which represents both output path and filename

    Raises:
    NA

    Return:
    NA
    """

    def __init__(self):
        """Define values made available across the application."""
        self.filename = "./einvoice.json"
        self.json_str = ""
        # Check to see if a default file exists and if not
        # create one.
        if not os.path.exists(self.filename):
            self.load_defaults(self.filename)

    def write_json_to_file(self, einvoice_data, filename, log):
        """Write the E-Invoice to a JSON file."""
        json_str = dumps(einvoice_data.__dict__)
        log.info(json_str)

        try:
            with open(filename, "w") as output:
                output.write(json_str)
        except ValueError as err:
            print("Error writing to file", err)

    @classmethod
    def load_defaults(cls, log, filename="./einvoice.json"):
        """Initialize library of default values.

        Args:

        Attributes:
        default_log_level: str
        Default logging level
        default_party_id_spec: str
        Default party id specification
        default_party_schema_type: str
        Default party id schema type
        default_party_id: str
        Default party id

        Raises:
        NA

        Returns:
        defaults: obj
        Dictionary {} object containing default values.

        """
        cls.defaults = {}
        cls.filename = filename

        cls.defaults["default_log_level"] = "info"
        cls.defaults["default_party_id_spec"] = \
            "urn:oasis:names:tc:ebcore:partyid-"\
            "type:unregistered:myscheme"
        cls.defaults["def_party_schema_typ"] = "BPC01"
        cls.defaults["default_party_id"] = "bpcBusid01"
        cls.write_json_to_file(cls, cls.defaults, cls.filename, log)
        return cls.defaults