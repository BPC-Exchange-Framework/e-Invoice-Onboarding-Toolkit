#!/usr/bin/env python3
#
# File: einvoice.py
# About: Class definition of an einvoice object.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The classes and functions which define a prototype e-Invoice.

This is a model definition of an e-Inoice which can be used in a four
corners distrubuted e-services implementation.

    Usage:
    my_einvoice = einvoice()
"""
from datetime import datetime
from json import dumps
from uuid import uuid4
from app_logging import create_logger
from party_address import Address
from line_item import LineItem


class EInvoice:
    """Represents an e-Inovice object.

    Args:

    Attributes:
        invoice_uuid:
            (String) UUID created from CreateUUID
            class as a String,
        invoice_date:
            The date of the Invoice expressed as a String.
        seller_address:
            Seller's place of busines as an Address() object.
        buyer_address:
            Buy's place of business as an Address() object.
        line_items[]:
            An array of line_item() objects.
        invoice_total:
            A flost representing the total cost of all line_items

    """

    log = create_logger("einvoice")

    @staticmethod
    def sum_line_item_totals(_line_items):
        """Sum all line items for an invoice total."""
        line_item_total = 0
        for obj in _line_items:
            line_item_total = line_item_total + obj.li_total
        return line_item_total

    def __init__(self):
        log.info("Creating an e-Invoice")
        self.invoice_uuid = str(uuid4())
        self.invoice_date = datetime.now().strftime("%Y-%m-%d")
        self.seller_address = Address()
        self.buyer_address = Address()
        self.line_items = [LineItem] # Line Items is list of LineITem
        self.invoice_total = self.sum_line_item_totals(self.line_items)


    @staticmethod
    def add_li_to_einvoice(_line_items,_line_item):
        """Take a line_item and add it to List of line_items[]"""
        log.info("Adding a line item to the invoice: %s", str(_line_item))
        _line_items.append(_line_item)
        print(_line_items)
        return _line_items


    def write_einovice_to_json(_einvoice,filename='einvoice.json'):
        """Writes the e-Inovice to a JSON file."""
        json_str = dumps(_einvoice.__dict__)
        with open(filename, 'w') as output:
            output.write(json_str)
