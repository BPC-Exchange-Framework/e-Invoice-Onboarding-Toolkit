#!/usr/bin/env python3
#
# File: party_address.py
# About: Dataclass definition of a party's address for an einvoice.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The dataclass definition of a party's address.

This is a model defined for the Address of a party in
an e-Invoice which can be used in a four
corners distributed e-services implementation.

    Usage:
    my_address = Address()
"""
from dataclasses import dataclass


@dataclass
class Address:
    """A dataclass representing a physical address.

    Used to store the address of the buyer and seller.

    Args:

    Attributes:
        org_id: str
            A unique identifier to reference the Address object.  Default
            value is undefined.
        name: str
            A common name for the business of Address owner.  Default
            value is undefined.
        address_1: str
            Address line #1.  Default value is undefined.
        address_2: str
            Address line #2. Default value is undefined.
        city: str
            The city where the business address is located. Default
            value is undefined.
        state: str
            The state where the business address is located. Default
            value is undefined.
        zip_: str
            The zip code where the business address is located. Default
            value is undefined.

    Returns:

    Raises:
    """

    org_id: str = ""
    name: str = ""
    address_1: str = ""
    address_2: str = ""
    city: str = ""
    state: str = ""
    zip_: str = ""
