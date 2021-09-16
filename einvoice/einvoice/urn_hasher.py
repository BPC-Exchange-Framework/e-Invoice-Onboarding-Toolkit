#!/usr/bin/env python3
#
# pylint: disable=R0902
# disable: too many attributes
# File: urn_hasher.py
# About: create the urn hashes for a dns NPTR record look-up
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
"""The classes and functions to create the urn hashes for a NAPTR look-up

This module is responsible for transforming a urn of into a
sha256 hash and then hashing it with base32.
This is to prepare it for the UNAPTR DNS look-up to obtain the SMP URI.
"""
import hashlib
import base64
from json import dumps
from einvoice.app_logging import create_logger
from einvoice.urn import Urn


class Hasher:
    """Constructs a base URN for the SML query and prepares the hashes.

    The base URN to be constructed as a string, and then hashed.

    Args:

    Attributes:
        log: object
            A custom logging object.
        msg: str
            A custom string handler for a log message.
        specification: str
            The party ID specification.
        schema: str
            The party ID schema type.
        party_id: str
            The party ID
        urn: str
            The full urn constructed by default values or passed into class
            when called.
        final_urn: str
            A version of the full urn which is not constructed on the
            fly but static (essentially as a constant)
        final_urn_lower_case: str
            The full urn normalized to lower case.
        urn_lower_encoded: byte-like object.
            Conversion of the lower case urn to a byte-like object
            to be converted to sha256
        urn_sha256_hashed: object
            The sha256 hash version of the urn.
        urn_sha256_digest: hex obj
            The hex representation of the sha2456 hash.
        urn_b32_hash_: str
            The value encoded again with b32 hash.
        urm_b32_cleaned: str
            The hash with trailing equal signs removed.
        lower_case_b32: str
            The hash normalized again to lower case.
        final_urn_b32: str
            The final output of the base32 applied to the sha256 and then
            made human readable.
        json_str: str
            Holds urn_values for writing to json on the filesystem.


    Returns:

    Raises:

    """

    def __init__(self):
        self.log = create_logger("urn_hasher")
        self.msg = None
        self.specification = None
        self.schema = None
        self.party_id = None
        self.urn = None
        self.final_urn = None
        self.final_urn_lower_case = None
        self.urn_lower_encoded = None
        self.urn_sha256_hashed = None
        self.urn_sha256_digest = None
        self.urn_b32_hash = None
        self.urn_b32_cleaned = None
        self.lower_case_b32 = None
        self.final_urn_b32 = None
        self.json_str = None

    def hasher(self, specification, schema, party_id):
        """Constructs the hashed urn for lookup"""
        self.log.debug("Checkpoint - Created hasher()")
        self.urn = Urn(specification, schema, party_id)
        self.final_urn = self.urn.urn()
        self.final_urn_lower_case = self.final_urn.lower()
        self.log.debug("Checkpoint - constructed urn for hashing")
        self.msg = ("Captured a urn for hashing: ",
                    self.final_urn_lower_case)
        self.log.debug(self.msg)
        self.urn_lower_encoded = self.final_urn_lower_case.encode("utf-8")
        self.urn_sha256_hashed = hashlib.sha256(self.urn_lower_encoded)
        self.urn_sha256_digest = self.urn_sha256_hashed.digest()
        self.log.debug("Checkpoint - Created sha256 hash")
        self.urn_b32_hash = base64.b32encode(self.urn_sha256_digest)
        self.urn_b32_cleaned = self.urn_b32_hash.rstrip(b"=")
        self.lower_case_b32 = self.urn_b32_cleaned.lower()
        self.final_urn_b32 = self.lower_case_b32.decode("utf-8")
        self.log.debug("Checkpoint - Created base32 hash.")
        self.msg = ("Created a hash for look-up: ", self.final_urn_b32)
        self.log.debug(self.msg)
        return {
            "party_id_spec": specification,
            "party_id_schema_type": schema,
            "party_id": party_id,
            "final_urn": self.final_urn_lower_case,
            "urn_hash": self.final_urn_b32,
        }

    def write_hashes_to_file(self, urn_dictionary, filename):
        """Write the urn values to a file"""
        self.log.debug(
            "Writing the dictionary of urn values to file %s", filename)
        self.json_str = dumps(urn_dictionary.__dict__)
        with open(filename, mode="w", encoding=str) as my_file:
            my_file.write(self.json_str)
