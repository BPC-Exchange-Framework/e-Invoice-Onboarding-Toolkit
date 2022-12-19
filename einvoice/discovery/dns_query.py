#!/usr/bin/env python3
# pylint: disable=R0903, W1203, W1309, R0915
# Too few public methods, use lazy formatting,
# f string without interpolated value error is false.
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


class DNSQuery:
    """Class to handle dns query/naptr look-up of hashed urn."""

    def __init__(self):
        """Entry point for the module.  Defines instance variables."""
        self.naptr_record = None
        self.lookup_response = None
        self.smp_uri = None
        self.rrset_dict = {
            "order": None,
            "preference": None,
            "flags": None,
            "service": None,
            "regexp": None,
            "replacement": None
        }
        self.dns_response = DNSResponse()

    def naptr_lookup(self, urn, domain, log):
        """Execute the naptr dns query/look-up."""
        self.naptr_record = urn + "." + domain
        # log.info(f"Look-up for urn: {self.naptr_record}")
        # Now let's look it up in the DNS system
        self.lookup_response = dns.resolver.resolve(self.naptr_record, "NAPTR")
        rrset_data = self.lookup_response.rrset.to_text()
        log.info(
            f"Response from dns query: {rrset_data}"
            )
        # Take a look at what this object type is.  That's half the battle in
        # understanding how to make sense of this object.
        # https://dnspython.readthedocs.io/en/latest/resolver-class.html
        # data = self.dns_response.get_dns_data(self.lookup_response.rrset)
        # self.dns_response.write_dns_response(data)
        for answer in self.lookup_response.rrset:
            # log.info(f"Inside answer loop: {answer}")
            # Interesting to see all the values brought back by the naptr query
            # but we only care about the regexp field
            # self.rrset_dict["Name"] = answer.Name
            self.rrset_dict['order'] = answer.order
            order_type = type(self.rrset_dict['order'])
            log.info(
                "Type dictionary item 'order' is: %s", order_type
                )
            log.info(
                f"order value of response: {answer.order}"
                )
            log.info(
                f"dict value of order: {self.rrset_dict['order']}"
                )
            response_valid = (answer.order == self.rrset_dict['order'])
            log.info(
                "Order value in response and in rrset_dict are the same:  " +
                "%s", response_valid
                        )

            self.rrset_dict['preference'] = answer.preference
            log.info(
                f"preference value of response: {answer.preference}"
                )
            log.info(
                f"dict value of preference: {self.rrset_dict['preference']}"
                )
            response_valid = (answer.preference ==
                              self.rrset_dict['preference'])
            log.info(
                "Preference value in response and " +
                "in rrset_dict are the same: " +
                "%s", response_valid
                )

            self.rrset_dict['flags'] = answer.flags.decode('utf-8')
            log.info(
                f"flags value of response: {answer.flags}"
                )
            log.info(
                f"dict value of flags: {self.rrset_dict['flags']}"
                )
            response_valid = (answer.flags.decode('utf-8') ==
                              self.rrset_dict['flags'])
            log.info(
                "flags value in response and in rrset_dict are the same: "
                "%s", response_valid
                )

            if self.rrset_dict['flags'] != "U":
                log.setLevel(logging.ERROR)
                msg = (
                    "The DNS NAPTR record FLAG " +
                    "value is not set to 'U'."
                )
                log.error(msg)
                msg = (
                    "The DNS record does not " +
                    "support output of the REGEXP field."
                )
                log.error(msg)
                msg = "Further URI processing is not possible."
                log.error(msg)
                msg = "See: https://www.rfc-editor.org/rfc/rfc2915."
                log.error(msg)
                log.setLevel(logging.INFO)

            self.rrset_dict['service'] = answer.service.decode('utf-8')
            log.info(
                f"service value of response: {answer.service}"
                )
            log.info(
                f"dict value of service: {self.rrset_dict['service']}"
                )
            response_valid = (answer.service.decode('utf-8') ==
                              self.rrset_dict['service'])
            log.info(
                "Service value in response and in rrset_dict are the same: "
                "%s", response_valid
                )

            self.rrset_dict['regexp'] = answer.regexp.decode('utf-8')
            log.info(
                f"regexp value of response: {answer.regexp}"
                )
            log.info(
                f"dict value of regexp: {self.rrset_dict['regexp']}"
                )
            response_valid = (answer.service.decode('utf-8') ==
                              self.rrset_dict['regexp'])
            log.info(
                "Regexp value in response and in rrset_dict are the same:  "
                "%s", response_valid
                )

            self.rrset_dict['replacement'] = answer.replacement.to_text()
            log.info(
                f"replacement value of response: {answer.replacement}"
                )
            log.info(
                f"dict value of replacement: {self.rrset_dict['replacement']}"
                )
            response_valid = (answer.replacement ==
                              self.rrset_dict['replacement'])
            log.info(
                "Replacement value in response " +
                "and in rrset_dict are the same: "
                "%s", response_valid
                )

            # log.info(f"This is the rrset_dict {self.rrset_dict}")
            # self.smp_uri = answer.regexp
            # self.smp_uri = self.smp_uri.decode()
        # Compile a regex pattern of the junk we need to strip
        # off the front side
        log.info(
                f"The naptr response as a dict: {self.rrset_dict}"
                )
        pattern = re.compile(r"\!\^\.\*\$\!")
        # Strip the front side junk from the uri
        self.smp_uri = re.sub(pattern, "", self.rrset_dict['regexp'])
        # Strip off the trailing bang "!" at the end of the uri.
        self.smp_uri = self.smp_uri.replace("!", "")
        return self.smp_uri, self.rrset_dict
