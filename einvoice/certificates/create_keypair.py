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
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from certificates.cert_logging import create_logger


class CreateKeypair:
    """Class to create a public/private"""

    def __init__(self):
        """Entry point for the app."""
        self.public_exponent = None
        self.key_size = None
        self.backend = None
        self.private_key = None
        self.public_key = None

    def create_private_key(self, exponent="65537", size="2048",
                           backend=default_backend()):
        """Create a private key"""
        log = create_logger("create_private_key")
        log.info("Private key exponent is %s.",  exponent)
        log.info("Key size is %s.", size)
        self.public_exponent = int(exponent)
        self.key_size = int(size)
        self.backend = backend
        self.private_key = rsa.generate_private_key(self.public_exponent,
                                                    self.key_size,
                                                    self.backend)
        log.info('Private Key created.')
        return self.private_key

    def create_public_key(self, private_key):
        """Create a public key using a private key"""
        log = create_logger("create_public_key")
        self.public_key = private_key.public_key()
        log.info("Public Key created.")
        return self.public_key
