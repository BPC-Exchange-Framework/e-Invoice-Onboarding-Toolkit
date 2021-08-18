"""
Sandbox of test cases.
"""
# test_k1.py
# from einvoice.einvoice.app_handler import UrnHandler
from einvoice.urn import Urn
from einvoice.app_handler import UrnHandler
from einvoice.app_logging import create_logger


def test_case_1():
    """Kelly's proto-test case 1"""
    log = create_logger("test_case_1")
    log.debug("Begin test case 1")
    _test_create_urn = UrnHandler()
    _test_values = _test_create_urn.create_urn_lookup("0123456789")
    # print(_test_values)
    log.debug("Test values %s", _test_values)
    assert _test_values == "urn:oasis:names:tc:ebco"\
        "re:partyid-type:iso6523::0123456789"


def test_case_2():
    """Kelly's proto-test case 2"""
    log = create_logger("test_case_2")
    specification = "urn:oasis:names:tc:ebcore:partyid-type"
    schema = "iso6523"
    party_id = "0123456789"
    test_urn = Urn(specification, schema, party_id)
    result = test_urn.urn()
    log.debug("Data type of result: %s", str(type(result)))
    log.debug("Result: %s", str(result))
    assert result == "urn:oasis:names:tc:ebco"\
        "re:partyid-type:iso6523::0123456789"
