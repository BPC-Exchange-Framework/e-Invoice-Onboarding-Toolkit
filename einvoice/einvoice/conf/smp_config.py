import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

SMP_CONFIG = {
    "party_id": os.getenv("PARTY_ID"),
    "party_id_schema": os.getenv("PARTY_ID_SCHEMA"),
    "smp_endpoint_url": os.getenv("SMP_ENDPOINT_URL"),
    "post_url": os.getenv("POST_URL"),
    "api_key": os.getenv("X-API-KEY"),
}
