import json
from src.einvoice.einvoice.conf.smp_config import SMP_CONFIG

def get_registry_entry_fqdn(unaptr_response: dict) -> str:
    return unaptr_response.get("registry_entry_fqdn", "")

def configure_smp_body():
    return json.dumps(SMP_CONFIG)

def make_smp_post_request():
    smp_body = configure_smp_body()
    