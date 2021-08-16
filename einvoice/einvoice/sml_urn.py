#!/usr/bin/env python3
#
# File: smlurn.py
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
from ei_logging import create_logger


@dataclass
class Smlurn:
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

    Raises:
    """
    handler_log = create_logger("handler")

    handler_log.debug("Created an instance of Smlurn")

    party_id_specification: str = "urn:oasis:names:tc:ebcore:partyid-type"
    handler_log.debug("party_id_specification: %s" % party_id_specification)

    party_id_schema_type: str = "iso6523"
    handler_log.debug("party_id_schema_type: %s" % party_id_schema_type)

    party_id: str = "0123456789"
    handler_log.debug("party_id: %s" % party_id)

    def party_urn(self) -> str:
        """Construct string for the party's URN"""
        return (party_id_specification + ":"
                + party_id_schema_type
                + "::" + party_id)
    handler_log.debug("party_urn: %s" % party_urn]

    def final_urn(self) -> str:
        """Return the urn as essetially a constant."""
        return (str(self.party_urn))
    handler_log.debug("final_urn: %s" % final_urn)

    urn_shaw256_hash: str = ""
    urn_base32_hash: str = ""
