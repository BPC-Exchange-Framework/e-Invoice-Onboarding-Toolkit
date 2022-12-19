#!/usr/bin/env python3
#
# File: test_hasher_hasher.py
# About: E-Invoice testing suite; app_handler.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-07-27 (July 27th, 2021)
#
"""This is a test file to be run using pytest."""
from hashlib import sha256
from base64 import b32encode
from einvoice.discovery.urn_hasher import Hasher
from einvoice.config import Logger


log = Logger().create_logger()


def ash_hash(urn):
    """Test case scenario of the Ash-Hash."""
    return (
        b32encode(sha256(bytes(urn.lower(), "utf-8")).digest()).rstrip(b"=")
        .lower()).decode("utf-8")

#############################################
#
#  Test Case 1
#
#############################################


def hasher_1(test_dict):
    """Test case #1 hasher."""
    log.info("Test case hash_1")
    test_hasher = Hasher()
    test_value = test_hasher.hasher(
         test_dict['spec'], test_dict['schema'], test_dict['party_id'],
         log
    )
    test_case_hash = "yn5tj7bteln4c5o4mtul7yvnq3pwu6dpmipcof4pwcbsd3avvn7a"
    assert test_value.get("urn_hash") == test_case_hash
    test_case_urn = (
        "urn:oasis:names:tc:ebcore:partyid-type:" +
        "unregistered:myscheme:bpc01::bpcbusid01"
    )
    assert test_value.get("final_urn") == test_case_urn
    assert test_value.get("urn_hash") == ash_hash(test_case_urn)
    return test_value

#############################################
#
#  Test Case 2
#
#############################################


def hasher_2(test_dict):
    """Test case #1 hasher."""
    log.info("Test case hash_2")
    test_hasher = Hasher()
    test_value = test_hasher.hasher(
         test_dict['spec'], test_dict['schema'], test_dict['party_id'],
         log
    )
    test_case_hash = (
        "6c24uvqpxrfyweqimfxmsuym3bbjvoikuwmmidquz2a2zzyikdya"
    )
    assert test_value.get("urn_hash") == test_case_hash
    test_case_urn = (
        test_dict['spec'] + ":" + test_dict['schema'] + "::" +
        test_dict['party_id']
    )
    assert test_value.get("final_urn") == test_case_urn
    assert test_value.get("urn_hash") == ash_hash(test_case_urn)
    return test_value

#############################################
#
#  Test Case 3
#
#############################################


def hasher_3(test_dict):
    """Test case #1 hasher."""
    log.info("Test case hash_3")
    test_hasher = Hasher()
    test_value = test_hasher.hasher(
         test_dict['spec'], test_dict['schema'], test_dict['party_id'],
         log
    )
    test_case_hash = "bc2ntkxz42amx3a5rmjbsaesp5ucuc3iciposkd3qwnj6b4wjh2q"
    assert test_value.get("urn_hash") == test_case_hash
    test_case_urn = (
        'urn:oasis:names:tc:ebcore:partyid-type:'
        'iso6523:0088::ean-7638725972413'
    )
    assert test_value.get("final_urn") == test_case_urn
    assert test_value.get("urn_hash") == ash_hash(test_case_urn)
    return test_value

#############################################
#
#  Test Case 4
#
#############################################


def hasher_4(test_dict):
    """Test case #1 hasher."""
    log.info("Test case hash_4")
    test_hasher = Hasher()
    test_value = test_hasher.hasher(
         test_dict['spec'], test_dict['schema'], test_dict['party_id'],
         log
    )
    test_case_hash = "rixkdb2u5xxf7vtieezqvakx5r2bc3iugzeqd35ibeddloeapf6a"
    assert test_value.get("urn_hash") == test_case_hash
    test_case_urn = (
        test_dict['spec'] + ":" + test_dict['schema'] + "::" +
        test_dict['party_id']
    )
    assert test_value.get("final_urn") == test_case_urn
    assert test_value.get("urn_hash") == ash_hash(test_case_urn)
    return test_value

#############################################
#
#  Test Case 5
#
#############################################


def hasher_5(test_dict):
    """Test case #1 hasher."""
    log.info("Test case hash_5")
    test_hasher = Hasher()
    test_value = test_hasher.hasher(
         test_dict['spec'], test_dict['schema'], test_dict['party_id'],
         log
    )
    test_case_hash = "jc4swjyiphrll4gfhlu2edehpwlkmqmsncc2lc3so7m5jvgjkewa"
    assert test_value.get("urn_hash") == test_case_hash
    test_case_urn = (
        test_dict['spec'] + ":" + test_dict['schema'] + "::" +
        test_dict['party_id']
    )
    assert test_value.get("final_urn") == test_case_urn
    assert test_value.get("urn_hash") == ash_hash(test_case_urn)
    return test_value


def test_runner():
    """Executer the test scenarios."""
    test_spec_1 = "urn:oasis:names:tc:ebcore:partyid-type"
    test_schema_1 = "iso6523:0088"

    test_dict_1 = {
        'spec': "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme",
        'schema': "BPC01",
        'party_id':  "bpcBusid01"
    }

    test_dict_2 = {
        'spec': test_spec_1,
        'schema': "iso6523",
        'party_id':  "0123456789"
    }

    test_dict_3 = {
        'spec': test_spec_1,
        'schema': test_schema_1,
        'party_id':  "EAN-7638725972413"
    }

    test_dict_4 = {
        'spec': test_spec_1,
        'schema':  test_schema_1,
        'party_id':  "bpc-2343030383"
    }

    test_dict_5 = {
        'spec': test_spec_1,
        'schema': test_schema_1,
        'party_id':  "4035811991021"
    }

    hasher_1(test_dict_1)

    hasher_2(test_dict_2)

    hasher_3(test_dict_3)

    hasher_4(test_dict_4)

    hasher_5(test_dict_5)
