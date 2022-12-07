#!/usr/bin/env python3
# pylint: disable=W1203
# Not using lazy logging.
# File: test_line_item.py
# About: E-Invoice testing suite; line_item.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest."""

import os
from os.path import join, dirname
from dotenv import load_dotenv
from einvoice.discovery.accessor import Accessor
from einvoice.config import Logger

LOGGER = __name__


def test_accessor():
    """Pytest case for test_accessor."""
    accessor_test = Accessor()
    logger_test = Logger()
    log = logger_test.create_logger()
    log.info("Start accessor test")
    dotenv_path = join(dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)
    specification = str(os.getenv("TEST_SPECIFICATION_2"))
    log.info("Specification: %s", specification)
    schema_id = str(os.getenv("TEST_SCHEMA_ID_2"))
    log.info("schema_id: %s", schema_id)
    party_id = str(os.getenv("TEST_PARTY_ID_2"))
    log.info("party_id: %s", party_id)
    domain = str(os.getenv("TEST_SML_DOMAIN"))

    test_urn = accessor_test.call_hash(specification, schema_id,
                                       party_id, log)
    log.info(f"returned urn dict: {test_urn}")
    test_specification = test_urn["specification"]
    test_schema_type_id = test_urn["schema_type_id"]
    test_party_id = test_urn["party_id"]
    example_urn = (f"{test_specification}:{test_schema_type_id}::"
                   f"{test_party_id}")

    log.info("Urn is: %s", example_urn)
    test_final_urn = test_urn["final_urn"]
    assert test_final_urn == example_urn.lower()

    hashed_urn = accessor_test.call_hash(test_specification,
                                         test_schema_type_id,
                                         test_party_id, log)
    log.info("Hashed urn: %s", hashed_urn)
    assert hashed_urn["urn_hash"] == (
        "vs2l6dxjq4it3hrsosbhb75"
        "xo4wpa4agukpprc2nnm3jepvdbjya"
    )
    smp_results = accessor_test.call_dns_lookup(hashed_urn["urn_hash"],
                                                domain, log)
    log.info(smp_results[0])
    assert smp_results[0] == "https://my-smp-url.com/"
    assert smp_results[1]['order'] == 100
    assert smp_results[1]['preference'] == 100
    assert smp_results[1]['flags'] == 'U'
    assert smp_results[1]['regexp'] == "!^.*$!https://my-smp-url.com/!"
    assert smp_results[1]['replacement'] == '.'
