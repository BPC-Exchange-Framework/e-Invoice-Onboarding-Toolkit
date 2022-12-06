#!/usr/bin/env python3
#
# pylint: disable=R0902
# Too many instance attributes
# File: accessor.py
# About: SML and SMP discovery
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-28 (October 28th, 2021)
#
"""Module created to execute sml/smp look-up e-to-e."""
from einvoice.discovery.dns_query import DNSQuery
from einvoice.discovery.capture_dns_response import DNSResponse
from einvoice.discovery.smp_query import SMPQuery
from einvoice.discovery.urn_hasher import Hasher

LOGGER = __name__

class Accessor:
    """Class to define walk through of end-to-end processing.

    Args:
    NA

    Attributes:
    NA

    Returns:
    NA

    Raises:
    NA

    """

    def __init__(self):
        """Define values for an instance of the is class."""
        self.specification = None
        self.schema_id = None
        self.party_id = None
        self.sml_address = None
        self.sml_urn = None
        self.hash_action = None
        self.hashed_urn = None
        self.hash_dict = {}
        self.naptr_lookup = None
        self.smp_uri = None
        self.smp_api_call_1 = None
        self.smp_api_response_1 = None
        self.smp_api_call_2 = None
        self.smp_api_response_2 = None
        self.access_point_3_uri = None
        self.smp_service_group_url_response = None
        self.smp_service_url_response = None
        self.log = None

    def call_hash(self, specification, schema_id, party_id, log):
        """Hash the urn to obtain sml lookup value."""
        # Pull out the individual attributes from the urn object
        self.specification = specification
        self.schema_id = schema_id
        self.party_id = party_id
        self.hash_action = Hasher()
        self.hash_dict = self.hash_action.hasher(
            self.specification, self.schema_id, self.party_id, log
        )
        return self.hash_dict

    def call_dns_lookup(self, hashed_urn, domain, log):
        """Look-up NAPTR record in the DNS."""
        naptr_lookup = DNSQuery()
        naptr_writer = DNSResponse()
        naptr_response = naptr_lookup.naptr_lookup(hashed_urn, domain, log)
        naptr_writer.write_dns_response(naptr_response, log)
        return naptr_response

    def call_smp_service_group_url(self, urn, log):
        """Create smp service group url query."""
        smp_handler = SMPQuery()
        self.smp_service_group_url_response\
            = smp_handler.query_service_group_url(urn, log)
        return self.smp_service_group_url_response

    def call_smp_service_url(self, urn, log):
        """Create smp service group url query."""
        smp_handler = SMPQuery()
        self.smp_service_url_response = smp_handler.query_service_url(urn, log)
        return self.smp_service_url_response
