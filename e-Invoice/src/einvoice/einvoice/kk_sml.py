from dataclasses import dataclass
from json import dumps
from kk_log import create_logger
import hashlib
import base64


ulog = create_logger("urn_logger")
ulog.info("Creating urn")

def writeURNtoJSON(_smlurn, _f_n):
    """Write the urn values to a file"""
    ulog.debug("Writing urn to file.")
    json_str = dumps(_smlurn.__dict__)
    with open(_f_n, "w") as f:
        f.write(json_str)

@dataclass
class SMLURN:
    prty_id_spec: str = "urn:oasis:names:tc:ebcore:partyid-type"
    prty_id_schma_type: str = "iso6523"
    prty_id: str = "0123456789"
        
    def prty_urn(self) -> str:
        """Construct string for the party's URN"""
        return self.prty_id_spec + ":" + self.prty_id_schma_type + "::" \
            + self.prty_id


def apply256Hash(_data):
    """Applys SHA256 hash to the lookup"""
    encoded_data = _data.encode()
    hash256 = hashlib.sha256(encoded_data)
    output = hash256.hexdigest()
    return output


def applyBase32(_hash):
    """Apply Base32 encoding per the spec"""
    b_string = _hash.encode("utf-8")
    output = base64.b32encode(b_string)
    return output


myurn = SMLURN("urn:oasis:names:tc:ebcore:partyid-type", "iso6523", "0123456789")
urn = myurn.prty_urn()
# print(urn)
# msg = ("Creating urn %s" % urn)
ulog.debug("Creating urn %s" % urn)
hurshed = apply256Hash(urn)
ulog.debug("shaw256 hash applied")
# ulog.debug("The shaw256 hash of the urn: %s" % hurshed)
bhurshed = applyBase32(hurshed) 
ulog.debug("The Base32 verison: %s" % bhurshed)
writeURNtoJSON(myurn,"./smlurn.json")
