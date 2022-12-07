#!/usr/bin/env python3
#
# File: app_handler.py
# About: Responsible for discovery components of 4-corners model.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
"""The classes and functions responsible for 4-corners participant discovery.

This module is responsible for retaining the invoice while work is done to
prepare the request do a UNAPTR DNS look-up to obtain the SMP URI, perform
the UNAPTR DNS look-up and perform SMP query on the URI returned,

    Args:
        _party_id: str
        The unique identifier of the party being searched for.

        _party_id_schema_type: str
        An alternate Party ID Schema if not using the default.Schema

        _discovery: obj (discovery)
        An discovery object (which is a JSON file)

    Attributes:
        NA

    Raises:
        NA

    Returns:
        NA
"""
from dataclasses import dataclass
import hashlib
import base64
from json import dumps


@dataclass
class SmlUrn:
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
        NA

    Raises:
        NA

    """

    party_id_specification: str = "urn:oasis:names:tc:ebcore:partyid-type"
    party_id_schema_type: str = "iso6523"
    party_id: str = "0123456789"

    def party_urn(self) -> str:
        """Construct string for the party's URN."""
        return self.party_id_specification +\
            ":" + self.party_id_schema_type + "::" + self.party_id

    def final_urn(self) -> str:
        """Return the urn as essentially a constant."""
        return str(self.party_urn)

    urn_shaw256_hash: str = ""
    urn_base32_hash: str = ""


def create_sml_lookup(_urn="", _schema="", _id=""):
    """Construct the full URN for lookup."""
    lookup_str = SmlUrn()
    if _urn != "":
        lookup_str.party_id_specification = _urn
    if _schema != "":
        lookup_str.party_id_schema_type = _schema
    if _id != "":
        lookup_str.party_id = _id
    lookup_str.final_urn = lookup_str.party_urn()
    return lookup_str


def apply_shaw256_hash(_smlurn_obj):
    """Apply SHA256 hash to the lookup."""
    _data = _smlurn_obj.final_urn
    encoded_data = _data.encode()
    hash256 = hashlib.sha256(encoded_data)
    _smlurn_obj.urn_shaw256_hash = hash256.hexdigest()
    return _smlurn_obj


def apply_base32_hash(_smlurn_obj):
    """Apply Base32 encoding per the spec."""
    _string = _smlurn_obj.urn_shaw256_hash
    # first convert to a byte-like object
    b_string = _string.encode("utf-8")
    # do the base32 conversion
    b_string_base32_hash = base64.b32encode(b_string)

    # Convert it back to a string so it can be handled by json
    _smlurn_obj.urn_base32_hash = b_string_base32_hash.decode("utf-8")
    return _smlurn_obj


def write_urn_to_json(_smlurn, _filename):
    """Write the urn values to a file."""
    json_str = dumps(_smlurn.__dict__)
    with open(_filename, "w", encoding=str) as my_file:
        my_file.write(json_str)


if __name__ == "__main__":
    # Everything that happens to follow takes place on
    # an SMLURN dataclass object which is handed between the
    # function calls.

    # Create an initial SMLURN object using defaults.
    sml_lookup = create_sml_lookup("", "", "")

    # apply the shaw256 hash to the urn
    sml_lookup256 = apply_shaw256_hash(sml_lookup)

    # apply the base32 hash to the shaw256 hash
    sml_lookup256toB32 = apply_base32_hash(sml_lookup256)

    # give the variable a more friendly name
    final_sml_obj = sml_lookup256toB32

    # write the SMLURN dataclass object to a file
    write_urn_to_json(final_sml_obj, "./sml_urn.json")
