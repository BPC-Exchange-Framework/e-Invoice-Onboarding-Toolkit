#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913
# Too many instance attributes, Too many arguments
# pycodestyle: disable=E303
# Too many blank lines.
# File: encryption.py
# About: Encrpt and decrypt using public/private key pairs based on
# Cryptography package
# Development: Kelly Kinney
# Date: 2021-09-202 (September 2, 2021)
#
"""This application will create a encrpt and decrypt text.

"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

class CryptoEncrypt():
    """ Class to encrypt and decrypt text using public/private key pairs.
    There are two ways to do this here. One method uses the cryptography
    package and it's Fernet implementation.  The other uses the rsa package.
    The Fernet implementation returns a key to decrypt which must be kept
    secret."""


    @classmethod
    def encrypt_crypto(cls, public_key, text):
        """ Classmethod to encrypt a message using the cryptography package.
            Arguments:
                public_key must be in the form of  RSAPublicKey or loaded
                using load_pem_public_key
        """
        cls.b_text = text.encode('utf-8')
        algorithm=hashes.SHA256()
        mgf=padding.MGF1(algorithm)
        label = None
        cls.cipher_output = public_key.encrypt(cls.b_text,
                                               padding.OAEP(mgf,
                                                            algorithm,
                                                            label))
        return cls.cipher_output


    @classmethod
    def decrypt_crypto(cls, private_key, ciphertext):
        """ Classmethod to decrypt a message using the cryptography package.
            Arguments:
                private_key must be in the form of  RSAPrivateKey or loaded
                using load_pem_private_key
        """
        algorithm=hashes.SHA256()
        mgf=padding.MGF1(algorithm)
        label = None
        cls.output = private_key.decrypt(ciphertext, padding.OAEP(mgf,
                                                                  algorithm,
                                                                  label))
        return cls.output

    @classmethod
    def signing(cls, private_key, message):
        """A classmethod to sign a message"""
        cls.b_text= message.encode("utf-8")
        # mgf if a mask generation function
        cls.mgf = padding.MGF1(hashes.SHA256())
        cls.salt_length = padding.PSS.MAX_LENGTH
        cls.signature = private_key.sign(cls.b_text,
                                         padding.PSS(cls.mgf,
                                                         cls.salt_length),
                                         hashes.SHA256())
        return cls.signature

    @classmethod
    def verification(cls, public_key, signature, message):
        """A classmethod to verify a message using a signature"""
        # mgf if a mask generation function
        cls.mgf = padding.MGF1(hashes.SHA256())
        cls.salt_length = padding.PSS.MAX_LENGTH

        try:
            public_key.verify(signature, message,
                              padding.PSS(cls.mgf, cls.salt_length),
                              hashes.SHA256())
        except InvalidSignature:
            pass
