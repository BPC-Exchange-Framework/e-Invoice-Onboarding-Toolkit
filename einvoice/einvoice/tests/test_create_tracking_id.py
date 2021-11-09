#!/usr/bin/env python3
#
# File: test_create_tracking_id.py
# About: e-Invoice testing suite; create_tracking_id.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-11-05 (November 11th, 2021)
#
"""This is a test file to be run using pytest.

"""
from einvoice.app_logging import create_logger
from einvoice.create_tracking_id import CreateTrackingID


def test_app_looging():
    log = create_logger("test_app_logging")
    log.info("Testing app loggin")


def test_create_urn_id():
    """Test case for party_address."""
    log = create_logger("test_create_tracking_id")
    log.info("Begin tracking id creation.")
    id_size = 10
    tracking_id_creator = CreateTrackingID()
    tracking_id = tracking_id_creator.create_tracking_id(id_size)
    log.info("created tracking id: %s", tracking_id)
    log.info("urn_uuid is type: %s", type(tracking_id))
    assert isinstance(tracking_id, str)
    assert len(tracking_id) == id_size
    log.info("Completed testing tracking id creation.")
