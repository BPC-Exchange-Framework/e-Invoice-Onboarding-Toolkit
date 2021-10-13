#!/usr/bin/env python3
#
# pylint: disable=R0902, R0903, R0913
# Too many instance attributes, Too few public methods, Too many arguments
# File: create_ssc.py
# About: Creates a self-signed security certificate.
# Development: Kelly Kinney
# Date: 2021-10-05 (October 5, 2021)
#
"""This application will create a Self-Signed Security Certificate."""
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from certificates.create_keypair import CreateKeypair


class CreateSelfSignedCert:
    """Class to crete a Certificate Authority"""

    def __init__(self):
        """Entry point for the app."""
        self.keypair = None
        self.private_key = None
        self.ssc_cert = None
        self.good_from_date = None
        self.one_day = None
        self.one_year = None
        self.certificate = None
        self.public_key = None

    def create_ssc(self, subject_common_name, subject_organization_name,
                   subject_organizational_unit_name,
                   issuer_common_name):
        """Create a Self Signed Cert using certificate builder."""
        keypair = CreateKeypair()
        private_key = keypair.create_private_key()
        ssc_cert = x509.CertificateBuilder()
        ssc_cert = ssc_cert.subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, subject_common_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME,
                               subject_organization_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                               subject_organizational_unit_name),
        ]))
        ssc_cert = ssc_cert.issuer_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, issuer_common_name),
        ]))

        self.one_day = datetime.timedelta(1, 0, 0)
        self.one_year = datetime.timedelta(365, 0, 0)

        ssc_cert = ssc_cert.not_valid_before(
            datetime.datetime.today() - self.one_day)
        ssc_cert = ssc_cert.not_valid_after(
            datetime.datetime.today() + self.one_year)
        ssc_cert = ssc_cert.serial_number(x509.random_serial_number())
        ssc_cert = ssc_cert.public_key(self.public_key)
        ssc_cert = ssc_cert.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )
        self.certificate = ssc_cert.sign(
            private_key=private_key, algorithm=hashes.SHA256(),
            backend=default_backend()
        )
        print(isinstance(self.certificate, x509.Certificate))

        return self.certificate
