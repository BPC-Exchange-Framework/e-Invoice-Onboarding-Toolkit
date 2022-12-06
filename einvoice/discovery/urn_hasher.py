#!/usr/bin/env python3
#
# pylint: disable=R0902. R0915. W1203
# disable: too many attributes. too many statements, use lazy formatting.
# File: urn_hasher.py
# About: create the urn hashes for a dns NPTR record look-up
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
"""The classes and functions to create the urn hashes for a NAPTR look-up.

This module is responsible for transforming a urn of into a
sha256 hash and then hashing it with base32.
This is to prepare it for the UNAPTR DNS look-up to obtain the SMP URI.
"""
import hashlib
import base64
from json import dumps
from einvoice.discovery.urn import Urn
from einvoice.discovery.create_tracking_id import CreateTrackingID

LOGGER = __name__

class Hasher:
    """Construct a base URN for the SML query and prepares the hashes.

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
        NA

    Raises:
        NA
    """

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        self.einvoice_id_creator = None
        self.einvoice_id = ""
        self.msg = ""
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

    def hasher(self, in_specification, in_schema, in_party_id, log):
        """Construct the hashed urn for lookup."""
        # Create the tracking id
        self.specification = in_specification
        log.info(f"Using specification {self.specification}")
        self.schema = in_schema
        log.info(f"Using schema: {self.schema}")
        self.party_id = in_party_id
        log.info(f"Using party_id: {self.party_id}")
        self.einvoice_id_creator = CreateTrackingID()
        self.einvoice_id = self.einvoice_id_creator.create_tracking_id(10, log)

        # Create a urn object
        self.urn = Urn(self.einvoice_id, self.specification,
                       self.schema, self.party_id)

        # Call the method which actually puts the urn together.
        self.final_urn = self.urn.urn()
        log.info(
            f"Created urn from input - {self.final_urn} - {self.einvoice_id}"
        )
        log.info(
            f"Implemented via the urn dataclass in the urn module. - {self.einvoice_id}"
        )

        # Make sure the urn is in all lowercase
        self.final_urn_lower_case = self.final_urn.lower()
        log.info(
            f"Converted urn to lower case - {self.final_urn_lower_case} - {self.einvoice_id}"
        )
        log.info(
            f"Implemented using the lower() string method - {self.einvoice_id}"
        )

        # encode the urn to a byte-like object.
        self.urn_lower_encoded = self.final_urn_lower_case.encode("utf-8")
        log.info(
            "Encoded the urn as a 'byte-like' object: " +
            self.final_urn_lower_case + "-" + self.einvoice_id
        )
        log.info(
            f'Implemented using the .encode("utf-8") string method - {self.einvoice_id}'
        )

        # Apply the sha256 to the urn.
        self.urn_sha256_hashed = hashlib.sha256(self.urn_lower_encoded)
        self.msg = "Apply the SHA256 hash to the urn: "
        self.msg = self.msg + str(self.urn_sha256_hashed)
        self.msg = self.msg + " - " + self.einvoice_id
        log.info(self.msg)
        log.info(
            f"Implemented using hashlib.sha256() - {self.einvoice_id}"
        )

        # Obtain the hash digest of the sha256 urn
        self.urn_sha256_digest = self.urn_sha256_hashed.digest()
        log.info(
            f"Obtain the hex digest of the SHA256 hashed urn {self.urn_sha256_digest} -"
            "{self.einvoice_id}"
        )
        log.info(
            "Implemented using .digest of the hashlib module. "
            "Output returned is the digest of the byte string. - " + self.einvoice_id
        )

        # Obtain the base32 has of the hex digest of the sha256 encoded urn
        self.urn_b32_hash = base64.b32encode(self.urn_sha256_digest)
        log.info(
            f"Obtain the base32 hash of the hex digest of the SHA256\
            encoded urn: {self.urn_b32_hash} - {self.einvoice_id}"
        )
        log.info(
            f"Implemented using the b32encode method of the base64 package. - {self.einvoice_id}"
        )

        # Strip the output of extraneous equal signs
        self.urn_b32_cleaned = self.urn_b32_hash.rstrip(b"=")
        log.info(
            f"Strip out the equals sign from the output: \
            {self.urn_b32_cleaned} -  {self.einvoice_id}"
        )
        log.info(
            f"Implements rstrip() method of String - {self.einvoice_id}"
        )

        # Convert the the output to lower case.
        self.lower_case_b32 = self.urn_b32_cleaned.lower()
        self.msg = "Convert all characters to lowercase: "
        self.msg = self.msg + str(self.lower_case_b32)
        self.msg = self.msg + " - " + self.einvoice_id
        log.info(self.msg)
        self.msg = "Implements .lower() method of String - "
        self.msg = self.msg + self.einvoice_id
        log.info(self.msg)

        # Decode the byte-like object back into string.
        self.final_urn_b32 = self.lower_case_b32.decode("utf-8")
        self.msg = "Decode the byte-like object back into a string: "
        self.msg = self.msg + self.final_urn_b32
        self.msg = self.msg + " - " + self.einvoice_id
        log.info(self.msg)
        self.msg = 'Implements the .decode("utf-8") from String. - '
        self.msg = self.msg + self.einvoice_id
        log.info(self.msg)
        log.info(f"Final hash for urn is: {self.final_urn_b32}")

        return {
            "specification": self.specification,
            "schema_type_id": self.schema,
            "party_id": self.party_id,
            "final_urn": self.final_urn_lower_case,
            "urn_hash": self.final_urn_b32,
            "einvoice_id": self.einvoice_id,
        }

    def write_hashes_to_file(self, urn_dictionary, filename, log):
        """Write the urn values to a file."""
        self.msg = "Writing the dictionary of urn values to file: "
        self.msg = self.msg + str(filename)
        log.info(self.msg)
        self.json_str = dumps(urn_dictionary.__dict__)
        with open(filename, mode="w", encoding=str) as my_file:
            my_file.write(self.json_str)
