# pylint: disable=W0612, W0611
# Unused variables, unused imports

"""
Test cases for create_ca
"""
import os
from os.path import join, dirname
# import sys
# sys.path.append("../certificates")
from dotenv import load_dotenv
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from certificates.create_ca import CreateCA
from certificates.cert_logging import create_logger


def test_private_key():
    """Test creation of a private key"""
    log = create_logger("test_private_key")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    pub_exp = os.getenv("PUBLIC_EXPONENT")
    key_size = os.getenv("KEY_SIZE")
    log.info("Exponent is: %s", str(pub_exp))
    log.info("Key size is: %s", str(key_size))
    create_ca_private = CreateCA()
    private_key = create_ca_private.create_private_key(pub_exp, key_size)
    is_private_key = isinstance(private_key, rsa.RSAPrivateKey)
    log.info("Is private key RSAPrivateKey?: %s", str(is_private_key))
    assert is_private_key
    return private_key


def test_public_key():
    """Test creation of the public key"""
    log = create_logger("test_public_key")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    pub_exp = os.getenv("PUBLIC_EXPONENT")
    key_size = os.getenv("KEY_SIZE")
    log.info("Exponent is: %s", str(pub_exp))
    log.info("Key size is: %s", str(key_size))
    create_ca = CreateCA()
    private_key = create_ca.create_private_key(pub_exp, key_size)
    public_key = create_ca.create_public_key(private_key)
    is_public_key = isinstance(public_key, rsa.RSAPublicKey)
    log.info("Is public key RSAPublicKey?: %s", str(is_public_key))
    assert is_public_key
    return public_key


def test_encryption():
    """Test encryption"""
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    log = create_logger("test_create_ca")
    exp = os.getenv("PUBLIC_EXPONENT")
    key = os.getenv("KEY_SIZE")
    text = os.getenv("RANDOM_TXT")
    bknd = os.getenv("BACKEND")
    private_1 = rsa.generate_private_key(65537, 2048, bknd)
    public_1 = private_1.public_key()

    create_ca = CreateCA()
    private_2 = create_ca.create_private_key(exp, key)
    public_2 = create_ca.create_public_key(private_2)
    # assert private_1 == private_2
    # assert public_1 == public_2

def test_create_ca():
    """Test creation of the ca cert"""
    log = create_logger("test_create_ca")
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
