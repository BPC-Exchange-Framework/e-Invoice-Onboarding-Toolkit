# certauth.sign.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from public import PublicKey
from util import make_builder

class SignedKey(PublicKey):
    @classmethod
    def generate(cls, csr, ca_public_key, ca_private_key):
        signed_key = SignedKey()
        builder = make_builder(csr.key.subject, 
            issuer=ca_public_key.key.subject)
        builder = builder.public_key(csr.key.public_key())

        for extension in csr.key.extensions:
            builder = builder.add_extension(extension.value, extension.critical)

        signed_key.key = builder.sign(private_key=ca_private_key.key,
            algorithm=hashes.SHA256(), backend=default_backend())

        return signed_key
