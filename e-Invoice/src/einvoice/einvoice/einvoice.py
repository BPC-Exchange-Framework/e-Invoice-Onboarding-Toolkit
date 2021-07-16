#!/usr/bin/env python3
#
# File: einvoice.py
# About: Class definition of an einvoice object.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
# LICENSE
# Copyright (C) 2021 Business Payments Coalition
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""The classes and functions which define a prototype e-Invoice.

This is a model definition of an e-Inoice which can be used in a four
corners distrubuted e-services implementation.

    Usage:
    my_einvoice = einvoice()
"""
from dataclasses import dataclass
from datetime import datetime
from json import dumps
from uuid import uuid4
import logging



# Create a logger instance.
# NOTE: This is a baseline logger to implement core fucntionality.
# It would desireable to externalize this config so it can be
# utilized by multiple apps.
FORMAT='%(asctime)s - $(levelname)s - $(funcName)s - $(message)s'
DATEFMT='%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(format=FORMAT, datefmt=DATEFMT, level=logging.INFO)


@dataclass
class Address:
    """A dataclass representing a physical address.

    Used to store the address of the buyer and seller.

    Args:

    Attributes:
        org_id: str
            A unique identifier to reference the Address object.  Default
            value is undefined.
        name: str
            A common name for the business of Address owner.  Default
            value is undefined.
        addr_1: str
            Address line #1.  Default value is undefined.
        addr_2: str
            Adresss line #2. Default value is undefined.
        city: str
            The city where the business address is located. Default
            value is undefined.
        state: str
            The state where the business address is located. Default
            value is undefined.
        zip: str
            The zip code where the business address is located. Default
            value is undefined.

    Returns:

    Raises:
    """
    org_id: str
    name: str
    addr_1: str
    addr_2: str
    city: str
    state: str
    zip: str


@dataclass
class LineItem:
    """Dataclass which represents a single line item on an invoice.

    An e-Invoice will contain 1-n LineItem objects.

    Args:

    Attributes:
        li_id: str
            A unique identifier for the LineItem.  Default value is undefined.
        li_per_item: str
            Units of measure of the item., e.g., individiaul, bundle roll, etc.
            Default value is undefined.
        li_name: str
            Short name of items sold. Default value is undefined.
        li_desc: str
            Additional descriptive details to differentiate the item.
            Default value is undefined.
        li_qty: int
            Quantity of items covered by this line item.  Default value is 0.
        li_ppi: float
            The price per item in dollars and cents (two decimal
            places).  Default value is 0.
        li_total: float
            The line item total cost. This is calculated as li_qty * li_ppi.

    Returns:

    Raises:
    """
    li_id: str
    li_per_item: str
    li_name: str
    li_desc: str
    li_qty: int = 0
    li_ppi: float = 0

    def li_total(self) -> float:
        """Compute line item total."""
        return self.li_qty * self.li_ppi


class  EInvoice:
    """Represents an e-Inovice object.

    Args:

    Attributes:
        inv_uuid:
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

    @staticmethod
    def sum_ei_lineitem_totals(_line_items):
        """Sum all line items for an invoice total."""
        line_item_total = 0
        for obj in _line_items:
            line_item_total = line_item_total + obj.li_total
        return line_item_total


    def __init__(self):
        logging.info("Creating an e-Invoice")
        self.ei_uuid = str(uuid4())
        self.ei_date = datetime.now().strftime("%Y-%m-%d")
        self.ei_seller_address = Address()
        self.ei_buyer_address = Address()
        self.ei_line_items = [LineItem] # Line Items is list of LineITem
        self.ei_invoice_total = self.sum_ei_lineitem_totals(self.ei_line_items)


    @staticmethod
    def add_li_to_einvoice(_line_items,_line_item):
        """Take a line_item and add it to List of line_items[]"""
        logging.info("Adding a line item to the invoice: %s", str(_line_item))
        _line_items.append(_line_item)
        print(_line_items)
        return _line_items


def write_einovice_to_json(_einvoice,filename='einvoice.json'):
    """Writes the e-Inovice to a JSON file."""
    json_str = dumps(_einvoice.__dict__)
    with open(filename, 'w') as output:
        output.write(json_str)
