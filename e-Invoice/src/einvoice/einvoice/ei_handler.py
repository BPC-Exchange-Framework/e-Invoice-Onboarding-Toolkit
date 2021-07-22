#!/usr/bin/env python3
#
# File: ei_handler.py
# About: Responsible for discovery compontents of 4-corners model.  
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
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
"""This classes and functions responsoble for the most crucial components of particpant
discovery.

The module handles retaining the inovice while parallel work is done to 
do a UNAPTR DNS look-up to obtain the SMP URI.  Then to do makes the REST API
call to the SMP endpoint.  

    Args:

    Attributes:

    Raises:

    Returns:

"""

def load_defaults(_defaults):
        _defaults['def_log_level'] = 'INFO'
        _defaults['def_prty_id_spec'] = 'urn:oasis:names:tc:ebcore:partyid-type'
        _defaults['def_prty_schma_typ'] = 'iso6523'
        _defaults['def_ptry_id'] = '0123456789' 
        print(_defaults)
        return _defaults


class ie_Handler:

    def __init__(self):
        self.defaults = {}
        self.load_defaults = load_defaults(self.defaults)