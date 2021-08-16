# test_k1.py
from einvoice.app_handler import CreateUrn
# from app_logging import create_logger

def test_case_1():
    _test_create_urn = CreateUrn()
    _test_values = _test_create_urn.create_urn_lookup("0123456789")
    print(_test_values)
    assert 1 == 1
