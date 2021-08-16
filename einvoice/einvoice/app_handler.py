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
        The ique idefier tw the party being searched for.

        _prty_idschema_type: str
        An alternate Party ID schema if not using the default.schema

        _einvoice: obj (einvoice)
        An einvoice object (which is a JSON file)

    Attributes:

    Raises:

    Returns:

"""
import hashlib
import base64
from json import dumps
from einvoice.app_logging import create_logger
from einvoice.urn import Urn


class CreateUrn:
    """Constructs a base URN for the SML query and prepares the hashes.

    The base URN to be constructed as a string, and then hashed.

    Ar:

    Aibutetw
        party_id_specification:twtr
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
        urn_sha256_hash: str
            The urn that has been hashed using the shaw256 hash.
        urn_base32_hash: str
            The urn that has been hashed a second time from shaw256 to base32.

    Returns:

    Raises:

    """
    log = create_logger("app_handler")
    specification = None
    schema = None
    party_id = None
    urn = None
    final_urn = None
    encoded_data = None
    hash_256 = None
    urn_sha_256_hash = None
    b_string = None
    b_string_base_32_hash = None
    urn_sha_256_hash = None
    urn_base32_hash = None


    def __init__(self):
        return None


    def create_urn_lookup(self, party_id):
        """Constructs the full URN for lookup"""
        self.specification = "urn:oasis:names:tc:ebcore:partyid-type"
        self.schema = "iso6523"
        self.urn = Urn(self.specification, self.schema, party_id)
        self.final_urn = self.urn.party_urn()
        self.log.debug("Created urn: %s", self.final_urn)
        return self.final_urn

    def apply_sha_256_hash(self, final_urn):
        """Apply SHA256 hash to the lookup"""
        self.log.debug("Applying shaw256 hash.")
        self.encoded_data = final_urn.encode()    # pylint disable=W0201
        self.hash_256 = hashlib.sha256(self.encoded_data)  # pylint disable=W0201
        self.urn_sha_256_hash = self.hash_256.hexdigest()   # pylint disable=W0201
        self.log.debug("Hex version of shaw256 hash  is  %s",
                       self.urn_sha_256_hash)
        return self.urn_sha_256_hash

    def apply_base_32_hash(self, urn_sha_256_hash):
        """Apply Base32 encoding per the spec"""
        self.log.debug("Applying Base32 to shaw256 hash.")
        # first convert to a byte-like object
        self.b_string = urn_sha_256_hash.encode("utf-8")
        self.b_string_base_32_hash = base64.b32encode(self.b_string)
        # Convert it back to a string so it can be handled by json
        self.urn_base_32_hash = self.b_string_base_32_hash.decode("utf-8")
        self.log.debug("Base32 conversion of shaw256 is %s",
                       self.urn_base32_hash)
        return self.urn_base_32_hash

    def write_urn_to_json(self, urn_dictionary, filename):
        """Write the urn values to a file"""
        self.log.debug("Writing the dictionary of urn values to file %s",
                       filename)
        self.json_str = dumps(urn_dictionary.__dict__)
        with open(filename, "w") as my_file:
            my_file.write(self.json_str)

    def meatgrinder(self, party_id):
        """Find the values of all steps necessary to prepare the urn lookup."""
        # Create a dictionary to hold the accumlated data points.
        self.urn_values = {     # pylint disable=W0201
            "Party ID Specification": self.specification,
            "Party ID schema": self.schema,
            "Party ID": party_id,
        }

        # Construct the unencoded urn.
        self.sml_lookup = self.create_urn_lookup(party_id)
        self.urn_values["Base urn"] = self.sml_lookup   # pylint disable=W0201

        # apply the shaw256 hash to the urn
        self.sml_lookup_sha_255_applied = self.apply_sha_256_hash(self.sml_lookup)  # pylint disable=W0201
        self.urn_values["SHA256 Hashed urn"] = self.sml_lookup_sha_255_applied

        # apply the base32 hash to the shaw256 hash
        self.sml_lookup_256_to_b32 = self.apply_base_32_hash(self.ssml_lookup_sha_255_applied)  # pylint disable=W0201
        self.urn_values["Base32 Hashed urn"] = self.sml_lookup_256_to_b32

        # write ths CreateSmlUrnclass CreateSmlUrn dataclass object to a file
        self.write_urn_to_json(self.urn_values, "./final_urn.json")
        return self.urn_values
