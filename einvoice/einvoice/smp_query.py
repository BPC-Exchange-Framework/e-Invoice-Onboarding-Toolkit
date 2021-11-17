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
    See the ebXML standards for request API format.

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
        self.smp_uri = None
        self.query_1 = None
        self.query_1_response = None
        self.query_2 = None
        self.access_point_3 = None

    def get_access_point_3(self, uri):
        """Make required calls to the SMP to obain access point 3 endpoint."""

        self.query_1 = self.smp_create_query_1()
        self.query_1_response = self.smp_execute_query_1(self.query_1, uri)
        self.query_2 = self.smp_create_query_2(self.query_1_response)
        self.access_point_3 = self.smp_execute_query_2(self.query_2, uri)
        return self.access_point_3

    def smp_create_query_1(self):
        """Create first smp api query."""
        self.query_1 = "some query"
        return self.query_1

    def smp_execute_query_1(self, query_1, smp_uri):
        """Execute first smp api query."""
        self.query_1_response = f"results of {query_1} against {smp_uri}"
        return self.query_1_response

    def smp_create_query_2(self, query_1_response):
        """Create second smp api query."""
        self.query_2 = f"make another query from {query_1_response}"
        return self.query_2

    def smp_execute_query_2(self, query_2, smp_uri):
        """Execute second smp api query."""
        self.access_point_3 = f"results of {query_2} against {smp_uri}"
        return self.access_point_3
