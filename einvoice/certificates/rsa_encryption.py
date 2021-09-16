#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913
# Too many instance attributes, Too many arguments, too many blank lines
# pycodestyle: disable=E303
# Too many blank lines.
# File: rsa_encryption.py
# About: Encrpt and decrypt using public/private key pairs based on RSA.
# package.
# Development: Kelly Kinney
# Date: 2021-09-202 (September 2, 2021)
#
"""This application will create a encrpt and decrypt text.

"""
import rsa

class RsaEncrypt():
    """ Class to encrypt and decrypt text using public/private key pairs.
    There are two ways to do this here. One method uses the cryptography
    package and it's Fernet implementation.  The other uses the rsa package.
    The Fernet implementation returns a key to decrypt which must be kept
    secret."""


    @classmethod
    def generate_rsa_keypair(cls):
        """If you don't already have a private key to use, this will
        generate an rsa keypair for you."""
        (cls.pub_key, cls.priv_key) = rsa.newkeys(512)
        cls.keys = [cls.pub_key, cls.priv_key]
        return cls.keys

    @classmethod
    def encrypt_rsa(cls, public_key, text):
        """ Classmethod to encrypt a message using the RSA package.
        This encodes with the public key"""
        cls.b_text = text.encode('utf-8')
        cls.output = rsa.encrypt(cls.b_text, public_key)
        return cls.output

    @classmethod
    def decrypt_rsa(cls, private_key, text):
        """Classmethod to decrypt a messgage using the RSA package"""
        cls.b_text = text.encode('utf-8')
        cls.output = rsa.decrypt(cls.b_text, private_key)
        return cls.output
