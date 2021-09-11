#!/usr/bin/env python3
#
# pylint: disable=R0902
# Too many instance attributes
# File: certificate_entities.py
# About: Dataclass definition of entities user for certificate creation.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-09-202 (September 2, 2021)
#
"""The dataclass definitions of certificate entities.
    Define the structure of certificate entities to create and sign certs.

    Usage:
    my_ca_cert = CertificateAuthority()
    my_csr = CertificateSigningRequest()
    my_signed_cert = SignedCertificate()
"""
# import os
from dataclasses import dataclass


@dataclass
class CertificateAuthority:
    """Dataclass which represents a Certificate of Authority entity.

    All values which may be necessary to work with a certificate.

    Args:

    Attributes:
            dir: dirname
                The root directory or starting point
            certs: dirname
                A directory to hold existing certificates
            crl_dir: dirname
                A directory to hold revocation files.
            new_certs_dir: dirname
                A directory to hold new certs.
            database: dirname = f"{dir}/index.txt"
                A flat file which will act as a database for certs
            serial: dirname
                A start point # to use for incrementing certs
            rand_file: dirname
                A file that contains seed for RNG
            private_key: str
               The file containing the private key
            certificate: str
               The file of the cert itself
            crl_number: str
                An identifier for the CRL
            crl: str
                The CRL file.

    Returns:

    Raises:

    """
    # OpenSSL root CA configuration file.

    # [ ca ]
    # `man ca`
    default_ca: str = 'CA_default'

    # [CA_default]
    # Directory and file locations.
    dir: str = '/home/kelly/Dev/'
    certs: str = f'{dir}/certs'
    crl_dir: str = f'{dir}/crl'
    new_certs_dir: str = f'{dir}/newcerts'
    database: str = f'{dir}/index.txt'
    serial: str = f'{dir}/serial'
    rand_file: str = f'{dir}/private/.rand'

    # The root key and root certificate.
    private_key: str = f'{dir}/private/ca.key.pem'
    certificate: str = f'{dir}/certs/ca.cert.pem'

    # For certificate revocation lists.
    crl_number: str = f'{dir}/crl_number'
    crl: str = f'{dir}/crl/ca.crl.pem'

    # crl_extensions = crl_ext
    # default_crl_days = 30

    # # SHA-1 is deprecated, so use SHA-2 instead.
    # default_md = sha256

    # name_opt = ca_default
    # cert_opt = ca_default
    # default_days = 375
    # preserve = no
    # policy = policy_strict

    # [policy_strict]
    # # The root CA should only sign intermediate certificates that match.
    # # See the POLICY FORMAT section of `man ca`.
    # countryName = match
    # stateOrProvinceName = match
    # organizationName = match
    # organizationalUnitName = optional
    # commonName = supplied
    # emailAddress = optional

    # [policy_loose]
    # # Allow the intermediate CA to sign a more diverse range of certificates.
    # # See the POLICY FORMAT section of the `ca` man page.
    # countryName = optional
    # stateOrProvinceName = optional
    # localityName = optional
    # organizationName = optional
    # organizationalUnitName = optional
    # commonName = supplied
    # emailAddress = optional

    # [req]
    # # Options for the `req` tool (`man req`).
    # default_bits = 2048
    # distinguished_name = req_distinguished_name
    # string_mask = utf8only

    # # SHA-1 is deprecated, so use SHA-2 instead.
    # default_md = sha256

    # # Extension to add when the -x509 option is used.
    # x509_extensions = v3_ca

    # [req_distinguished_name]
    # # See <https://en.wikipedia.org/wiki/Certificate_signing_request>.
    # countryName = Country Name(2 letter code)
    # stateOrProvinceName = State or Province Name
    # localityName = Locality Name
    # 0.organizationName = Organization Name
    # organizationalUnitName = Organizational Unit Name
    # commonName = Common Name
    # emailAddress = Email Address

    # # Optionally, specify some defaults.
    # countryName_default = GB
    # stateOrProvinceName_default = England
    # localityName_default =
    # 0.organizationName_default = Alice Ltd
    # organizationalUnitName_default =
    # emailAddress_default =

    # [v3_ca]
    # # Extensions for a typical CA (`man x509v3_config`).
    # subjectKeyIdentifier = hash
    # authorityKeyIdentifier = keyid: always, issuer
    # basicConstraints = critical, CA: true
    # keyUsage = critical, digitalSignature, cRLSign, keyCertSign

    # [v3_intermediate_ca]
    # # Extensions for a typical intermediate CA (`man x509v3_config`).
    # subjectKeyIdentifier = hash
    # authorityKeyIdentifier = keyid: always, issuer
    # basicConstraints = critical, CA: true, pathlen: 0
    # keyUsage = critical, digitalSignature, cRLSign, keyCertSign

    # [usr_cert]
    # # Extensions for client certificates (`man x509v3_config`).
    # basicConstraints = CA: FALSE
    # nsCertType = client, email
    # nsComment = "OpenSSL Generated Client Certificate"
    # subjectKeyIdentifier = hash
    # authorityKeyIdentifier = keyid, issuer
    # keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
    # extendedKeyUsage = clientAuth, emailProtection

    # [server_cert]
    # # Extensions for server certificates (`man x509v3_config`).
    # basicConstraints = CA: FALSE
    # nsCertType = server
    # nsComment = "OpenSSL Generated Server Certificate"
    # subjectKeyIdentifier = hash
    # authorityKeyIdentifier = keyid, issuer: always
    # keyUsage = critical, digitalSignature, keyEncipherment
    # extendedKeyUsage = serverAuth

    # [crl_ext]
    # # Extension for CRLs (`man x509v3_config`).
    # authorityKeyIdentifier = keyid: always

    # [ocsp]
    # # Extension for OCSP signing certificates (`man ocsp`).
    # basicConstraints = CA: FALSE
    # subjectKeyIdentifier = hash
    # authorityKeyIdentifier = keyid, issuer
    # keyUsage = critical, digitalSignature
    # extendedKeyUsage = critical, OCSPSigning
