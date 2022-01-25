#!/usr/bin/env python3
#
# File: discovery_message_package.py
# About: Dataclass definition of an discovery message package
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-17 (October 17, 2021)
#
""" Dataclass Object to define the e-invoice message package."""

from dataclasses import dataclass
from einvoice.discovery.urn import Urn
from einvoice.discovery.semantic_model import EInvoice


@dataclass
class EinvoiceMessagePackageP():
    """Class defining the einvoice message package"""

    einvoice_urn: Urn
    einvoice_invoice: EInvoice
