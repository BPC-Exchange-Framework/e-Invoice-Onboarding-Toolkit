#!/usr/bin/env python3
#
# File: config_tool.py
# About: e-Invoice configuration management tool.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-17 (July 17th, 2021)
#
"""The classes and functions which support programatic configuration updates.

The configuration values are stored in a dictionary written to a JSON file.
The values are read on demand by other package and module files as necessary.
This allows for the programtic maintenance of the file.

    Args: str
        ei_conf_fn: the file name containing the values to load.
        This is filename can be dynamiclaly saved to support multiple versions.

    Attributes:

    Raises:

    Returns:

"""
import os.path
from json import dumps
from .. app_logging import create_logger


class EInvoiceConfig:
    """Configure default settings for e-Invoice

    This class creates some baseline configurations for e-Invoice handling.py

    Args:

    Attributes:
        defaults: obj
            This is a dictionary {} object to hold config key/value pairs
        f_n: str
            filename which represents both output path and filename

    Raises:

    Returns:
    """

    def write_json_to_file(_data, _fn):
        """Writes the e-Inovice to a JSON file."""
        json_str = dumps(_data.__dict__)

        try:
            with open(_fn, "w") as output:
                output.write(json_str)
        except ValueError as err:
            print("Error writing to file", err)

    def __init__(self):
        self.defaults = {}
        self.config_logger = create_logger("config_tool")
        self.f_n = "./config_tool.json"
        if not os.path.exists(self.f_n):
            self.config_tool = self.load_defaults(self.defaults, self.f_n)

    def load_defaults(cls, _defaults, _filename):
        """A classmethod to define library of default values.

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

        Returns:
            _defaults: obj
            Dictionary {} object containing default values.
        """
        _defaults["default_log_level"] = "INFO"
        _defaults["default_party_id_spec"] = \
            "urn:oasis:names:tc:ebcore:partyid-type"
        _defaults["def_prty_schma_typ"] = "iso6523"
        _defaults["default_party_id"] = "0123456789"
        config_logger.debug(_defaults)
        write_json_to_file(_defaults, _filename)
        return _defaults
