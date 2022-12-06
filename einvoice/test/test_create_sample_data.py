#!/usr/bin/env python3
#
# File: test_create_sample_data.py
# About: E-Invoice testing suite; create_sample_data
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-17 (October 17th, 2021)
#
"""Testing code to create sample data."""

from einvoice.discovery.data.create_sample_data import CreateSampleData
from einvoice.config import Logger

LOGGER = __name__

def test_generate_fake_address():
    """Pytest for creating sample data."""
    test_logger = Logger()
    log = test_logger.create_logger()
    data_factory = CreateSampleData()
    address = data_factory.generate_fake_address(4)
    log.info(address)
    return address
