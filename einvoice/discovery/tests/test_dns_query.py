"""
Test cases for dns_query

"""
# pylint: disable=C0415, E0401, W1514, W0611
# import outside toplevel (os), unable to import 'dotvenv',
# using open without explicitly specifying an encoding


def test_smp_config():
    """ Test the SMP config"""
    import os
    from os.path import join, dirname
    from dotenv import load_dotenv
    dotenv_path = join(dirname(__file__), '../../.env')
    load_dotenv(dotenv_path)

    party_id = os.getenv("PARTY_ID")
    party_id_schema = os.getenv("PARTY_ID_SCHEMA")
    smp_endpoint_url = os.getenv("SMP_ENDPOINT_URL")
    post_url = os.getenv("POST_URL")
    x_api_key = os.getenv("X-API-KEY")

    from einvoice.discovery.conf.smp_config import SMP_CONFIG
    assert SMP_CONFIG["party_id"] == party_id
    assert SMP_CONFIG["party_id_schema"] == party_id_schema
    assert SMP_CONFIG["smp_endpoint_url"] == smp_endpoint_url
    assert SMP_CONFIG["post_url"] == post_url
    assert SMP_CONFIG["api_key"] == x_api_key
