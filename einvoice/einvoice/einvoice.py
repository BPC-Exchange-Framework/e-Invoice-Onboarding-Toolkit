#!/usr/bin/env python3
#
# File: einvoice.py v2
# About: Dataclass definition of an einvoice object.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The classes and functions which define a prototype e-Invoice.

This is a model definition of an e-Invoice which can be used in a four
corners distributed e-services implementation.

    Usage:
    my_einvoice = einvoice()
"""
from dataclasses import dataclass
from party_address import Address
from line_item import LineItem


@dataclass
class EInvoice:
    """Represents an e-Invoice object.

    Args:

    Attributes:
        invoice_uuid: str
            UUID created from CreateUUID class as a String,
        invoice_date: str
            The date of the Invoice expressed as a String.
        seller_address: obj
            Seller's place of busines as an Address() object.
        buyer_address: obj
            Buy's place of business as an Address() object.
        line_items[]: obj
            An array of line_item() objects.
        invoice_total: float
            The total cost of all line_items.

    Raises:

    Returns:

    """

    einvoice_uuid: str
    einvoice_date: str
    einvoice_sellers_address: Address()
    einvoice_buyers_addres: Address()
    einvoice_line_items: list(LineItem())

    def invoice_total(self) -> float:
        """Sum the line items to get an invoice total."""
        self.total = 0.0
        if (len(self.einvoice_line_items)) > 0:
            for i in range(len(self.einvoice_line_items)):
                if type(self.einvoice_line_items[i].line_item_total) is float:
                    self.total = (self.total +
                                  self.einvoice_line_items[i].line_item_total)
        return self.total
