#!/usr/bin/env python3
#
# pylint: disable=C0103
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
    def write_private_key_to_file(file_name, key, password):
        """A method to write the private key to a file as PEM"""
        encoding = serialization.Encoding.PEM
        output_format = serialization.PrivateFormat.PKCS8
        encryption_algorithm = serialization.BestAvailableEncryption(
            bytes(password, "utf-8"))
        pem = key.private_bytes(encoding, output_format, encryption_algorithm)
        with open(file_name, "wb") as file_out:
            file_out.write(pem)

    @staticmethod
    def write_public_key_to_file(file_name, key):
        """A method to write the public key to a file as PEM"""
        encoding = serialization.Encoding.PEM
        output_format = serialization.PublicFormat.SubjectPublicKeyInfo
        pem = key.public_bytes(encoding, output_format)
        with open(file_name, "wb") as file_out:
            file_out.write(pem)

    @staticmethod
    def write_CA_to_file(file_name, CA):
        """A method to write the CA to file.  """
        encoding = serialization.Encoding.PEM
        pem = CA.public_bytes(encoding)
        with open(file_name, "wb") as file_out:
            file_out.write(pem)

    @staticmethod
    def read_private_key_in(file_name, password=None):
        """A method to read the private key in from a file"""
        if password is not None:
            password = password.encode('utf-8')
        with open(file_name, 'rb') as file_in:
            key = serialization.load_pem_private_key(
                file_in.read(),
                password
            )
        return key

    @staticmethod
    def read_public_key_in(file_name, password=None):
        """A method to read the public key in from a file"""
        if password is not None:
            password = password.encode('utf-8')
        with open(file_name, 'rb') as file_in:
            key = serialization.load_pem_public_key(
                file_in.read(),
                password
            )
        return key
