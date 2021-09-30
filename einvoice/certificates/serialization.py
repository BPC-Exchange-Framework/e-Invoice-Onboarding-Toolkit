#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913, C0103
# Too many instance attributes, Too many arguments, snake naming convention
# File: serialization.py
# About: File to handle serialization of certs.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-09-28 (September 28, 2021)
#
"""This application handles reading and writing of certs
to the filesystem.


Reading a file in or writing a file out are functions handled by
file io in Python.  Serialization is the process of putting the data in
the format specified.

The method to serialize the private_key is
    private_bytes(encoding, format, encryption_algorithm)
    contained in cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey

The method to serialize the public_key is
    public_key(encoding, format)
    contained in cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey

"""
from cryptography.hazmat.primitives import serialization


class Serialize:
    """Class to handle file io using serialization"""

    @staticmethod
    def write_private_key_to_file(private_key_file_name, private_key,
                                  secret_password):
        """A method to write the private key to a file as PEM"""
        private_encoding = serialization.Encoding.PEM
        private_output_format = serialization.PrivateFormat.PKCS8
        encryption_algorithm = serialization.BestAvailableEncryption(
            bytes(secret_password, "utf-8"))
        pem = private_key.private_bytes(private_encoding,
                                        private_output_format,
                                        encryption_algorithm)
        with open(private_key_file_name, "wb") as file_name:
            file_name.write(pem)

    @staticmethod
    def write_public_key_to_file(public_key_file_name, public_key):
        """A method to write the public key to a file as PEM"""
        public_encoding = serialization.Encoding.PEM
        public_output_format = serialization.PublicFormat.SubjectPublicKeyInfo
        pem = public_key.public_bytes(public_encoding, public_output_format)
        with open(public_key_file_name, "wb") as file_name:
            file_name.write(pem)

    @staticmethod
    def write_CA_to_file(CA_file_name, CA):
        """A method to write the CA to file.  """
        public_encoding = serialization.Encoding.PEM
        pem = CA.public_bytes(public_encoding)
        with open(CA_file_name, "wb") as file_name:
            file_name.write(pem)

    @staticmethod
    def read_private_key_in(file_name, key_file_password=None):
        """A method to read the private key in from a file"""
        password = None
        if key_file_password is not None:
            password = key_file_password.encode('utf-8')
        with open(file_name, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password
            )
        return private_key

    @staticmethod
    def read_public_key_in(file_name, key_file_password=None):
        """A method to read the public key in from a file"""
        password = None
        if key_file_password is not None:
            password = key_file_password.encode('utf-8')
        with open(file_name, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                password
            )
        return public_key
