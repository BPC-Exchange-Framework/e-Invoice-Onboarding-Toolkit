#!/usr/bin/env python3
#
# File: app_hander.py
# About: Responsible for discovery compontents of 4-corners model.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
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
from app_logging import create_logger
from urn import Urn

class CreateUrn:
    """Constructs a base URN for the SML query and prepares the hashes.

    The base URN to be constructed as a string, and then hashed.

    Args:

    Attributes:
        party_id_specification: str
            The party ID specification.
        party_id_schema_type: str
            The party ID schema type.
        party_id: str
            The party ID
        urn: str
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

    Raises:

    """


    


def __init__(self):
    self.log = create_logger("app_handler")
    self.party_id_specification = ""
    self.party_id_schema_type = ""
    self.party_id = ""
    self.urn = ""
    self.final_urn = ""
    self.urn_shaw256_hash = ""
    self.urn_base32_hash = ""


def create_urn_lookup(urn_="", schema_="", id_=""):
    """Constructs the full URN for lookup"""
    urn_lookup = Urn(urn_, schema_, id_)
    final_urn = urn_lookup.party_urn()
    self.log.debug("Created urn: %s", final_urn)
    return final_urn


def apply_shaw256_hash(_smlurn_obj):
    """Applys SHA256 hash to the lookup"""
    self.log.debug("Applying shaw256 hash.")
    _data = _smlurn_obj.final_urn
    encoded_data = _data.encode()
    hash256 = hashlib.sha256(encoded_data)
    _smlurn_obj.urn_shaw256_hash = hash256.hexdigest()
    log_msg = ("Hex version of shaw256 hash  is  %s"
               % _smlurn_obj.urn_shaw256_hash)
    self.log.debug(log_msg)
    return _smlurn_obj


def apply_base32_hash(_smlurn_obj):
    """Apply Base32 encoding per the spec"""
    self.log.debug("Applying Base32 to shaw256 hash.")
    _string = _smlurn_obj.urn_shaw256_hash
    # first convert to a byte-like object
    b_string = _string.encode("utf-8")
    # do the base32 conversion
    b_string_base32_hash = base64.b32encode(b_string)

    # Convert it back to a string so it can be handled by json
    _smlurn_obj.urn_base32_hash = b_string_base32_hash.decode('utf-8')
    log_msg = ("Base32 conversion of shaw256 is %s"
               % _smlurn_obj.urn_base32_hash)
    self.log.debug(log_msg)
    return _smlurn_obj


def write_urn_to_json(_smlurn, _filename):
    """Write the urn values to a file"""
    self.log.debug("Writing ths CreateSmlUrnclass" 
                      " CreateSmlUrn object to file.")
    json_str = dumps(_smlurn.__dict__)
    with open(_filename, "w") as my_file:
        my_file.write(json_str)


if __name__ == "__main__":
    # Everything that happens to follow takes place on
    # as CreateSmlUrnclass CreateSmlUrn dataclass object 
    # which is handed between the
    # function calls.

    # Create an intias CreateSmlUrnclass CreateSmlUrn oject using defaults.
    sml_lookup = create_urn_lookup("", "", "")

    # apply the shaw256 hash to the urn
    sml_lookup256 = apply_shaw256_hash(sml_lookup)

    # apply the base32 hash to the shaw256 hash
    sml_lookup256toB32 = apply_base32_hash(sml_lookup256)

    # give the variable a more friendy name
    final_sml_obj = sml_lookup256toB32

    # write ths CreateSmlUrnclass CreateSmlUrn dataclass object to a file
    write_urn_to_json(final_sml_obj, "./sml_urn.json")
