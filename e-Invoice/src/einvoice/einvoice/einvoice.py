#!/Users/kelly/Dev/virtualenvs/e-Invoice/bin python

# Author: Kelly Kinney
# Date: 2021-06-20 (June 20, 2021)
# File: einvoice.py
# About: Class definition of an einvoice object.  Based on
# Notes: chmod 755 create_dev_struct.sh in order to execute.
#
# LICENSE
# Copyright (C) 2021 Kelly Kinney
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# A copy of the GNU General Public License is included in the GitHub
# repository root which contained this file.
# If not, see <http://www.gnu.org/licenses/>.
"""The classes and functions which define a prototype e-Invoice.

This is a model definitiontion of an e-Inoice which can be used in a four
corners distrubuted e-services implementation.

    Usage:
    my_einvoice = einvoice()
"""
import json
from uuid import uuid1
from datetime import datetime


class Address:

    def __init__(self):
        self.OrgID = ''     # Unique Identifier for Organiazation (a PK)
        self.name = ''     # A common name for the Org (to go on an address)
        self.addr_1 = ''    # Address Line 1
        self.addr_2 = ''    # Address line 2                                                                                                                                                                                             dr_2 = ''           # Address Line 2
        self.city = ''      # Address city
        self.state = ''     # Address state
        self.zip = ''       # Address zip
"""An object representing a physical address.

Used to store the address of the buyer and seller.

Args:
    OrgID:
        A unique identifier to reference the Address object.  Default
        value is empty.
    name:
        A common name for the business of Address owner.  Default
        value is empty.
    addr_1:
        Address line #1 (usually Attn:).  Default value is empty.
    addr_2:
        Adresss line #2 (usually street address). Default value
        is empty.
    city:
        The city where the business address is located. Default
        value is empty.
    state:
        The state where the business address is located. Default
        value is empty.
    zip:
        The zop code where the business address is located. Default
        value is empty.

Returns:

Raises:
"""


class LineItem:

    def __init__(self):
        self.LIID = ''       # A unique idenitifier for an invoice item,
        self.LIQty = 0       # Quantity of items.
        self.LIPerItem = ''  # Units of measure of item, e.g., individual, bundle,  roll, etc.
        self.LIPPI = 0       # Price Per Item
        self.LIName = ''     # Short name of goods or services sold (2-3 words)
        self.LIDesc = ''           # Additional details to differentiate the item if necessary.

        def calculateLITotal(LIQty, LIPPI):
            """Calculates the total list item value multiplying the ListItem
            quantity by the ListItem price."""
            return (LIQty * LIPPI)

        self.LITotal = calculateLITotal()       # The line item total.
"""Represents a single line item on an invoice.

An e-Invoice will contain 1-n LineItem objects.

Args:
    LIID:
        A unique identifier for the LineItem.  Default value is empty.
    LIQty:
        Quantity of items covered by this line item.  Default value
        is 0.
    LIPerItem:
        Units of measure of the item., e.g., individiaul, bundle
        roll, etc. Default value is empty.
    LIPPI:
        Per per item.  Default value is 0.
    LIName:
        Short name of items sold. Default value is empoty.
    LIDesc:
        Additional descriptive details to differentiate the item.
        Default value is empy.
    LITotal:
        The line item total cost. This is calculated as LIQty * LIPPI.
        Default value is empty.

Returns:

Raises:
"""


class UniqueIdentifier:

    def __init__(self):
        self.InvUID = uuid.uuid1()
        return(self.InvUID)
"""Generates a unique identifier for an invoice.

Call uuid1() method to obtain a unique identifier for the e-Invoice.

Args:
    InvUID: The unique identifier of the e-Invoice to be generated.

Returns:
    UniqueIdentifier: The unique identifier of the e-Invoice object.

Raises:
"""

class  eInvoice:


    def __init__(self):
        self.InvUID = UniqueIdentifier()
        self.invDate = datetime.now().strftime("%Y-%m-%d")     # Invoice date
        self.SAddr = Address()           # Address instance for the Seller.
        self.BAddr = Address()           # Address instance for the Buyer.
        LineItems = []             # Create an empty list to contain line items.

        def AddItemToEInvocie(_LineItems,_LineItem):
            """Take a LineItem and add it to List of LineItems[]"""
            _LineItems.append(_LineItem)
            print(_LineItems)
            return (_LineItems)

        def CalcLineItemTotal(LineItems):
            """Caluculate the sum of all LineItem objects in the
             List of LineItems[]"""
            total = sum(item.LITotal for item in LineItems)
            return(total)


        self.InvoiceTotal = CalcLineItemTotal(LineItems)   # Total value of
                                                        # all items on invoice

        # def writeEInvoiceXML(eInvoice):

        def writeEInvoiceJSON(eInvoice,fn='eInvoice.json'):
            """Writes the e-Inovice to a JSON file."""
            jsonStr = json.dumps(eInvoice.__dict__)
            with open(fn, 'w') as output:
                output.write(jsonStr)
"""Represents an e-Inovice object.

Args:
    InvUID:
        UniqueIdentifier created from UniqueIdentifier
        class as a String,
    InvDate:
        The date of the Invoice expressed as a Sting.
    SAddr:
        Seller's place of busines as an Address() object.
    BAddr:
        Buy's place of business as an Address() object.
    LineItems[]:
        An array of LineItem() objects.
    InvoiceTotal:
        A flost representing the total cost of all LineItems

Returns:

Raises:
"""
