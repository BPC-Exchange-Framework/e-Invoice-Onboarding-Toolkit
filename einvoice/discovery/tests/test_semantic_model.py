#!/usr/bin/env python3
#
# File: test_semantic_model.py
# About: e-Invoice testing suite; discovery.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-14 (October 14th, 2021)
#
"""Test file to be run using pytest."""
# from einvoice.discovery.semantic_model import EInvoice
# from einvoice.discovery.line_item import LineItem
from einvoice.discovery.create_einvoice import CreateEInvoice
# import einvoice.discovery.line_item


def test_semantic_model():
    """Test case to generate an einvoice."""
    test_einvoice = CreateEInvoice.create_einvoice(None, None, None, None,
                                                   None)
    test_line_items = test_einvoice.einvoice_line_items
    test_line_items.einvoice_line_items.line_item_total = [10 for _ in
                                                           test_line_items]

# from einvoice.app_logging import create_logger
# from einvoice.party_address import Address
# from einvoice.line_item import LineItem
# from einvoice.data.create_sample_data import CreateSampleData
