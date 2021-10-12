#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913
# Too many instance attributes, Too many arguments
# File: create_keypair.py
# About:  Creates a private/public keypair
# Development: Kelly Kinney
# Date: 2021-10-04 (October 4, 2021)
#
"""This application will public/private keypair.

"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from certificates.cert_logging import create_logger


class CreateKeypair:
    """Class to create a public/private"""

    def __init__(self):
        """Entry point for the app."""
        self.private_key = None
        self.public_key = None

    def create_private_key(self):
        """Create a private key"""
        log = create_logger("create_private_key")
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)
        pub_exp = int(os.getenv("PUBLIC_EXPONENT"))
        key_size = int(os.getenv("KEY_SIZE"))
        public_exponent = int(pub_exp)
        key_size = int(key_size)
        self.private_key = rsa.generate_private_key(public_exponent, key_size,
                                                    backend=default_backend())
        log.info("Created private key")
        return self.private_key

    def create_public_key(self, private_key):
        """Create a public key using a private key"""
        log = create_logger("create_public_key")
        self.public_key = private_key.public_key()
        log.info("Created public key")
        return self.public_key
