#!/usr/bin/env python3
#
# File: test_line_item.py
# About: e-Invoice testing suite; line_item.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-08-15 (August 15th, 2021)
#
"""This is a test file to be run using pytest.

"""
from einvoice.app_logging import create_logger
from einvoice.line_item import LineItem


def create_line_item():
    """Test helper to create an instace of an object to test."""
    some_line_item = LineItem("KCAL-0.0001", "Case",
                              "Diet Cola", "Tastes better than Slurm.",
                              144, 10.29)
    return some_line_item


def test_line_item():
    """Test case for line_item."""
    log = create_logger("test_line_item")
    log.debug("Begin testing line_item.")
    another_line_item = create_line_item()
    assert another_line_item.line_item_id == "KCAL-0.0001"
    assert another_line_item.line_item_per == "Case"
    assert another_line_item.line_item_name == "Diet Cola"
    assert another_line_item.line_item_description \
        == "Tastes better than Slurm."
    assert another_line_item.line_item_quantity == 144
    assert another_line_item.line_item_price_per_item == 10.29
    assert another_line_item.calculate_line_item_total() \
        == another_line_item.line_item_quantity \
        * another_line_item.line_item_price_per_item
    log.debug("Completed testing party_address.")
