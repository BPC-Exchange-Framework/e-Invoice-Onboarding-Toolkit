#!/usr/bin/env python3
#
# File: test_party_address.py
# About: E-Invoice testing suite; party_address.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""Test file to be run using pytest."""
from einvoice.config import Logger
from einvoice.discovery.party_address import Address

LOGGER = __name__

def create_address():
    """Test helper to create an instance of an object to test."""
    some_address = Address("01245zyx", "Big Corporate Company",
                           "123 Main Street", "Attn: Accounts Payable",
                           "Springfield", "Confusion", "90210")
    return some_address


def test_party_address():
    """Test case for party_address."""
    test_logger = Logger()
    log = test_logger.create_logger()
    log.debug("Begin testing party_address.")
    another_address = create_address()
    assert another_address.org_id == "01245zyx"
    assert another_address.name == "Big Corporate Company"
    assert another_address.address_1 == "123 Main Street"
    assert another_address.address_2 == "Attn: Accounts Payable"
    assert another_address.city == "Springfield"
    assert another_address.state == "Confusion"
    assert another_address.zip_ == "90210"
    log.debug("Completed testing party_address.")
