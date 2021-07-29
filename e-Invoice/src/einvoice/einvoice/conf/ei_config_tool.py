#!/usr/bin/env python3
#
# File: ei_config_tool.py
# About: e-Invoice configuration management tool.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-17 (July 17th, 2021)
#
# LICENSE
# Copyright (C) 2021 Business Payments Coalition
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
# from .. import ei_logging
from .. ei_logging import create_logger

# # Note that the values for logging configuration are included
# # in the dictionary so a default logging config will be loaded
# # until it can be updated in the runtime.

# @dataclass
# class CIItem:
#     """This is a dataclass which defines a configuration item.

#     A dictionary of the package's configuraiton objects grouped by module
#     and defined by a key:value pair of objects.
#         Args:

#         Attributes:
#             ci_module_name: str
#                 Use the module's filesfdffname.
#             ci_param: str
#                 The name key of a key:value pair.
#             ci_value: str
#                 The actual value represented by the key in the key


#         Raises:

#         Retuns:

#     """
#     ci_module_name: str
#     ci_param: str
#     ci_value: str

# @dataclass
# class Configuration::

#     ci_dict = {}
#     configuration = ()

#     def add_ci_item(_ci_dict, _module_name, _param,
#     _value):
#         _ci_dict = {_module_name, _para, _value}
#         _configuration = _configuration.append(_ci_dict)
#         return _configuration

# def read_from_file(fn='ei_config_active.json'):
#     _config = {}
#     # this_is_a_TODO put the code read in actual file.
#     return _config

# def write_to_file(fn='ei_config_active.json'):
#     happy = ''
#     # this_is_a_TODO put the code to write to file.
#     return happy

# class EIConfigTool:

#     def __init__(self, _fn=''):
#         self.configuration = read_from_file(_fn)


logger = create_logger("ei_config_tool")


def write_json_to_file(_data, _fn):
    """Writes the e-Inovice to a JSON file."""
    json_str = dumps(_data.__dict__)

    try:
        with open(_fn, "w") as output:
            output.write(json_str)
    except ValueError as err:
        print("Error writing to file", err)


class EIConfig:
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

    # defaults = {}
    # Check so see if config file already exists.

    @classmethod
    def load_defaults(cls, _defaults, _filename):
        """A classmethod to define library of default values.

        Args:

        Attributes:
            def_log_level: str
                Default logging level
            def_prty_id_spec: str
                Default party id specification
            def_ptry_schma_type: str
                Default party id schema type
            def_prty_id: str
                Default party id
        Raises:

        Returns:
            _defaults: obj
            Dictionary {} object containing default values.
        """
        _defaults["def_log_level"] = "INFO"
        _defaults["def_prty_id_spec"] = \
            "urn:oasis:names:tc:ebcore:partyid-type"
        _defaults["def_prty_schma_typ"] = "iso6523"
        _defaults["def_prty_id"] = "0123456789"
        print(_defaults)
        write_json_to_file(_defaults, _filename)
        return _defaults

    # def check_file_exists(self, _defaults, _fn):
    #     """Check to see if the defult config exists and if not create it."""
    #     if os.path.exists(_fn):
    #         self.load_defaults(_defaults, _fn)

    def __init__(self):
        self.defaults = {}
        self.f_n = "./ei_config.json"
        if not os.path.exists(self.f_n):
            self.ei_config = self.load_defaults(self.defaults, self.f_n)
        #  return self.ei_config
