#!/usr/bin/env python3
#
# File: implementation.py
# About: SML and SMP discovery
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-28 (October 28th, 2021)
#
"""Module created to execute sml/smp look-up e-to-e."""
from http.client import NotConnected
from einvoice.smp_query import SMPQuery
from einvoice.urn import Urn
from einvoice.urn_hasher import Hasher
from einvoice.app_logging import create_logger
from einvoice.smp_query import SMPQuery


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
        self.sml_urn = Urn(specification, schema_id, party_id)
        return self.sml_urn

    def hash_urn(self, urn):
        """Hash the urn to obtain sml lookup value"""
        self.urn = urn
        self.hash_action = Hasher()
        self.urn_dict = self.hash_action.hasher(self.urn.specification,
                                                self.urn.schema_id,
                                                self.urn.party_id)
        return self.urn_dict

    def NAPTR_dns_lookup(self, hashed_urn):
        """Look-up NAPTR record in the DNS"""

        return self.smp_uri

    def smp_handler(self, party_id, uri):
        """Create handler for SMP tasks"""
        smp_query_handler = SMPQuery()
        self.smp_api_call_1 = smp_query_handler.\
            smp_create_query_1(self.party_id)
        self.smp_api_response_1 = smp_query_handler.\
            smp_execute_query_1(self.smp_api_call_1, self.smp_uri)
        self.smp_api_call_2 = smp_query_handler.\
            smp_create_query_2(self.smp_api_response_1)
        self.smp_api_response_2 = smp_query_handler.\
            smp_execute_query_2(self.smp_amp_call_2, self.smp_uri)
        self.access_point_3_uri = self.smp_api_response_2
        return self.access_point_3_uri

    if __name__ == "__main__":
        urn = create_urn(specification="urn:oasis:names:tc:ebcore:partyid-"
                                       "type:unregistered:myscheme",
                         schema_id="BPC01",
                         party_id="bpcBusid01")
        urn_dict = hash_urn(urn)
        smp_uri = NAPTR_dns_lookup(urn_dict["urn_hash"])
        access_point_3_uri = smp_handler(urn_dict.party_id, smp_uri)
