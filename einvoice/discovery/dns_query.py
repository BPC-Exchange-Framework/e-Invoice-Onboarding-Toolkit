#!/usr/bin/env python3
# pylint: disable=R0903, W1203
# Too fw public methods, use lazy formating.
# File: dns_query.py
# About: Discovery of smp from dns query
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-27 (October 27th, 2021)
#
"""Queries DNS services for NAPTR records."""
import re
import dns.resolver
from einvoice.discovery.app_logging import create_logger


class DNSQuery:
    """Class to handle dns query/naptr look-up of hashed urn."""

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        self.naptr_record = None
        self.lookup_response = None
        self.smp_uri = None
        self.log = create_logger("DNSQuery")

    def naptr_lookup(self, urn, domain):
        """Execute the naptr dns query/look-up."""
        self.naptr_record = urn + "." + domain
        self.log.info(f"Look-up for urn: {self.naptr_record}")
        # Now let's look it up in the DNS system
        self.lookup_response = dns.resolver.resolve(self.naptr_record, "NAPTR")
        # Take a look at what this object type is.  That's half the battle in
        # understanding how to make sense of this object.
        # https://dnspython.readthedocs.io/en/latest/resolver-class.html
        for answer in self.lookup_response.rrset:
            # Interesting to see all the values brought back by the naptr query
            # but we only care about the regexp field
            self.smp_uri = answer.regexp
            self.smp_uri = self.smp_uri.decode()
        # Compile a regex pattern of the junk we need to strip
        # off the front side
        pattern = re.compile(r"\!\^\.\*\$\!")
        # Strip the front side junk from the uri
        self.smp_uri = re.sub(pattern, "", self.smp_uri)
        # Strip off the trailing bang "!" at the end of the uri.
        self.smp_uri = re.sub(r"\!", "", self.smp_uri)
        return self.smp_uri
