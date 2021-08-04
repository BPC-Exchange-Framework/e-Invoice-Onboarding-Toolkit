import json
from einvoice.conf.smp_config import SMP_CONFIG

def get_registry_entry_fqdn(unaptr_response: dict) -> str:
    return unaptr_response.get("registry_entry_fqdn", "")

def configure_smp_body():
    smp_body_dict = {
        "party_id": SMP_CONFIG["party_id"],
        "party_id_schema": SMP_CONFIG["party_id_schema"],
        "smp_endpoint_url": SMP_CONFIG["smp_endpoint_url"],
    }
    
    return json.dumps(smp_body_dict)

def make_smp_post_request():
    smp_body = configure_smp_body()
    # TODO: finishing configuring POST request using SMP config 