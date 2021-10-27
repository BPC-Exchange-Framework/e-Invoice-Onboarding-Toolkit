#!/usr/bin/env python3
#
# File: line_item.py
# About: Dataclass definition of a line item in an einvoice.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-06-20 (June 20, 2021)
#
"""The dataclass definition of a line items in an einvoice.

This is a model defined for a line item of in
an e-Invoice which can be used in a four
corners distributed e-services implementation.

    Usage:
    my_line_item = LineItem()
"""
from dataclasses import dataclass


@dataclass
class LineItem:
    """Dataclass which represents a single line item on an invoice.

    An e-Invoice will contain 1-n LineItem objects.

    Args:

    Attributes:
        line_item_id: str
            A unique identifier for the LineItem.  Default value is undefined.
        line_item_per: str
            Units of measure of the item., e.g., individual, bundle roll, etc.
            Default value is undefined.
        line_item_name: str
            Short name of items sold. Default value is undefined.
        line_item_description: str
            Additional descriptive details to differentiate the item.
            Default value is undefined.
        line_item_quantity: int
            Quantity of items covered by this line item.  Default value is 0.
        line_item_price_per_item: float
            The price per item in dollars and cents (two decimal
            places).  Default value is 0.
        line_item_total: float
            The line item total cost.
            This is calculated as
            line_item_quantity * line_item_price_per_item.

    Returns:

    Raises:
    """

    line_item_id: str
    line_item_per: str
    line_item_name: str
    line_item_description: str
    line_item_quantity: int = 0
    line_item_price_per_item: float = 0

    def line_item_total(self) -> float:
        """Compute line item total."""
        return self.line_item_quantity * self.line_item_price_per_item
