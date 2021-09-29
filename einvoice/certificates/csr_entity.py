#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913
# Too many instance attributes, Too many arguments
# File: csr_entity.py
# About: Definition of a csr data entity
# Development: Kelly Kinney
# Date: 2021-09-16 (September 16, 2021)
#
"""This dataclass entity contains basis information required to complete
a csr.

"""
from dataclasses import dataclass


@dataclass
class CertificateSigningRequest():
    """A dataclass representing elements required for a certificate
    signing """

    subject_name: str
    country_name: str
    state_or_province_name: str
    locality_name: str
    organization_name: str
    common_name: str
    alternate_dns_name_1: str
    alternate_dns_name_2: str
    alternate_dns_name_3: str
