#!/usr/bin/env python3
#
# File: einvoice_message_package.py
# About: Dataclass definition of an einvoice message package
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-17 (October 17, 2021)
#
""" Dataclass Object to define the e-invoice message package."""

from einvoice.urn import Urn

@dataclass
class EinvoiceMessagePackageP():
    """Class defining the einvoice message package"""

    einvoice_urn: Urn
    einvoice_invoice: obj

