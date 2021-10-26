#!/usr/bin/env python3
#
# File: test_line_item.py
# About: e-Invoice testing suite; line_item.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest.

"""
import os
from os.path import join, dirname
from random import setstate
from dotenv import load_dotenv
from einvoice.app_logging import create_logger
from einvoice.implementation import Implementation


def test_implementation():
    log = create_logger("test_implementation")
    log.info("Start implementation test")
    dotenv_path = join(dirname(__file__), '../../certificates/.env')
    load_dotenv(dotenv_path)
    SPECIFICATION = str(os.getenv("TEST_SPECIFICATION"))
    log.info("Specification: %s", SPECIFICATION)
    SCHEMA_ID = str(os.getenv("TEST_SCHEMA_ID"))
    log.info("Schema_Id: %s", SCHEMA_ID)
    PARTY_ID = str(os.getenv("TEST_PARTY_ID"))
    log.info("Party_Id: %s", PARTY_ID)
    implementation_tester = Implementation()
    test_urn = implementation_tester.create_urn(SPECIFICATION, SCHEMA_ID,
                                                PARTY_ID)
    example_urn = (f"{test_urn.specification}:{test_urn.schema_id}::"
                   f"{test_urn.party_id}")
    log.info("Urn is: %s", example_urn)
    assert test_urn.urn() == example_urn

    hashed_urn = implementation_tester.hash_urn(test_urn)
    log.info("Hashed urn: %s", hashed_urn)
    assert hashed_urn["urn_hash"] == "yn5tj7bteln4c5o4mtul7yv"\
        "nq3pwu6dpmipcof4pwcbsd3avvn7a"
