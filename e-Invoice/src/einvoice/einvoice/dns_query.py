def get_registry_entry_fqdn(unaptr_response: dict) -> str:
    return unaptr_response.get("registry_entry_fqdn", "")