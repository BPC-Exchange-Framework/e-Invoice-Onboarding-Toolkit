#!/usr/bin/env python3
#
# File: test_hasher_hasher.py
# About: e-Invoice testing suite; app_handler.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest.

"""
from uuid import uuid4
from hashlib import sha256
from base64 import b32encode
from einvoice.app_logging import create_logger
from einvoice.urn_hasher import Hasher


# Test the logging fuctionality using built-in Pytest "caplog"
def test_log_insert(caplog):
    """This is a pytest to validate loggig is writing properly to a log."""
    log = create_logger("Pytest_test_logger_1")
    log_test_uuid = str(uuid4())
    log.info("Adding uuid to log for testing %s", log_test_uuid)
    for record in caplog.records:
        assert record.levelname != "CRITITAL"
    assert log_test_uuid in caplog.text
    if log_test_uuid in caplog.text:
        log.info("Found uuid %s in log", log_test_uuid)


# Another quick test of the log functionality as a baseline - has handlers.
def test_logger():
    """This is a pytest to validate the log handlers are being created."""
    log = create_logger("Pytest_test_logger_2")
    assert log.hasHandlers()
    if log.hasHandlers():
        log.info("Logger has handlers.")


def ash_hash(urn):
    return (b32encode(sha256(bytes(urn.lower(), "utf-8")).digest())
            .rstrip(b"=").lower()).decode('utf-8')


#############################################
#
#  Test Case 1
#
#############################################


def test_hasher_1():
    """Test case #1 hasher"""

    test_case_spec = "urn:oasis:names:tc:ebcore:partyid-"\
        "type:unregistered:myscheme"
    test_case_schema = "BPC01:"
    test_case_party_id = "bpcBusid01"
    test_hasher = Hasher()
    test_value = test_hasher.hasher(test_case_spec,
                                    test_case_schema,
                                    test_case_party_id)
    return test_value


def test_hasher_1_case_1():
    case_dict = test_hasher_1()
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "unregistered:myscheme:bpc01::bpcbusid01"
    assert (
        case_dict.get('final_urn') == test_case_urn
    )


def test_hasher_1_case_2():
    case_dict = test_hasher_1()
    test_case_hash = "yn5tj7bteln4c5o4mtul7yvnq3pwu6dpmipcof4pwcbsd3avvn7a"
    assert (
        case_dict.get('urn_hash') == test_case_hash
    )


def test_hasher_1_case_3():
    case_dict = test_hasher_1()
    urn = case_dict.get("final_urn")
    assert (
        case_dict.get('urn_hash') == ash_hash(urn)
    )


#############################################
#
#  Test Case 2
#
#############################################


def test_hasher_2():
    """Test case #2 hasher"""
    test_case_spec = "urn:oasis:names:tc:ebcore:partyid-type"
    test_case_schema = "iso6523:"
    test_case_party_id = "0123456789"
    test_hasher = Hasher()
    test_value = test_hasher.hasher(test_case_spec,
                                    test_case_schema,
                                    test_case_party_id)
    return test_value


def test_hasher_2_case_1():
    case_dict = test_hasher_2()
    test_case_urn = "urn:oasis:names:tc:ebcore:pa"\
        "rtyid-type:iso6523::0123456789"
    assert (
        case_dict.get('final_urn') == test_case_urn
    )


def test_hasher_2_case_2():
    case_dict = test_hasher_2()
    test_case_hash = "6c24uvqpxrfyweqimfxmsuym3bbjvoikuwmmidquz2a2zzyikdya"
    assert (
        case_dict.get('urn_hash') == test_case_hash
    )


def test_hasher_2_case_3():
    case_dict = test_hasher_2()
    urn = case_dict.get("final_urn")
    assert (
        case_dict.get('urn_hash') == ash_hash(urn)
    )


#############################################
#
#  Test Case 3
#
#############################################


def test_hasher_3():
    """Test case #3 hasher"""
    test_case_spec = "urn:oasis:names:tc:ebcore:partyid-type"
    test_case_schema = "iso6523:0088:"
    test_case_party_id = "EAN-7638725972413"
    test_hasher = Hasher()
    test_value = test_hasher.hasher(test_case_spec,
                                    test_case_schema,
                                    test_case_party_id)
    return test_value


def test_hasher_3_case_1():
    case_dict = test_hasher_3()
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:iso6523"\
        ":0088::ean-7638725972413"
    assert (
        case_dict.get('final_urn') == test_case_urn
    )


def test_hasher_3_case_2():
    case_dict = test_hasher_3()
    test_case_hash = "bc2ntkxz42amx3a5rmjbsaesp5ucuc3iciposkd3qwnj6b4wjh2q"
    assert (
        case_dict.get('urn_hash') == test_case_hash
    )


def test_hasher_3_case_3():
    case_dict = test_hasher_3()
    urn = case_dict.get("final_urn")
    assert (
        case_dict.get('urn_hash') == ash_hash(urn)
    )


#############################################
#
#  Test Case 4
#
#############################################


def test_hasher_4():
    """Test case #4 hasher"""
    test_case_spec = "urn:oasis:names:tc:ebcore:partyid-type"
    test_case_schema = "iso6523:0088:"
    test_case_party_id = "bpc-2343030383"
    test_hasher = Hasher()
    test_value = test_hasher.hasher(test_case_spec,
                                    test_case_schema,
                                    test_case_party_id)
    return test_value


def test_hasher_4_case_1():
    case_dict = test_hasher_4()
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:iso6523:"\
        "0088::bpc-2343030383"
    assert (
        case_dict.get('final_urn') == test_case_urn
    )


def test_hasher_4_case_2():
    case_dict = test_hasher_4()
    test_case_hash = "rixkdb2u5xxf7vtieezqvakx5r2bc3iugzeqd35ibeddloeapf6a"
    assert (
        case_dict.get('urn_hash') == test_case_hash
    )


def test_hasher_4_case_3():
    case_dict = test_hasher_4()
    urn = case_dict.get("final_urn")
    assert (
        case_dict.get('urn_hash') == ash_hash(urn)
    )


#############################################
#
#  Test Case 5
#
#############################################


def test_hasher_5():
    """Test case #5 hasher"""
    test_case_spec = "urn:oasis:names:tc:ebcore:partyid-type"
    test_case_schema = "iso6523:0088"
    test_case_party_id = "4035811991021"
    test_hasher = Hasher()
    test_value = test_hasher.hasher(test_case_spec,
                                    test_case_schema,
                                    test_case_party_id)
    return test_value


def test_hasher_5_case_1():
    case_dict = test_hasher_5()
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088:4035811991021"
    assert (
        case_dict.get('final_urn') == test_case_urn
    )


def test_hasher_5_case_2():
    case_dict = test_hasher_5()
    test_case_hash = "i3qyb36ctayrfgthbycqzdtojfhgazjeglfooe7727egvdwrk5qq"
    assert (
        case_dict.get('urn_hash') == test_case_hash
    )


def test_hasher_5_case_3():
    case_dict = test_hasher_5()
    urn = case_dict.get("final_urn")
    assert (
        case_dict.get('urn_hash') == ash_hash(urn)
    )
