#!/usr/bin/env python3
# pylint: disable=C0301
#
# long lines of test data
# File: test_smp_query.py
# About: E-Invoice testing suite; smp_query.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-11-18 (November 18th, 2021)
#
"""This is a test file to be run using pytest."""
from einvoice.discovery.smp_query import SMPQuery
from einvoice.config import Logger


def test_smp_query():
    """Test smp_query."""
    identifier_scheme = "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::"
    smp_url = (
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames%3Atc"
        "%3Aebcore%3Apartyid-type%3Aiso6523%3A0088%3A%3A"
                         )
    service_url = (
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames%3Atc"
        "%3Aebcore%3Apartyid-type%3Aiso6523%3A0088%3A%3A"
                            )
    services = (
        "/services/bdx-docid-qns%3A%3Aurn%3Aoasis%3Anames%3Aspecification"
        "%3Aubl%3Aschema%3Axsd%3AInvoice-1%3A%3AInvoice%23%23BPC-UBL-2.2"
                        )

    urns = (
        identifier_scheme + "kellytestsmp",
        identifier_scheme + "kelly2021",
        identifier_scheme + "kellysmbtest",
        identifier_scheme + "mnkellyk"
    )

    service_group_urls = (
        smp_url + "kellytestsmp",    # flake8: noqa: E501
        smp_url + "kelly2021",    # flake8: noqa: E501
        smp_url + "kellysmbtest",    # flake8: noqa: E501
        smp_url + "mnkellyk",    # flake8: noqa: E501
    )

    service_urls = (
        service_url + "kellytestsmp" + services,    # flake8: noqa: E501
        service_url + "kelly2021" + services,    # flake8: noqa: E501
        service_url + "kellysmbtest" + services,   # flake8: noqa: E501
        service_url + "mnkellyk" + services    # flake8: noqa: E501
    )

    log = Logger().create_logger()

    query = SMPQuery()
    for index, urn in enumerate(urns):
        msg = f"Attempting urn: {urn}"
        log.info(msg)
        service_group_url_test = query.smp_create_srvc_group_url_query(urn,
                                                                       log)
        log.info(service_group_url_test)
        service_url_test = query.smp_create_service_url_query(urn, log)
        assert service_group_url_test == service_group_urls[index]
        log.info(query.smp_execute_qry(service_group_url_test, log))
        assert service_url_test == service_urls[index]
        log.info(query.smp_execute_qry(service_url_test, log))
