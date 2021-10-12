#!/usr/bin/env python3
#
# pylint: disable=R0902, R0903
# Too many instance attributes, Too few public methods,
# File: create_ca.py
# About: Create a Certificate of Authority
# Development: Kelly Kinney
# Date: 2021-10-01 (October 1, 2021)
#
"""This application will create a Certificate of Authority"""
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from certificates.create_keypair import CreateKeypair
from certificates.serialization import Serialize


class CreateCA:
    """Class to create a Certificate Authority"""

    def __init__(self):
        """Entry point for the app."""
        self.subject_common_name = None
        self.issuer_common_name = None
        self.subject_org_name = None
        self.subject_org_unit_name = None
        self.private_key_file = None
        self.public_key_file = None
        self.private_key_file_pwd = None
        self.ca_file_name = None
        self.keypair = None
        self.writer = None
        self.private_key = None
        self.public_key = None
        self.ca_cert = None
        self.one_day = None
        self.one_year = None
        self.cert_home = None
        self.CA_certificate = None
        self.CA_cert_file = None

    def create_ca(self):
        """Create a CA using certificate builder."""
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)
        self.subject_common_name = str(os.getenv("CA_SUBJECT_COMMON_NAME"))
        self.issuer_common_name = str(os.getenv("CA_ISSUER_COMMON_NAME"))
        self.subject_org_name = str(os.getenv("CA_SUBJECT_ORG_NAME"))
        self.subject_org_unit_name =\
            str(os.getenv("CA_SUBJECT_ORG_UNIT_NAME"))
        self.cert_home = str(os.getenv("CERTIFICATE_STORE"))
        self.private_key_file = self.cert_home +\
            str(os.getenv("CA_PRIVATE_KEY_FILE"))
        self.public_key_file = self.cert_home +\
            str(os.getenv("CA_PUBLIC_KEY_FILE"))
        self.private_key_file_pwd =\
            str(os.getenv("CA_PRIVATE_KEY_SECRET_PWD"))
        self.ca_cert_file = self.cert_home + str(os.getenv("CA_CERT_FILE"))
        self.keypair = CreateKeypair()
        self.writer = Serialize()
        self.private_key = self.keypair.create_private_key()
        self.public_key = self.keypair.create_public_key(self.private_key)
        self.writer.write_private_key_to_file(self.private_key_file,
                                              self.private_key,
                                              self.private_key_file_pwd)
        self.writer.write_public_key_to_file(self.public_key_file,
                                             self.public_key)
        self.ca_cert = x509.CertificateBuilder()

        self.ca_cert = self.ca_cert.subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, self.subject_common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME,
                               self.subject_org_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                               self.subject_org_unit_name),
        ]))

        self.ca_cert = self.ca_cert.issuer_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, self.issuer_common_name),
        ]))

        self.one_day = datetime.timedelta(1, 0, 0)
        self.one_year = datetime.timedelta(365, 0, 0)

        self.ca_cert = self.ca_cert.not_valid_before(
            datetime.datetime.today() - self.one_day)
        self.ca_cert = self.ca_cert.not_valid_after(
            datetime.datetime.today() + self.one_year)

        self.ca_cert = self.ca_cert.serial_number(x509.random_serial_number())
        self.ca_cert = self.ca_cert.public_key(self.public_key)
        self.ca_cert = self.ca_cert.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )
        self.certificate = self.ca_cert.sign(
            private_key=self.private_key, algorithm=hashes.SHA256(),
            backend=default_backend()
        )
        print(isinstance(self.certificate, x509.Certificate))
        self.writer.write_CA_to_file(self.ca_cert_file, self.certificate)
        return self.certificate
