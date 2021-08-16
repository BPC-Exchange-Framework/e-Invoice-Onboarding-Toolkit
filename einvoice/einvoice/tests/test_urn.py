#!/usr/bin/env python3
#
# File: test_urn.py
# About: e-Invoice testing suite; urn.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest.

"""
from einvoice.app_logging import create_logger
from einvoice.urn import Urn


def create_urn():
    """Test helper to create an instace of an object to test."""
    some_urn = Urn("urn:oasis:names:tc:ebcore:partyid-type",
                   "iso6523", "0123456789")
    return some_urn


def test_urn():
    """Test case for party_address."""
    log = create_logger("test_urn")
    log.debug("Begin testing urn creation.")
    another_urn = create_urn()
    assert (
        another_urn.party_id_specification
        == "urn:oasis:names:tc:ebcore:partyid-type"
    )
    assert another_urn.party_id_schema_type == "iso6523"
    assert another_urn.party_id == "0123456789"
    assert (
        another_urn.party_urn()
        == "urn:oasis:names:tc:ebcore:partyid-type:iso6523::0123456789"
    )
    log.debug("Completed testing urn creation.")
