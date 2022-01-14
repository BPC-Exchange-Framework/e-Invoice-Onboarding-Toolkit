#!/usr/bin/env python3
#
# File: test_create_sample_data.py
# About: e-Invoice testing suite; create_sample_data
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-17 (October 17th, 2021)
#
"""Testing code to create sample data."""

from einvoice.discovery.data.create_sample_data import CreateSampleData
from einvoice.discovery.app_handler import create_logger


def test_generate_fake_address():
    """Pytest for creating sample data"""
    log1 = create_logger("test_generate_fake_addresses")
    data_factory = CreateSampleData()
    address = data_factory.generate_fake_address(4)
    log1.info(address)
    return address
