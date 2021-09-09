# certauth.csr.py
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from public import PublicKey
from util import make_x509_name

class CSR(PublicKey):
    @classmethod
    def generate(cls, private_key, alt_hosts, name_dict):
        subject = make_x509_name(**name_dict)

        # Generate alternative DNS names
        hosts = []
        for host in alt_hosts:
            hosts.append( x509.DNSName(host) )

        subject_alt_names = x509.SubjectAlternativeName(hosts)

        builder = (
            x509.CertificateSigningRequestBuilder()
            .subject_name(subject)
            .add_extension(subject_alt_names, critical=False)
        )

        csr = CSR()
        csr.key = builder.sign(private_key.key, hashes.SHA256(), 
            default_backend())
        return csr

    @classmethod
    def load(cls, filename):
        public_key = PublicKey()
        with open(filename, "rb") as keyfile:
            data = keyfile.read()
            public_key.key = x509.load_pem_x509_csr(data, default_backend())

        return public_key
