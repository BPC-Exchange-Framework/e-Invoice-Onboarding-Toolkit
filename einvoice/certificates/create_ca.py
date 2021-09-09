#!/usr/bin/env python3
#
# pylint: disable=R0902, R0913
# Too many instance attributes, Too many arguments
# File: create_ca.py
# About: Dataclass definition of entities user for certificate creation.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-09-202 (September 2, 2021)
#
"""This application will create a CA

"""
import datetime
import uuid
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509.oid import NameOID


class CreateCA:
    """Class to crete a Certificate Authority"""

    def __init__(self):
        """Entry point for the app."""
        self.good_from_date = None
        self.ca_cert = None
        self.private_key = None
        self.public_key = None
        self.one_day = None
        self.one_year = None
        self.certificate = None

    def create_private_key(self, public_exponent, key_size):
        """Create a private key"""
        public_exponent = int(public_exponent)
        key_size = int(key_size)
        self.private_key = rsa.generate_private_key(public_exponent, key_size,
                                                    backend=default_backend())
        return self.private_key

    def create_public_key(self, private_key):
        """Create a public key using a private key"""
        self.public_key = private_key.public_key()
        return self.public_key

    def create_ca(self, subject_common_name, subject_organization_name,
                  subject_organizational_unit_name,
                  issuer_common_name, ca_public_key, ca_private_key):
        """Create a CA using certificate builder."""
        self.ca_cert = x509.CertificateBuilder()

        self.ca_cert = self.ca_cert.subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, subject_common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME,
                               subject_organization_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                               subject_organizational_unit_name),
        ]))

        self.ca_cert = self.ca_cert.issuer_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, issuer_common_name),
        ]))

        self.one_day = datetime.timedelta(1, 0, 0)
        self.one_year = datetime.timedelta(365, 0, 0)

        self.ca_cert = self.ca_cert.not_valid_before(
            datetime.datetime.today() - self.one_day)
        self.ca_cert = self.ca_cert.not_valid_after(
            datetime.datetime.today() + self.one_year)

        self.ca_cert = self.ca_cert.serial_number(int(uuid.uuid4()))
        self.ca_cert = self.ca_cert.public_key(ca_public_key)
        self.ca_cert = self.ca_cert.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )
        self.certificate = self.ca_cert.sign(
            private_key=ca_private_key, algorithm=hashes.SHA256(),
            backend=default_backend()
        )
        print(isinstance(self.certificate, x509.Certificate))

        return self.certificate

    @staticmethod
    def write_private_key_to_file(private_key_file_name, private_key,
                                  secret_password):
        """A method to write the private key to a file as PEM"""
        private_encoding = serialization.Encoding.PEM
        private_output_format = serialization.PrivateFormat.TraditionalOpenSSL
        encryption_algorithm = serialization.BestAvailableEncryption(
            bytes(secret_password, "utf-8"))
        with open(private_key_file_name, "wb") as file_name:
            file_name.write(private_key.private_bytes(private_encoding,
                                                      private_output_format,
                                                      encryption_algorithm))

    @staticmethod
    def write_public_key_to_file(public_key_file_name, public_key):
        """A method to write the public key to a file as SSH"""
        public_encoding = serialization.Encoding.OpenSSH
        public_output_format = serialization.PublicFormat.OpenSSH
        with open(public_key_file_name, "wb") as file_name:
            file_name.write(public_key.public_bytes(
                public_encoding, public_output_format))
