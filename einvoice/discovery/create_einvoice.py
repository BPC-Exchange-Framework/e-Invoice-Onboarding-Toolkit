#!/usr/bin/env python3
#
# pylint: disable=R0913, R0903
# too many arguments, too few public methods
# File: create_semantic_model.py
# About: Demonstrate how to implement the semantic model dataclass.
# Development: Kelly Kinney
# Date: 2022-06-04 (June 4, 2022)
#
"""Create an einvoice from the semantic model dataclass."""

import uuid
from datetime import date
from einvoice.discovery.semantic_model import EInvoice
from einvoice.discovery.data.create_sample_data import CreateSampleData


class CreateEInvoice:
    """Class to create an einvoice from the semantic model dataclass.

    Args:
    NA

    Attributes:
    NA

    Returns:
    An instance of an einvoice based on the semantic_model.

    Raises:
    NA

    """

    def __init__(self):
        """Define values for an instance of the the class."""
        self.einvoice = None

    def create_einvoice(
        self,
        invoice_uuid=None,
        invoice_date=None,
        sellers_address=None,
        buyers_address=None,
        line_items=None,
    ):
        """Create the einvoice from the inputs provided."""
        if invoice_uuid is None:
            invoice_uuid = uuid.uuid4()
        if invoice_date is None:
            invoice_date = date.today()
        if sellers_address is None:
            sellers_address = CreateSampleData.generate_fake_address(1)
        if buyers_address is None:
            buyers_address = CreateSampleData.generate_fake_address(1)
        if line_items is None:
            line_items = CreateSampleData.create_sample_list_items(3)

        self.einvoice = EInvoice(
            uuid, date, sellers_address, buyers_address, line_items
        )

        return self.einvoice
