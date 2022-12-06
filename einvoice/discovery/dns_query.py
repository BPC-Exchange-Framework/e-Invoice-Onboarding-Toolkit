#!/usr/bin/env python3
# pylint: disable=R0903, W1203, W1309
# Too few public methods, use lazy formatting, f string without interpolated value error is false.
# File: dns_query.py
# About: Discovery of smp from dns query
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-10-27 (October 27th, 2021)
#
"""Queries DNS services for NAPTR records."""
import re
import logging
import dns.resolver
from einvoice.discovery.capture_dns_response import DNSResponse

LOGGER = __name__

class DNSQuery:
    """Class to handle dns query/naptr look-up of hashed urn."""

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        self.naptr_record = None
        self.lookup_response = None
        self.smp_uri = None
        self.rrset_dict = {
            "order" : None,
            "preference" : None,
            "flags" : None,
            "service": None,
            "regexp" : None,
            "replacement" : None
        }
        self.log = None
        self.dns_response = DNSResponse()

    def naptr_lookup(self, urn, domain, logger):
        """Execute the naptr dns query/look-up."""
        self.log = logger
        self.naptr_record = urn + "." + domain
        # self.log.info(f"Look-up for urn: {self.naptr_record}")
        # Now let's look it up in the DNS system
        self.lookup_response = dns.resolver.resolve(self.naptr_record, "NAPTR")
        self.log.info(f"Response from dns query: {self.lookup_response.rrset.to_text()}")
        # Take a look at what this object type is.  That's half the battle in
        # understanding how to make sense of this object.
        # https://dnspython.readthedocs.io/en/latest/resolver-class.html
        # data = self.dns_response.get_dns_data(self.lookup_response.rrset)
        # self.dns_response.write_dns_response(data)
        for answer in self.lookup_response.rrset:
            # self.log.info(f"Inside answer loop: {answer}")
            # Interesting to see all the values brought back by the naptr query
            # but we only care about the regexp field
            # self.rrset_dict["Name"] = answer.Name
            self.rrset_dict['order'] = answer.order
            self.log.info(f"Type dictionary item 'order' is: {type(self.rrset_dict['order'])}")
            self.log.info(f"order value of response: {answer.order}")
            self.log.info(f"dict value of order: {self.rrset_dict['order']}")
            self.log.info(f"Order value in response and in rrset_dict are the same:  "
                          "{(answer.order == self.rrset_dict['order'])}")

            self.rrset_dict['preference'] = answer.preference
            self.log.info(f"preference value of response: {answer.preference}")
            self.log.info(f"dict value of preference: {self.rrset_dict['preference']}")
            self.log.info(f"Preference value in response and in rrset_dict are the same: "
                "{(answer.preference == self.rrset_dict['preference'])}")

            self.rrset_dict['flags'] = answer.flags.decode()
            self.log.info(f"flags value of response: {answer.flags}")
            self.log.info(f"dict value of flags: {self.rrset_dict['flags']}")
            self.log.info(f"flags value in response and in rrset_dict are the same: "
                          "{(answer.flags.decode('utf-8') == self.rrset_dict['flags'])}")

            if self.rrset_dict['flags'] != "U":
                self.log.setLevel(logging.ERROR)
                msg = "The DNS NAPTR record FLAG value is not set to 'U'."
                self.log.error(msg)
                msg = "The DNS record does not support output of the REGEXP field."
                self.log.error(msg)
                msg = "Further URI processing is not possible."
                self.log.error(msg)
                msg = "See: https://www.rfc-editor.org/rfc/rfc2915."
                self.log.error(msg)
                self.log.setLevel(logging.INFO)

            self.rrset_dict['service'] = answer.service.decode()
            self.log.info(f"service value of response: {answer.service}")
            self.log.info(f"dict value of service: {self.rrset_dict['service']}")
            self.log.info(f"Service value in response and in rrset_dict are the same: "
                          "{(answer.service.decode('utf-8') == self.rrset_dict['service'])}")

            self.rrset_dict['regexp'] = answer.regexp.decode()
            self.log.info(f"regexp value of response: {answer.regexp}")
            self.log.info(f"dict value of regexp: {self.rrset_dict['regexp']}")
            self.log.info(f"Regexp value in response and in rrset_dict are the same:  "
                          "{(answer.regexp.decode('utf-8') == self.rrset_dict['regexp'])}")

            self.rrset_dict['replacement'] = answer.replacement.to_text()
            self.log.info(f"replacement value of response: {answer.replacement}")
            self.log.info(f"dict value of replacement: {self.rrset_dict['replacement']}")
            self.log.info(f"Replacement value in response and in rrset_dict are the same: "
                          "{(answer.replacement.to_text() == self.rrset_dict['replacement'])}")

            # self.log.info(f"This is the rrset_dict {self.rrset_dict}")
            # self.smp_uri = answer.regexp
            # self.smp_uri = self.smp_uri.decode()
        # Compile a regex pattern of the junk we need to strip
        # off the front side
        self.log.info(f"The naptr response as a dict: {self.rrset_dict}")
        pattern = re.compile(r"\!\^\.\*\$\!")
        # Strip the front side junk from the uri
        self.smp_uri = re.sub(pattern, "", self.rrset_dict['regexp'] )
        # Strip off the trailing bang "!" at the end of the uri.
        self.smp_uri = self.smp_uri.replace("!","")
        return self.smp_uri, self.rrset_dict
