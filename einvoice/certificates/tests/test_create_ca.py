# pylint: disable=W0612, W0611, R0914, C0103
# Unused variables, unused imports, too many local variables, snake case
"""
Test cases for create_ca
"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
# from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from certificates.create_ca import CreateCA
from certificates.cert_logging import create_logger
from certificates.serialization import Serialize
from certificates.create_keypair import CreateKeypair


def create_private_key():
    """Test creation of a private key"""
    create_ca_private = CreateKeypair()
    private_key = create_ca_private.create_private_key()
    is_private_key = isinstance(private_key, rsa.RSAPrivateKey)
    log = create_logger("Test_case_create_private_key")
    log.info("Is private key RSAPrivateKey?: %s", str(is_private_key))
    assert is_private_key
    return private_key


def test_write_private_key():
    """Testing creation of a private key and writing to a file."""
    log = create_logger("test_write_private_key")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    private_key = create_private_key()
    private_key_file_name = str(os.getenv("PRIVATE_KEY_FILE_NAME"))
    private_key_file_pwd = str(os.getenv("PRIVATE_KEY_SECRET_PASSWORD"))
    log.info("Attempting to write private key to file. ")
    log.info(private_key)
    writer = Serialize()
    writer.write_private_key_to_file(private_key_file_name, private_key,
                                     private_key_file_pwd)


def create_public_key():
    """Test creation of the public key"""
    log = create_logger("create_public_key")
    create_ca = CreateKeypair()
    private_key = create_ca.create_private_key()
    public_key = create_ca.create_public_key(private_key)
    is_public_key = isinstance(public_key, rsa.RSAPublicKey)
    log.info("Is public key RSAPublicKey?: %s", str(is_public_key))
    assert is_public_key
    return public_key


def test_create_public_key():
    """Testing creation of a public key and writing to a file."""
    log = create_logger("test_create_public_key")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    public_key_file_name = str(os.getenv("PUBLIC_KEY_FILE_NAME"))
    public_key = create_public_key()
    log.info("Attempting to write public key to file. ")
    writer = Serialize()
    writer.write_public_key_to_file(public_key_file_name, public_key)


# def test_encryption():
#     """Test encryption"""
#     dotenv_path = join(dirname(__file__), '../.env')
#     load_dotenv(dotenv_path)
#     log = create_logger("test_create_ca")
#     exp = os.getenv("PUBLIC_EXPONENT")
#     key = os.getenv("KEY_SIZE")
#     text = os.getenv("RANDOM_TXT")
#     bknd = os.getenv("BACKEND")
#     private_1 = rsa.generate_private_key(65537, 2048,
#     backend=default_backend())
#     public_1 = private_1.public_key()

#     create_ca = CreateCA()
#     private_2 = create_ca.create_private_key(exp, key)
#     public_2 = create_ca.create_public_key(private_2)
#     assert private_1 == private_2
#     assert public_1 == public_2

def test_create_ca():
    """Test creation of the ca cert"""
    log = create_logger("test_create_ca")
    log.info("Attempting to create a CA")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    log = create_logger("test_create_ca")
    create_ca = CreateCA()
    CA = create_ca.create_ca()
    log.info(CA)
    assert isinstance(CA, x509.Certificate)
