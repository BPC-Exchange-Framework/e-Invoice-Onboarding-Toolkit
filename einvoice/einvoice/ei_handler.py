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

handler_log = create_logger("ei_handler")


@dataclass
class SMLURN:
    """Dataclass which represents the base URN for the SML query.

    The base URN to be constructed as a string.

    Args:

    Attributes:
        party_id_specification: str
            The party ID specification.
        party_id_schema_type: str
            The party ID schema type.
        party_id: str
            The party ID
        party_urn: str
            The full urn constructed by default values or passed into class
            when called.
        final_urn: str
            A version of the full urn which is not constructed on the
            fly but held (essentially as a constant)
        urn_shaw256_hash: str
            The urn that has been hashed using the shaw256 hash.
        urn_base32_hash: str
            The urn that has been hashed a second time from shaw256 to base32.

    Returns:
w
    Raises:
    """
    handler_log.debug("Created an instance of SMLURN")
    party_id_specification: str = "urn:oasis:names:tc:ebcore:partyid-type"
    handler_log.debug("party_id_specification: %s" % party_id_specification)
    party_id_schema_type: str = "iso6523"
    handler_log.debug("party_id_schema_type: %s" % party_id_schema_type)
    party_id: str = "0123456789"
    handler_log.debug("party_id: %s" % party_id)

    def party_urn(self) -> str:
        """Construct string for the party's URN"""
        return (self.party_id_specification + ":"
                + self.party_id_schema_type
                + "::" + self.party_id)
    handler_log.debug("party_urn: %s" % party_urn)

    def final_urn(self) -> str:
        """Return the urn as essetially a constant."""
        return (str(self.party_urn))
    handler_log.debug("final_urn: %s" % final_urn)

    urn_shaw256_hash: str = ""
    urn_base32_hash: str = ""


def create_sml_lookup(_urn="", _schema="", _id=""):
    """Constructs the full URN for lookup"""
    lookup_str = SMLURN()
    if _urn != "":
        lookup_str.party_id_specification = _urn
    if _schema != "":
        lookup_str.party_id_schema_type = _schema
    if _id != "":
        lookup_str.party_id = _id
    lookup_str.final_urn = lookup_str.party_urn()
    # lookup_str.final_urn = (_urn + ":" + _schema + "::" + _id)
    log_msg = ("Constructed urn from dataclass definition %s"
               % lookup_str.final_urn)
    handler_log.debug(log_msg)
    return lookup_str


def apply_shaw256_hash(_smlurn_obj):
    """Applys SHA256 hash to the lookup"""
    handler_log.debug("Applying shaw256 hash.")
    _data = _smlurn_obj.final_urn
    encoded_data = _data.encode()
    hash256 = hashlib.sha256(encoded_data)
    _smlurn_obj.urn_shaw256_hash = hash256.hexdigest()
    log_msg = ("Hex version of shaw256 hash  is  %s"
               % _smlurn_obj.urn_shaw256_hash)
    handler_log.debug(log_msg)
    return _smlurn_obj


def apply_base32_hash(_smlurn_obj):
    """Apply Base32 encoding per the spec"""
    handler_log.debug("Applying Base32 to shaw256 hash.")
    _string = _smlurn_obj.urn_shaw256_hash
    # first convert to a byte-like object
    b_string = _string.encode("utf-8")
    # do the base32 conversion
    b_string_base32_hash = base64.b32encode(b_string)

    # Convert it back to a string so it can be handled by json
    _smlurn_obj.urn_base32_hash = b_string_base32_hash.decode('utf-8')
    log_msg = ("Base32 conversion of shaw256 is %s"
               % _smlurn_obj.urn_base32_hash)
    handler_log.debug(log_msg)
    return _smlurn_obj


def write_urn_to_json(_smlurn, _filename):
    """Write the urn values to a file"""
    handler_log.debug("Writing the SMLURN object to file.")
    json_str = dumps(_smlurn.__dict__)
    with open(_filename, "w") as my_file:
        my_file.write(json_str)


if __name__ == "__main__":
    # Everything that happens to follow takes place on
    # an SMLURN dataclass object which is handed between the
    # function calls.

    # Create an intial SMLURN oject using defaults.
    sml_lookup = create_sml_lookup("", "", "")

    # apply the shaw256 hash to the urn
    sml_lookup256 = apply_shaw256_hash(sml_lookup)

    # apply the base32 hash to the shaw256 hash
    sml_lookup256toB32 = apply_base32_hash(sml_lookup256)

    # give the variable a more friendy name
    final_sml_obj = sml_lookup256toB32

    # write the SMLURN dataclass object to a file
    write_urn_to_json(final_sml_obj, "./sml_urn.json")
