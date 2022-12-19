#!/usr/bin/env python3
# noqa: R0903
# File: discovery_message_package.py
# About: Dataclass definition of an discovery message package
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-17 (October 17, 2021)
#
"""Dataclass Object to define the e-invoice message package."""

from dataclasses import dataclass
from einvoice.discovery.urn import Urn


@dataclass
class EinvoiceMessagePackageP:                  # noqa: R0903
    """Class defining the einvoice message package."""

    einvoice_urn: Urn
