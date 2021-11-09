#!/usr/bin/env python3
# pylint: disable=R0903, W1203
# Too fw public methods, use lazy formating.
# File: dns_query.py
# About: Discovery of smp from dns query
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-27 (October 27th, 2021)
#
"""Queries DNS services for NAPTR records"""
from dns.resolver import resolve
from einvoice.app_logging import create_logger


class DNSQuery:
    """Class to handle dns query/naptr look-up of hashed urn."""

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        self.naptr_record = None
        self.lookup_response = None
        self.smp_uri = None
        self.log = create_logger("DNSQuery")

    def naptr_lookup(self, urn, domain):
        """Module to do the naptr dns query/look-up."""
        self.naptr_record = urn + domain
        self.log.info(f"Look-up for urn: {self.naptr_record}")
        self.lookup_response = dict[resolve(self.naptr_record,
                                                     'NAPTR')]
        for answer in self.lookup_response.rrset:
            self.smp_uri = answer.regexp
            self.smp_uri = self.smp_uri.decode()
        return self.smp_uri
