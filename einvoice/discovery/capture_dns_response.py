#!/usr/bin/env python3
# pylint: disable=R0903, W1203
# Too few public methods, use lazy formatting.
# File: capture_dns_response.py
# About: Capture the DNS response
# Development: Kelly Kinney
# Date: 2022-11-20 (November 20th, 2022)
#
"""Writes DNS response for NAPTR query to file."""
import os
from os.path import join, dirname
from json import dumps
from datetime import datetime
from dotenv import load_dotenv

LOGGER = __name__

class DNSResponse:
    """Class to write response from DNS query to file."""

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        dotenv_path = join(dirname(__file__), "../../.env")
        load_dotenv(dotenv_path)
        self.date_obj = datetime.now()
        self.dns_response = None
        self.dns_list = []
        self.dns_dict = {}
        self.output_file = str(os.getenv("DNS_RESPONSE_FILE"))
        self.log = None

    def write_dns_response(self, dns_response, logger):
        """Write the urn values to a file."""
        self.log = logger
        date_fmt  = self.date_obj.strftime("%Y%m%d%H%M%S")
        self.output_file = self.output_file + "_" + date_fmt + ".json"
        self.log.info(f"Writing out DNS response to file {self.output_file}")
        self.dns_dict = dns_response
        self.log.info(f"This is the raw input {self.dns_dict}")
        self.log.info(f"Writing the DNS response to file.{self.dns_dict}")
        json_str = dumps(self.dns_dict)
        with open(self.output_file, "w", encoding="utf-8") as output:
            output.write(json_str)
