#!/usr/bin/env python3
# pylint: disable=W0613
# unused arguments
# File: smp_query.py
# About: Query SMP REST API.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
""""Provides functionality for an SMPQuery 4-corner
discovery"""
class SMPQuery:
    """Class to create and execute a RESt API query.
    See the ebXML standards for request API format."""

    def __init__(self):
        self.party_id = None
        self.smp_uri = None
        self.query_1 = None
        self.query_1_response = None
        self.query_2 = None
        self.query_2_response = None

    def smp_create_query_1(self, party_id):
        """Function to create first smp api query"""

        return self.query_1

    def smp_execute_query_1(self, query_1, smp_uri):
        """Function to execute first smp api query"""

        return self.query_1_response

    def smp_create_query_2(self, query_1_response):
        """Function to create second smp api query"""

        return self.query_2

    def smp_execute_query_2(self, query_2, smp_uri):
        """Function to execute second smp api query"""

        return self.query_2_response
