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

"""
import hashlib
import base64
from json import dumps
from einvoice.app_logging import create_logger
from einvoice.urn import Urn


class UrnHandler:
    """Constructs a base URN for the SML query and prepares the hashes.

    The base URN to be constructed as a string, and then hashed.

    Args:

    Atributes:
        log: object
            A custom logging object.
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
            fly but staticly (essentially as a constant)
        pre_sha256_encoded_data: byte-like object
            Conversion of the urn to a byte-like object to be conversted
            to sha256
        urn_sha256_hashed: object
            The hashed sha256 version of the urn.
        urn_readable_sha256_hash: str
            The urn that has been hashed using the sha256 hash that has been
            converted into something human readable via hexdigest()
        urn_sha256_byte_obj: byte-like object
            Encode the sha32 urn into a utf-8 byte-like object again
            to prep for Base32 hash.
        urn_b32_byte_obj: byte-like object
            The Base32 hashed object which is still a "byte-like object."
        urn_b32_hash_decoded: str
            The final hash decoded from the byte-like object/utf-8 to a string.
        urn_values: dictionary
            A dictionary to hold values acculuated as we go along.
        urn_formatter: str
            Calls create_urn_lookup directly from within a class method to
            obtain the string value of the urn.
        urn_sha_256_applied: str
            Calls method to apply sha256 hash directly from with the class
            method to obtain a string value of the hashed value.
        urn_b32_applied: str
            The final output of the base32 applied to the sha256 and then
            made human readable.
        json_str: str
            Holds urn_values for writing to json on the filesystem.


    Returns:

    Raises:

    """
    log = create_logger("app_handler")
    specification = None
    schema = None
    party_id = None
    urn = None
    final_urn = None
    pre_sha256_encoded_data = None
    urn_sha256_hashed = None
    urn_readable_sha256_hash = None
    urn_sha256_byte_obj = None
    urn_b32_byte_obj = None
    urn_b32_hash_decoded = None
    urn_values = None
    urn_formatter = None
    urn_sha256_applied = None
    urn_b32_applied = None
    json_str = None

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

    def apply_sha256_hash(self, final_urn):
        """Apply SHA256 hash to the lookup"""
        self.log.debug("Applying shaw256 hash.")
        self.pre_sha256_encoded_data = final_urn.encode()
        self.urn_sha256_hashed = hashlib.sha256(self.pre_sha256_encoded_data)
        self.urn_readable_sha256_hash = self.urn_sha256_hashed.hexdigest()
        self.log.debug(
            "Hex version of shaw256 hash  is  %s",
            self.urn_readable_sha256_hash
        )
        return self.urn_readable_sha256_hash

    def apply_b32_hash(self, urn_readable_sha256_hash):
        """Apply Base32 encoding to the SHA356 hash"""
        self.log.debug("Applying Base32 to sha256 hash.")
        # first convert to a byte-like object
        self.urn_sha256_byte_obj = urn_readable_sha256_hash.encode("utf-8")
        self.urn_b32_byte_obj = base64.b32encode(self.urn_sha256_byte_obj)
        # Convert it back to a string so it can be handled by json
        self.urn_b32_hash_decoded = self.urn_b32_byte_obj.decode("utf-8")
        self.log.debug("Base32 conversion of shaw256 is %s",
                       self.urn_b32_hash_decoded)
        return self.urn_b32_hash_decoded

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
        self.urn_values = {  # pylint disable=W0201
            "Party ID Specification": self.specification,
            "Party ID schema": self.schema,
            "Party ID": party_id,
        }

        # Construct the unencoded urn.
        self.urn_formatter = self.create_urn_lookup(party_id)
        self.urn_values["Base urn"] = self.urn_formatter

        # apply the shaw256 hash to the urn
        self.urn_sha256_applied = self.apply_sha256_hash(self.urn_formatter)
        self.urn_values["SHA256 Hashed urn"] = self.urn_sha256_applied

        # apply the base32 hash to the shaw256 hash
        self.urn_b32_applied = self.apply_b32_hash(self.urn_sha256_applied)
        self.urn_values["Base32 Hashed urn"] = self.urn_b32_applied

        # write ths CreateSmlUrnclass CreateSmlUrn dataclass object to a file
        self.write_urn_to_json(self.urn_values, "./final_urn.json")
        return self.urn_values
