#!/usr/bin/env python3
#
# File: test_ei_handler.py
# About: e-Invoice testing suite; app_handler.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest.

"""
from uuid import uuid4
from app_logging import create_logger
from app_handler import create_sml_lookup, apply_shaw256_hash, apply_base32_hash

# Creat a logger to use for our own purposes.
log = create_logger("test_app_handler")


# Test the logging fuctionality using built-in Pytest "caplog"
def test_baz(caplog):
    """This is a pytest to validate loggig is writing properly to a log."""
    pytest_logger_1 = create_logger("Pytest_test_logger_1")
    log_test_uuid = str(uuid4())
    log_msg = "Adding uuid to log for testing %s" % log_test_uuid
    pytest_logger_1.debug(log_msg)
    for record in caplog.records:
        assert record.levelname != "CRITITAL"
    assert log_test_uuid in caplog.text


# Another quick test of the log functionality as a baseline - has handlers.
def test_logger():
    """This is a pytest to validate the log handlers are being created."""
    pytest_logger_2 = create_logger("Pytest_test_logger_2")
    assert pytest_logger_2.hasHandlers()


# Test core dataclass structure, creation and construction of urn
def test_smlurn_default(
    _test_case_id="Default",
    _test_case_id_spec="urn:oasis:names:tc:ebcore:partyid-type",
    _test_case_party_schema_type="iso6523",
    _test_case_party_id="0123456789",
):
    """Default test case."""
    log_msg = "Created default test case"
    log.debug(log_msg)
    smlurn = create_sml_lookup(
        _test_case_id_spec, _test_case_party_schema_type, _test_case_party_id
    )
    assert smlurn.party_id_specification == "urn:oasis:names:tc:ebcore:"\
        "partyid-type"
    assert smlurn.party_id_schema_type == "iso6523"
    assert smlurn.party_id == "0123456789"
    value_final_urn = (
        smlurn.party_id_specification
        + ":"
        + smlurn.party_id_schema_type
        + "::"
        + smlurn.party_id
    )

    assert (
        smlurn.final_urn == "urn:oasis:names:tc:ebcore:partyid-"
        "type:iso6523::0123456789"
    )
    assert value_final_urn == smlurn.final_urn
    applied_shaw256_hash = apply_shaw256_hash(smlurn).urn_shaw256_hash
    log.debug("Shaw256 hash value is %s", applied_shaw256_hash)
    assert (
        applied_shaw256_hash
        == "f0b5ca560fbc4b8b1208616ec9530cd8429ab90aa598c40e14ce81ace70850f0"
    )
    applied_base32_hash = apply_base32_hash(smlurn)
    assert (
        applied_base32_hash.urn_base32_hash
        == "MYYGENLDME2TMMDGMJRTIYRYMIYTEMBYGYYTMZLDHE2TGMDDMQ4DIMRZ"
        "MFRDSMDBME2TSODDGQYGKMJUMNSTQMLBMNSTOMBYGUYGMMA="
    )


def test_smlurn_1(
    _test_case_id="1",
    _test_case_id_spec="urn:oasis:names:tc:ebcore:partyid-type",
    _test_case_party_schema_type="iso6523",
    _test_case_party_id="EAN-7638725972413",
):
    """Test case #1"""
    log_msg = ("Test case for party id {}", _test_case_party_id)
    log.debug(log_msg)
    smlurn = create_sml_lookup(
        _test_case_id_spec, _test_case_party_schema_type, _test_case_party_id
    )
    assert smlurn.party_id_specification == "urn:oasis:names:tc:"\
        "ebcore:partyid-type"
    assert smlurn.party_id_schema_type == "iso6523"
    assert smlurn.party_id == "EAN-7638725972413"
    value_final_urn = (
        smlurn.party_id_specification
        + ":"
        + smlurn.party_id_schema_type
        + "::"
        + smlurn.party_id
    )

    assert (
        smlurn.final_urn
        == "urn:oasis:names:tc:ebcore:partyid-type:iso6523::EAN-7638725972413"
    )
    assert value_final_urn == smlurn.final_urn
    applied_shaw256_hash = apply_shaw256_hash(smlurn).urn_shaw256_hash
    log_msg = "Shaw256 hash value is %s" % applied_shaw256_hash
    log.debug(log_msg)
    assert (
        applied_shaw256_hash
        == "93bb91efa204b16933652ece6897ebf265cd10f1533d24c127d5dc812e9d9de0"
    )
    applied_base32_hash = apply_base32_hash(smlurn)
    assert (
        applied_base32_hash.urn_base32_hash
        == "HEZWEYRZGFSWMYJSGA2GEMJWHEZTGNRVGJSWGZJWHA4TOZLCM"
        "YZDMNLDMQYTAZRRGUZTGZBSGRRTCMRXMQ2WIYZYGEZGKOLEHFSGKMA="
    )


def test_smlurn_2(
    _test_case_id="2",
    _test_case_id_spec="urn:oasis:names:tc:ebcore:partyid-type",
    _test_case_party_schema_type="iso6523",
    _test_case_party_id="bpc-2343030383",
):
    """Test case #2"""
    log_msg = ("Test case for party id {}", _test_case_party_id)
    log.debug(log_msg)
    smlurn = create_sml_lookup(
        _test_case_id_spec, _test_case_party_schema_type, _test_case_party_id
    )
    assert smlurn.party_id_specification == "urn:oasis:names:tc:ebcore:"\
        "partyid-type"
    assert smlurn.party_id_schema_type == "iso6523"
    assert smlurn.party_id == "bpc-2343030383"
    value_final_urn = (
        smlurn.party_id_specification
        + ":"
        + smlurn.party_id_schema_type
        + "::"
        + smlurn.party_id
    )
    assert (
        smlurn.final_urn
        == "urn:oasis:names:tc:ebcore:partyid-type:iso6523::bpc-2343030383"
    )
    assert value_final_urn == smlurn.final_urn
    applied_shaw256_hash = apply_shaw256_hash(smlurn).urn_shaw256_hash
    log_msg = ("Shaw256 hash value is {}", applied_shaw256_hash)
    log.debug(log_msg)
    assert (
        applied_shaw256_hash
        == "ae9520550626abdb6a3d8812bc8cc4925524be6f2614b0cf0b9f8d2855e4179f"
    )
    applied_base32_hash = apply_base32_hash(smlurn)
    assert (
        applied_base32_hash.urn_base32_hash
        == "MFSTSNJSGA2TKMBWGI3GCYTEMI3GCM3EHA4DCMTCMM4GGYZUHEZD"
        "KNJSGRRGKNTGGI3DCNDCGBRWMMDCHFTDQZBSHA2TKZJUGE3TSZQ="
    )


def test_smlurn_(
    _test_case_id="3",
    _test_case_id_spec="urn:oasis:names:tc:ebcore:partyid-type",
    _test_case_party_schema_type="iso6523",
    _test_case_party_id="4035811991021",
):
    """Test case #3"""
    log_msg = ("Test case for party id {}", _test_case_party_id)
    log.debug(log_msg)
    smlurn = create_sml_lookup(
        _test_case_id_spec, _test_case_party_schema_type, _test_case_party_id
    )
    assert smlurn.party_id_specification == "urn:oasis:names:tc:ebcore:"\
        "partyid-type"
    assert smlurn.party_id_schema_type == "iso6523"
    assert smlurn.party_id == "4035811991021"
    value_final_urn = (
        smlurn.party_id_specification
        + ":"
        + smlurn.party_id_schema_type
        + "::"
        + smlurn.party_id
    )
    assert (
        smlurn.final_urn
        == "urn:oasis:names:tc:ebcore:partyid-type:iso6523::4035811991021"
    )
    assert value_final_urn == smlurn.final_urn
    applied_shaw256_hash = apply_shaw256_hash(smlurn).urn_shaw256_hash
    log_msg = ("Shaw256 hash value is {}", applied_shaw256_hash)
    log.debug(log_msg)
    assert (
        applied_shaw256_hash
        == "50e3e2082ac4cc5feee392d27ff8698ce45c49b13741afd5b79306521c81dc84"
    )
    applied_base32_hash = apply_base32_hash(smlurn)
    assert (
        applied_base32_hash.urn_base32_hash
        == "GUYGKM3FGIYDQMTBMM2GGYZVMZSWKZJTHEZGIMRXMZTDQ"
        "NRZHBRWKNBVMM2DSYRRGM3TIMLBMZSDKYRXHEZTANRVGIYWGOBRMRRTQNA="
    )
