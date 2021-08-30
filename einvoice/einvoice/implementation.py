#!/usr/bin/env python3
# #from urn import Urn
from urn_hasher import Hasher
from app_logging import create_logger

log = create_logger("implementation")
log.info("Created implementation")

specification = "urn:oasis:names:tc:ebcore:partyid-type:unregistered:myscheme"
schema = "BPC01"
party_id = "bpcBusid01"

my_hasher = Hasher()
my_hash_dictionary = my_hasher.hasher(specification, schema, party_id)
print(my_hash_dictionary)
