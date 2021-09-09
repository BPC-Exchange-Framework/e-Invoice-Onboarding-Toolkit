# certauth.private.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import rsa

class PrivateKey:
    @classmethod
    def generate(cls):
        private_key = PrivateKey()
        private_key.key = rsa.generate_private_key(public_exponent=65537, 
            key_size=2048, backend=default_backend())

        return private_key

    @classmethod
    def load(cls, filename, password):
        private_key = PrivateKey()
        encoded_password = password.encode('utf-8')

        with open(filename, "rb") as keyfile:
            data = keyfile.read()
            private_key.key = serialization.load_pem_private_key(data,
                encoded_password, default_backend())

        return private_key

    def save(self, password, filename):
        utf8_pass = password.encode("utf-8")
        algorithm = serialization.BestAvailableEncryption(utf8_pass)

        encoding = serialization.Encoding.PEM
        format = serialization.PrivateFormat.TraditionalOpenSSL

        with open(filename, "wb") as keyfile:
            key_bytes = self.key.private_bytes(encoding=encoding, format=format,
                encryption_algorithm=algorithm)

            keyfile.write(key_bytes)
