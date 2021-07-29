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
"""The classes and functions responsoble for 4-corners participant discovery.

This module is responsible for retaining the inovice while work is done to
prepare the request do a UNAPTR DNS look-up to obtain the SMP URI, perform
the UNAPTR DNS look-up and perform SMP query on the URI returned,

    Args:
        _party_id: str
        The unique identifier of the party being searched for.

        _prty_id_schema_type: str
        An alternate Party ID Schema if not using the default.Schema

        _einvoice: obj (einvoice)
        An einvoice object (which is a JSON file)

    Attributes:

    Raises:

    Returns:

"""
from dataclasses import dataclass
import hashlib
import base64
from json import dumps
from ei_logging import create_logger

ulog = create_logger("ei_handler")

@dataclass
class SMLURN:
    """Dataclass which represents the base URN for the SML query.

    The base URN to be constructed as a string.

    Args:

    Attributes:
        prty_id_spec: str
            The party ID specification.
        prty_id_schma_type: str
            The party ID schema type.
        prty_id: str
            The party ID

    Returns:

    Raises:
    """
@dataclass
class SMLURN:
    """A Dataclass which defines the URN"""
    ulog.debug("Created an instance of SMLURN")
    prty_id_spec: str = "urn:oasis:names:tc:ebcore:partyid-type"
    prty_id_schma_type: str = "iso6523"
    prty_id: str = "0123456789"
        
    def prty_urn(self) -> str:
        """Construct string for the party's URN"""
        return self.prty_id_spec + ":" + self.prty_id_schma_type + "::" \
            + self.prty_id

    final_urn: str = ""
    urn_shaw256_hash: str = ""
    urn_base32_hash: str = ""


def createSMLLookup(_urn="", _schema="", _id=""):
    """Constructs the full URN for lookup"""
    lookup_str = SMLURN()
    if not _urn == "":
        lookup_str.prty_id_spec = _urn
    if not _schema == "":
        lookup_str.prty_id_schema_type = _schema
    if not _id == "":
        lookup_str.prty_id = id
    lookup_str.final_urn = lookup_str.prty_urn()
    ulog.debug("Constructed urn from dataclass definition %s" % lookup_str.final_urn)
    return lookup_str


def apply256Hash(_smlurn_obj):
    """Applys SHA256 hash to the lookup"""
    ulog.debug("Applying shaw256 hash.")
    _data = _smlurn_obj.final_urn
    encoded_data = _data.encode()
    hash256 = hashlib.sha256(encoded_data)
    _smlurn_obj.urn_shaw256_hash = hash256.hexdigest()
    ulog.debug("hex verision of shaw256 is: %s" % _smlurn_obj.urn_shaw256_hash)
    return _smlurn_obj


def applyBase32(_smlurn_obj):
    """Apply Base32 encoding per the spec"""
    ulog.debug("Applying Base32 to shaw256 hash.")
    _string = _smlurn_obj.urn_shaw256_hash
    # first convert to a byte-like object
    b_string = _string.encode("utf-8")
    # do the base32 conversion
    b_string_base32_hash = base64.b32encode(b_string)
   
    # Convert it back to a string so it can be handled by json
    _smlurn_obj.urn_base32_hash = b_string_base32_hash.decode('utf-8')
    ulog.debug("Base32 conversion of shaw256 is: %s" % _smlurn_obj.urn_base32_hash)
    return _smlurn_obj


def writeURNtoJSON(_smlurn, _f_n):
    """Write the urn values to a file"""
    ulog.debug("Writing the SMLURN object to file.")
    json_str = dumps(_smlurn.__dict__)
    with open(_f_n, "w") as f:
        f.write(json_str)


# Everything that happens to follow takes place on 
# an SMLURN dataclass object which is handed between the 
# function calls.

# Create an intial SMLURN oject using defaults.
sml_lookup = createSMLLookup("", "", "")

# apply the shaw256 hash to the urn
sml_lookup256 = apply256Hash(sml_lookup)

# apply the base32 hash to the shaw256 hash
sml_lookup256toB32 = applyBase32(sml_lookup256)

# give the variable a more friendy name
final_sml_obj = sml_lookup256toB32

# write the SMLURN dataclass object to a file
writeURNtoJSON(final_sml_obj, "./sml_urn.json")
