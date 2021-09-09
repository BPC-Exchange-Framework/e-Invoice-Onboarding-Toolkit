#!/usr/bin/env python3
#
# File: cert_config.py
# About: File with values for certificate creation.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-09-06 (September 6, 2021)
#
import os
from os.path import join, dirname
from dotenv import load_dotenv
""" This loads values from .env.

"""
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

CERT_CONFIG = {
    "public_exponent": os.getenv("PUBLIC_EXPONENT"),
    "key_size": os.getenv("KEY_SIZE"),
    "backend": os.getenv("BACKEND"),
    "subject_cn": os.getenv("SUBJECT_COMMON_NAME"),
    "issuer_cn": os.getenv("ISSUER_COMMON_NAME"),
    "dns_name":  os.getenv("DNS_NAME"),
    "subject_org_name":  os.getenv("SUBJECT_ORGANIZATION_NAME"),
    "subject_ou": os.getenv("SUBJECT_ORGANIZATIONAL_UNIT_NAME"),
    "ca_private_key_file_name": os.getenv("PRIVATE_KEY_FILE_NAME"),
    "ca_public_key_file_name": os.getenv("PUBIC_KEY_FILE_NAME")
}
