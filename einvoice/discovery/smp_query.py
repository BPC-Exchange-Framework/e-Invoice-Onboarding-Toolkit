#!/usr/bin/env python3
# pylint: disable=W0613, W1203. R0902
# unused arguments, use of lazy % formatting,
# too many instance attributes
# File: smp_query.py
# About: Query SMP REST API.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-16 (July 16th, 2021)
"""Provides functionality for an SMPQuery Four-corner model discovery."""
import os
from os.path import join, dirname
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    import requests
from dotenv import load_dotenv

LOGGER = __name__

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
        """Define and instantiate variables."""
        dotenv_path = join(dirname(__file__), "../../.env")
        load_dotenv(dotenv_path)
        self.protocol = str(os.getenv("PROTOCOL"))
        self.standard = str(os.getenv("STANDARD"))
        self.service_id = str(os.getenv("SERVICE_ID"))
        self.services = str(os.getenv("SERVICES"))
        self.domain = str(os.getenv("DOMAIN"))
        self.log = None
        self.request_url = None
        self.urn = None
        self.smp_uri = None
        self.srvc_grp_url_qry = None
        self.srvc_grp_url_reply = None
        self.srvc_url_qry = None
        self.srvc_url_reply = None
        self.response = None

    def query_service_group_url(self, urn, logger):
        """Make required calls to the SMP to obtain service group url info."""
        self.log = logger
        self.urn = urn
        self.srvc_grp_url_qry = self.smp_create_srvc_group_url_query(self.urn, self.log)
        self.srvc_grp_url_reply = self.smp_execute_qry(self.srvc_grp_url_qry, self.log)
        self.log.info(f"Service group url response: {self.srvc_grp_url_reply}")
        return self.srvc_grp_url_reply

    def query_service_url(self, urn, logger):
        """Make required calls to the SMP to obtain service url info."""
        self.log = logger
        self.urn = urn
        self.srvc_url_qry = self.smp_create_service_url_query(self.urn, self.log)
        self.srvc_url_reply = self.smp_execute_qry(self.srvc_url_qry, self.log)
        self.log.info(f"Service group url response: {self.srvc_url_reply}")
        return self.srvc_url_reply

    def smp_create_srvc_group_url_query(self, urn, logger):
        """Create first smp api query."""
        self.log = logger
        self.urn = urn
        self.request_url = (
            self.protocol + "://" + self.domain +
            "/" + self.standard + "/" + self.urn
        )
        self.request_url = self.request_url.replace(":", "%3A")
        self.request_url = self.request_url.replace("https%3A", "https:")
        self.log.info(f"Service group url created: {self.request_url}")
        return self.request_url

    def smp_create_service_url_query(self, urn, logger):
        """Create second smp api query."""
        self.log = logger
        self.urn = urn
        self.request_url = (self.protocol + "://" + self.domain +
                            "/" + self.standard + "/" + self.urn +
                            "/" + self.services + "/" + self.service_id)
        self.request_url = self.request_url.replace(":", "%3A")
        self.request_url =self.request_url.replace("#", "%23")
        self.request_url = self.request_url.replace("https%3A", "https:")
        self.log.info(f"Service url created: {self.request_url}")
        return self.request_url

    def smp_execute_qry(self, url, logger):
        """Execute an api query."""
        self.log = logger
        self.response = requests.get(url, verify=False)
        self.log.info(f"SMP execute raw response: {self.response}")
        return self.response.content
    