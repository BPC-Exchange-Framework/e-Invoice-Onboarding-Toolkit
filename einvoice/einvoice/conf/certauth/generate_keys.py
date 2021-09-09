# certauth.generate_keys.py
from private import PrivateKey
from public import PublicKey
from csr import CSR
from sign import SignedKey

if __name__ == "__main__":
    # Generate CA's private key
    ca_private_key = PrivateKey.generate()
    ca_private_key.save("PrivateP@ssw0rd", "ca-private-key.pem")

    # Generate CA's public key
    name_dict = {
        "country":"US", 
        "state":"New York", 
        "locality":"New York", 
        "org":"Charlie's Certificate Authority", 
        "hostname":"charlie_CA.example.com",
    }

    ca_public_key = PublicKey.generate(ca_private_key, name_dict, is_ca=True)
    ca_public_key.save("ca-public-key.pem")

    # Generate private key for the server
    server_private_key = PrivateKey.generate()
    server_private_key.save("ServerP@ssw0rd", "server-private-key.pem")

    # Generate CSR
    name_dict = {
        "country":"US", 
        "state":"Maryland", 
        "locality":"Baltimore", 
        "org":"Alice Co", 
        "hostname":"alice.example.net",
    }
    alt_names = ['localhost', 'alice.example.net', ]

    csr = CSR.generate(server_private_key, alt_names, name_dict)
    csr.save("server-csr.pem")

    # CA signs CSR, creating server's certificate / public key
    signed_key = SignedKey.generate(csr, ca_public_key, ca_private_key)
    signed_key.save("server-public-key.pem")
