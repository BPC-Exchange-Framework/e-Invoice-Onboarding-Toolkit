#!/usr/bin/env python3
#
# pylint: disable=R0902
# Too many instance attributes
# File: accesspr.py
# About: SML and SMP discovery
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-28 (October 28th, 2021)
#
"""Module created to execute sml/smp look-up e-to-e."""
from einvoice.discovery.dns_query import DNSQuery
from einvoice.discovery.smp_query import SMPQuery
from einvoice.discovery.urn_hasher import Hasher
from einvoice.discovery.app_logging import create_logger


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
        self.log = create_logger("implementation")

    # def create_urn(self, specification, schema_id, party_id):
    #     """Construct a sml_urn from values provided."""
    #     self.sml_urn = Urn(specification, schema_id, party_id)
    #     return self.sml_urn

    def call_hash(self, specification, schema_id, party_id):
        """Hash the urn to obtain sml lookup value."""
        # Pull out the individual attrributes from the urn object
        self.specification = specification
        self.schema_id = schema_id
        self.party_id = party_id
        self.hash_action = Hasher()
        self.hash_dict = self.hash_action.hasher(self.specification,
                                                 self.schema_id,
                                                 self.party_id)
        return self.hash_dict

    def call_dns_lookup(self, hashed_urn, domain):
        """Look-up NAPTR record in the DNS."""
        self.naptr_lookup = DNSQuery()
        self.smp_uri = self.naptr_lookup.naptr_lookup(hashed_urn,
                                                      domain)
        return self.smp_uri

    def call_smp_service_group_url(self, urn):
        """Create smp service group url query."""
        smp_handler = SMPQuery()
        self.smp_service_group_url_response = smp_handler.\
            query_service_group_url(urn)
        return self.smp_service_group_url_response

    def call_smp_service_url(self, urn):
        """Create smp service group url query."""
        smp_handler = SMPQuery()
        self.smp_service_url_response = smp_handler.\
            query_service_url(urn)
        return self.smp_service_url_response

    # if __name__ == "__main__":
    #     urn = create_urn(specification="urn:oasis:"
    #                                    "names:tc:ebcore:partyid-"
    #                                    "type:unregistered:myscheme",
    #                      schema_id="BPC01",
    #                      party_id="bpcBusid01")
    #     urn_dict = hash_urn(urn)
    #     smp_uri = naptr_dns_lookup(urn_dict["urn_hash"], domain="sc-b2b.us")
    #     access_point_3_uri = smp_handler()
