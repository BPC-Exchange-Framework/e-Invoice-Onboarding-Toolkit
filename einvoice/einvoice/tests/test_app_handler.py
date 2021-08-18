#!/usr/bin/env python3
#
# File: test_app_handler.py
# About: e-Invoice testing suite; app_handler.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest.

"""
from uuid import uuid4
from einvoice.app_logging import create_logger
from einvoice.app_handler import UrnHandler


# Test the logging fuctionality using built-in Pytest "caplog"
def test_log_insert(caplog):
    """This is a pytest to validate loggig is writing properly to a log."""
    log = create_logger("Pytest_test_logger_1")
    log_test_uuid = str(uuid4())
    log.debug("Adding uuid to log for testing %s", log_test_uuid)
    for record in caplog.records:
        assert record.levelname != "CRITITAL"
    assert log_test_uuid in caplog.text
    if log_test_uuid in caplog.text:
        log.debug("Found uuid %s in log", log_test_uuid)


# Another quick test of the log functionality as a baseline - has handlers.
def test_logger():
    """This is a pytest to validate the log handlers are being created."""
    log = create_logger("Pytest_test_logger_2")
    assert log.hasHandlers()
    if log.hasHandlers():
        log.debug("Logger has handlers.")


# Three tests for each party ID
# create urn
# create sha256 hash
# create b32 hash
def test_create_urn_lookup_1():
    """Test case #1 create_urn_lookup"""
    logger_name = ("Test case #1 create_urn_lookup")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::0123456789"
    test_case_party_id = "0123456789"
    test_urn = UrnHandler()
    test_value = test_urn.create_urn_lookup(test_case_party_id)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert (
        test_value == test_case_urn
    )
    log.debug("||End test cases.||")


def test_apply_sha256_hash_1():
    """Test case #1 apply_sha256_hash"""
    logger_name = ("Test case #1 apply_sha256_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::0123456789"
    test_case_sha256_hash = "f0b5ca560fbc4b8b1208616ec95"\
        "30cd8429ab90aa598c40e14ce81ace70850f0"
    test_urn = UrnHandler()
    test_value = test_urn.apply_sha256_hash(test_case_urn)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_sha256_hash
    log.debug("||End test cases.||")


def test_apply_b32_hash_1():
    """Test case #1 apply_b32_hash"""
    logger_name = ("Test case #1 apply_b32_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_sha256_hash = "f0b5ca560fbc4b8b1208616ec95"\
        "30cd8429ab90aa598c40e14ce81ace70850f0"
    test_case_b32_hash = "MYYGENLDME2TMMDGMJRTIYRYMIYTEMBYGYYTMZ"\
        "LDHE2TGMDDMQ4DIMRZMFRDSMDBME2TSO"\
        "DDGQYGKMJUMNSTQMLBMNSTOMBYGUYGMMA="
    test_urn = UrnHandler()
    test_value = test_urn.apply_b32_hash(test_case_sha256_hash)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_b32_hash
    log.debug("||End test cases.||")


def test_create_urn_lookup_2():
    """Test case #2 create_urn_lookup"""
    logger_name = ("Test case #2 create_urn_lookup")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::EAN-7638725972413"
    test_case_party_id = "EAN-7638725972413"
    test_urn = UrnHandler()
    test_value = test_urn.create_urn_lookup(test_case_party_id)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert (
        test_value == test_case_urn
    )
    log.debug("||End test cases.||")


def test_apply_sha256_hash_2():
    """Test case #2 apply_sha256_hash"""
    logger_name = ("Test case #2 apply_sha256_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::EAN-7638725972413"
    test_case_sha256_hash = "93bb91efa204b16933652ece6897ebf"\
        "265cd10f1533d24c127d5dc812e9d9de0"
    test_urn = UrnHandler()
    test_value = test_urn.apply_sha256_hash(test_case_urn)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_sha256_hash
    log.debug("||End test cases.||")


def test_apply_b32_hash_2():
    """Test case #2 apply_b32_hash"""
    logger_name = ("Test case #2 apply_b32_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_sha256_hash = "93bb91efa204b16933652ece6897ebf"\
        "265cd10f1533d24c127d5dc812e9d9de0"
    test_case_b32_hash = "HEZWEYRZGFSWMYJSGA2GEMJWHEZT"\
        "GNRVGJSWGZJWHA4TOZLCMYZDMNLDMQYTAZRRGUZTGZB"\
        "SGRRTCMRXMQ2WIYZYGEZGKOLEHFSGKMA="
    test_urn = UrnHandler()
    test_value = test_urn.apply_b32_hash(test_case_sha256_hash)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_b32_hash
    log.debug("||End test cases.||")


def test_create_urn_lookup_3():
    """Test case #3 create_urn_lookup"""
    logger_name = ("Test case #3 create_urn_lookup")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::bpc-2343030383"
    test_case_party_id = "bpc-2343030383"
    test_urn = UrnHandler()
    test_value = test_urn.create_urn_lookup(test_case_party_id)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert (
        test_value == test_case_urn
    )
    log.debug("||End test cases.||")


def test_apply_sha256_hash_3():
    """Test case #3 apply_sha256_hash"""
    logger_name = ("Test case #3 apply_sha256_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::bpc-2343030383"
    test_case_sha256_hash = "ae9520550626abdb6a3d8812bc8cc492"\
        "5524be6f2614b0cf0b9f8d2855e4179f"
    test_urn = UrnHandler()
    test_value = test_urn.apply_sha256_hash(test_case_urn)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_sha256_hash
    log.debug("||End test cases.||")


def test_apply_b32_hash_3():
    """Test case #3 apply_b32_hash"""
    logger_name = ("Test case #3 apply_b32_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_sha256_hash = "ae9520550626abdb6a3d8812bc8cc492"\
        "5524be6f2614b0cf0b9f8d2855e4179f"
    test_case_b32_hash = "MFSTSNJSGA2TKMBWGI3GCYTEMI3GCM3EHA4DCMTC"\
        "MM4GGYZUHEZDKNJSGRRGKNTGGI3DCNDCGBRWMMD"\
        "CHFTDQZBSHA2TKZJUGE3TSZQ="
    test_urn = UrnHandler()
    test_value = test_urn.apply_b32_hash(test_case_sha256_hash)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_b32_hash
    log.debug("||End test cases.||")


def test_create_urn_lookup_4():
    """Test case #4 create_urn_lookup"""
    logger_name = ("Test case #4 create_urn_lookup")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::4035811991021"
    test_case_party_id = "4035811991021"
    test_urn = UrnHandler()
    test_value = test_urn.create_urn_lookup(test_case_party_id)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert (
        test_value == test_case_urn
    )
    log.debug("||End test cases.||")


def test_apply_sha256_hash_4():
    """Test case #4 apply_sha256_hash"""
    logger_name = ("Test case #1 apply_sha256_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_urn = "urn:oasis:names:tc:ebcore:partyid-type:"\
        "iso6523::4035811991021"
    test_case_sha256_hash = "50e3e2082ac4cc5feee392d27ff8698"\
        "ce45c49b13741afd5b79306521c81dc84"
    test_urn = UrnHandler()
    test_value = test_urn.apply_sha256_hash(test_case_urn)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_sha256_hash
    log.debug("||End test cases.||")


def test_apply_b32_hash_4():
    """Test case #4 apply_b32_hash"""
    logger_name = ("Test case #1 apply_b32_hash")
    log = create_logger(logger_name)
    log.debug("||Begin test case.")
    test_case_sha256_hash = "50e3e2082ac4cc5feee392d27ff8698"\
        "ce45c49b13741afd5b79306521c81dc84"
    test_case_b32_hash = "GUYGKM3FGIYDQMTBMM2GGYZVMZSWKZJTHEZG"\
        "IMRXMZTDQNRZHBRWKNBVMM2DSYRRGM3TIM"\
        "LBMZSDKYRXHEZTANRVGIYWGOBRMRRTQNA="
    test_urn = UrnHandler()
    test_value = test_urn.apply_b32_hash(test_case_sha256_hash)
    log.debug("||Value received from app_handler: %s||", test_value)
    assert test_value == test_case_b32_hash
    log.debug("||End test cases.||")
