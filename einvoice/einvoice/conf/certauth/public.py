# certauth.public.py
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization 

from util import make_x509_name, make_builder

class PublicKey:
    @classmethod
    def generate(cls, private_key, name_dict, is_ca=False):
        subject = make_x509_name(**name_dict)

        # Self signed certificate means subject and issuer are the same
        builder = make_builder(subject, issuer=subject, is_ca=is_ca)
        builder = builder.public_key(private_key.key.public_key())

        # Sign the certificate with the private key
        public_key = PublicKey()
        public_key.key = builder.sign(private_key.key, hashes.SHA256(), 
            default_backend())

        return public_key

    @classmethod
    def load(cls, filename):
        public_key = PublicKey()
        with open(filename, "rb") as keyfile:
            data = keyfile.read()
            public_key.key = x509.load_pem_x509_certificate(data, 
                default_backend())

        return public_key

    def save(self, filename):
        with open(filename, "wb") as certfile:
            encoding = serialization.Encoding.PEM
            key_bytes = self.key.public_bytes(encoding)

            certfile.write(key_bytes)
