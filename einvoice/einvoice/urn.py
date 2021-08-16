#!/usr/bin/env python3
#
# File: urn.py
# About: Dataclass definition of a urn.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The dataclass object representing a urn for lookup.

The small class encapsulates the necessary information to work
with the urn as an object.

    Usage:
    my_urn = einvoice()

"""
from dataclasses import dataclass


@dataclass
class Urn:
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
        urn: str
            The urn constructed by default values or passed into the
            dataclass when called.

    Returns:

    Raises:

    """

    party_id_specification: str
    party_id_schema_type: str
    party_id: str

    def party_urn(self) -> str:
        """Construct string for the party's URN"""
        return (
            self.party_id_specification
            + ":"
            + self.party_id_schema_type
            + "::"
            + self.party_id
        )
