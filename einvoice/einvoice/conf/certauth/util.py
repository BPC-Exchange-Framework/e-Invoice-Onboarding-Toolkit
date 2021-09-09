# certauth.util.py
from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID

def make_x509_name(country, state, locality, org, hostname):
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, org),
        x509.NameAttribute(NameOID.COMMON_NAME, hostname),
    ])

    return subject

def date_range(expire_in_days):
    # Return a date range starting from now for N days
    valid_from = datetime.utcnow()
    valid_to = valid_from + timedelta(days=expire_in_days)

    return valid_from, valid_to

def make_builder(subject, issuer, is_ca=False):
    # Expire this certificate 30 days from now
    valid_from,valid_to = date_range(3650)

    # Chain-call certificate builder with necessary parameters
    builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .serial_number(x509.random_serial_number())
        .not_valid_before(valid_from)
        .not_valid_after(valid_to)
    )

    if is_ca:
        builder = builder.add_extension(x509.BasicConstraints(ca=True,
            path_length=None), critical=True)

    return builder
