#!/usr/bin/env python3

from http.client import NotConnected
from einvoice.smp_query import SMPQuery
from urn import Urn
from urn_hasher import Hasher
from app_logging import create_logger
from smp_query import SMPQuery


class Implementation:
    """Class to define walk through of end-to-end processing.
    
        Args:

        Attributes:

        Returns: 

        Raises:

    """

    def __init__(self):
        """Entry point for an instance of the is class."""
        self.specification = None
        self.schema_id = None
        self.party_id = None
        self.sml_address = None
        self.sml_urn = None
        self.hash_action = None
        self.hashed_urn = None
        self.urn_dict = None
        self.NAPTR_dns_lookup = None
        self.smp_uri = None
        self.smp_api_call_1 = None
        self.smp_api_response_1 = None
        self.smp_api_call_2 = None
        self.smp_api_response_2 = None
        self.access_point_3_uri = None
        self.log = create_logger("implementation")

    def create_urn(self, specification, schema_id, party_id):
        """Construct a sml_urn from values provided."""
        self.sml_urn = Urn()
        self.sml_urn.specification = specification
        self.sml_urn.schema_id = schema_id
        self.sml_urn.party_id = party_id
        return self.sml_urn.urn

    def hash_urn(self, urn):
        """Hash the urn to obtain sml lookup value"""
        self.urn = urn
        self.hash_action = Hasher()
        self.urn_dict = self.hash_action.hasher(self.urn.specification,
                                                self.urn.schema_id,
                                                self.party_id)
        return self.urn_dict

    def NAPTR_dns_lookup (self, hashed_urn):
        """Look-up NAPTR record in the DNS"""

        return self.smp_uri

    def smp_handler(self):
        """Create handler for SMP tasks"""
        smp_query_handler = SMPQuery

        
        return self.access_point_3_uri

    def query_smp_api_call_1(self):
        """Execute first SMP API query"""

        return self.smp_api_response_1

    def create_smp_api_request_2(self):
        """Create second SMP API query"""

        return self.smp_api_call_2

    def query_smp_api_call_2(self):
        """Execute second SMP API query"""

        return self.smp_api_response_2


    if __name__ == "__main__":
        self.urn = create_urn(specification, schema_id, party_id)
        self.urn_dict = hash_urn(self.urn)
        self.smp_uri = NAPTR_dns_lookup(self.urn_dict["urn_hash"])
        smp_api_ca11_1 = create_smp_api_request_1()
        smp_api_response_1 = query_smp_api_call_1(smp_uri, smp_api_call_1)
        smp_api_call_2 = create_smp_api_request_2(smp_api_response_1)
        smp_api_response_2 = query_smp_api_call_2(smp_uri, smp_api_call_2)
