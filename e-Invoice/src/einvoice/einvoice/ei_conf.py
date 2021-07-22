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

The configuration values are stored in a dictionary written to a JSON file.  The values are read on demand by other package and module files as necessary.   This allows for the programtic maintenance of the file.  

    Args: str
        ei_conf_fn: the file name containing the values to load.  This is filename can be dynamiclaly saved to support multiple versions.  

    Attributes:

    Raises:

    Returns:

"""
from json import dumps
import logging

# Note that the values for logging configuration are included
# in the dictionary so a default logging config will be loaded
# until it can be updated in the runtime.
