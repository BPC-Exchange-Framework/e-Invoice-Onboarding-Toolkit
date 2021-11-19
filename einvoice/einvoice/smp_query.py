#!/usr/bin/env python3
# pylint: disable=W0613, W1203. R0902
# unused arguments, use of lazy % formating,
# too many instance attributes
# File: smp_query.py
# About: Query SMP REST API.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
#
""""Provides functionality for an SMPQuery 4-corner
discovery"""
import re
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from einvoice.app_logging import create_logger


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
        dotenv_path = join(dirname(__file__), './.env')
        load_dotenv(dotenv_path)
        self.protocol = str(os.getenv("PROTOCOL"))
        self.standard = str(os.getenv("STANDARD"))
        self.service_id = str(os.getenv("SERVICE_ID"))
        self.services = str(os.getenv("SERVICES"))
        self.domain = str(os.getenv("DOMAIN"))
        self.log = create_logger("smp_query")
        self.request_url = None
        self.urn = None
        self.smp_uri = None
        self.srvc_grp_url_qry = None
        self.srvc_grp_url_reply = None
        self.srvc_url_qry = None
        self.srvc_url_reply = None
        self.response = None

    def query_service_group_url(self, urn):
        """Make required calls to the SMP to obain service group url info."""
        self.urn = urn
        self.srvc_grp_url_qry = self.smp_create_srvc_group_url_query(self.urn)
        self.srvc_grp_url_reply = self.smp_execute_qry(self.srvc_grp_url_qry)
        self.log.info(f"Service group url response: {self.srvc_grp_url_reply}")
        return self.srvc_grp_url_reply

    def query_service_url(self, urn):
        """Make required calls to the SMP to obain service url info."""
        self.urn = urn
        self.srvc_url_qry = self.smp_create_service_url_query(self.urn)
        self.srvc_url_reply = self.smp_execute_qry(self.srvc_url_qry)
        self.log.info(f"Service group url response: {self.srvc_url_reply}")
        return self.srvc_url_reply

    def smp_create_srvc_group_url_query(self, urn):
        """Create first smp api query."""
        self.urn = urn
        self.request_url = (self.protocol + "://" + self.domain + "/" +
                            self.standard + "/" + self.urn)
        self.request_url = re.sub(":", "%3A", self.request_url)
        self.request_url = re.sub("https%3A", "https:", self.request_url)
        self.log.info(f"Service group url created: {self.request_url}")
        return self.request_url

    def smp_create_service_url_query(self, urn):
        """Create second smp api query."""
        self.urn = urn
        self.request_url = (self.protocol + "://" + self.domain + "/" +
                            self.standard + "/" + self.urn + "/" +
                            self.services + "/" + self.service_id)
        self.request_url = re.sub(":", "%3A", self.request_url)
        self.request_url = re.sub("#", "%23", self.request_url)
        self.request_url = re.sub("https%3A", "https:", self.request_url)
        self.log.info(f"Service url created: {self.request_url}")
        return self.request_url

    def smp_execute_qry(self, url):
        """Execute an api query."""
        self.response = requests.get(url)
        return self.response.text
