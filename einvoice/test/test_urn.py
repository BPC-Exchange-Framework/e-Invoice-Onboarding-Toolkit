#!/usr/bin/env python3
#
# File: test_urn.py
# About: E-Invoice testing suite; urn.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""Test file to be run using pytest."""
from einvoice.config import Logger
from einvoice.discovery.urn import Urn


def create_urn():
    """Test helper to create an instance of an object to test."""
    some_urn = Urn("ABCDEFG123", "urn:oasis:names:tc:ebcore:partyid-type",
                   "iso6523", "0123456789")
    return some_urn


def test_urn():
    """Test case for party_address."""
    log = Logger().create_logger()
    log.info("Begin testing urn creation.")
    another_urn = create_urn()
    assert another_urn.specification == "urn:oasis:names:tc:ebcore:"\
        "partyid-type"
    assert another_urn.schema_id == "iso6523"
    assert another_urn.party_id == "0123456789"
    assert (
        another_urn.urn() == "urn:oasis:names:tc:"
        "ebcore:partyid-type:iso6523::0123456789"
    )
    log.info("Completed testing urn creation.")
