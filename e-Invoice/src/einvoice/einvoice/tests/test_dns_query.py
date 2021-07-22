import json
from src.einvoice.einvoice.dns_query import get_registry_entry_fqdn

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

    