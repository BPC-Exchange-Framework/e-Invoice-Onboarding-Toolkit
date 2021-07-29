#!/usr/local/bin python3
#
# File: test_ei_handler.py
# About: e-Invoice testing suite; ei_handler.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
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
from ei_logging import (create_logger)
from ei_handler import (SMLURN, createSMLLookup, apply256Hash, applyBase32, writeURNtoJSON)

def test_SMLURN():
    smlurn = createSMLLookup("","","")
    assert smlurn.prty_id_spec == "urn:oasis:names:tc:ebcore:partyid-type"
    assert smlurn.prty_id_schma_type == "iso6523"
    assert smlurn.ßprty_id == "0123456789"

