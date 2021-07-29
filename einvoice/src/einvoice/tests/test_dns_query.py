import json
from src.einvoice.einvoice.dns_query import (
    get_registry_entry_fqdn,
    configure_smp_body,
)

def test_get_registry_entry_fqdn():
    sample_data_path = "e-Invoice/src/einvoice/einvoice/tests/sample_data/unaptr_response.json"
    
    # Test retrieval from a valid unaptr response
    with open(sample_data_path) as f:
        sample_unaptr_response = json.load(f)
        expected_ref_value = "jfw63g2zdjoljk4y2h5tzed6mqeqcncjbxk7ekbn6pjphjfkejfq.aisaac.us"
        actual_ref_value = get_registry_entry_fqdn(sample_unaptr_response)
        assert actual_ref_value == expected_ref_value

    # Test retrieval from an invalid unaptr response
    invalid_unaptr_response = {
        "invalid_key": "akdkdlslakkd"
    }
    expected_ref_value = ""
    actual_ref_value = get_registry_entry_fqdn(invalid_unaptr_response)
    assert actual_ref_value == expected_ref_value

def test_smp_config():
    import os 
    from os.path import join, dirname
    from dotenv import load_dotenv
    dotenv_path = join(dirname(__file__), '../.env')
    load_dotenv(dotenv_path)
    
    party_id = os.getenv("PARTY_ID")
    party_id_schema = os.getenv("PARTY_ID_SCHEMA")
    smp_endpoint_url = os.getenv("SMP_ENDPOINT_URL")
    post_url = os.getenv("POST_URL")
    x_api_key = os.getenv("X-API-KEY")

    from src.einvoice.einvoice.conf.smp_config import SMP_CONFIG
    assert SMP_CONFIG["party_id"] == party_id
    assert SMP_CONFIG["party_id_schema"] == party_id_schema
    assert SMP_CONFIG["smp_endpoint_url"] == smp_endpoint_url
    assert SMP_CONFIG["post_url"] == post_url
    assert SMP_CONFIG["api_key"] == x_api_key

def test_configure_smp_body():
    smp_body = configure_smp_body()
    smp_body_dict = json.loads(smp_body)
    assert "party_id" in smp_body_dict.keys()
    assert "party_id_schema" in smp_body_dict.keys()
    assert "smp_endpoint_url" in smp_body_dict.keys()