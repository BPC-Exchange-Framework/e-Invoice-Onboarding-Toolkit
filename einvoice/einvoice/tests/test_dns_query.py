"""
Test cases for dns_query

"""
# pylint: disable=C0415, E0401, W1514
# import outside toplevel (os), unable to import 'dovenv',
# using open without explicitly specifying an encoding
from einvoice.dns_query import naptr_lookup

def test_naptr_lookup():
    test_urn = "6c24uvqpxrfyweqimfxmsuym3bbjvoikuwmmidquz2a2zzyikdya"
    test_domain = "sc-b2b.us"
    query_object = DNSQuery()
    uri = query_object.naptr_lookup(test_urn, test_domain)


# def test_get_registry_entry_fqdn():
#     """ Test registry entry fqdn"""
#     # sample_data_path = "einvoice/einvoice/tests/sampl"\
#     #     "e_data/unaptr_response.json"

#     sample_data_path = "./unaptr_response.json"

#     # Test retrieval from a valid unaptr response
#     with open(sample_data_path) as fname:
#         sample_unaptr_response = json.load(fname)
#         expected_ref_value = "jfw63g2zdjoljk4y2h5tzed6mqeqcncjbxk7"\
#             "ekbn6pjphjfkejfq.aisaac.us"
#         actual_ref_value = get_registry_entry_fqdn(sample_unaptr_response)
#         assert actual_ref_value == expected_ref_value

#     # Test retrieval from an invalid unaptr response
#     invalid_unaptr_response = {
#         "invalid_key": "akdkdlslakkd"
#     }
#     expected_ref_value = ""
#     actual_ref_value = get_registry_entry_fqdn(invalid_unaptr_response)
#     assert actual_ref_value == expected_ref_value


# def test_smp_config():
#     """ Test the SMP config"""
#     import os
#     from os.path import join, dirname
#     from dotenv import load_dotenv
#     dotenv_path = join(dirname(__file__), '../.env')
#     load_dotenv(dotenv_path)
#
#     party_id = os.getenv("PARTY_ID")
#     party_id_schema = os.getenv("PARTY_ID_SCHEMA")
#     smp_endpoint_url = os.getenv("SMP_ENDPOINT_URL")
#     post_url = os.getenv("POST_URL")
#     x_api_key = os.getenv("X-API-KEY")
#
#     from einvoice.conf.smp_config import SMP_CONFIG
#     assert SMP_CONFIG["party_id"] == party_id
#     assert SMP_CONFIG["party_id_schema"] == party_id_schema
#     assert SMP_CONFIG["smp_endpoint_url"] == smp_endpoint_url
#     assert SMP_CONFIG["post_url"] == post_url
#     assert SMP_CONFIG["api_key"] == x_api_key
#
#
# def test_configure_smp_body():
#     """Test configuration of smp body"""
#     smp_body = configure_smp_body()
#     smp_body_dict = json.loads(smp_body)
#     assert "party_id" in smp_body_dict.keys()
#     assert "party_id_schema" in smp_body_dict.keys()
#     assert "smp_endpoint_url" in smp_body_dict.keys()
