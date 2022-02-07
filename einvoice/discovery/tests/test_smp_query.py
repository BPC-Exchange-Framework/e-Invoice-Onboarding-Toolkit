#!/usr/bin/env python3
# pylint: disable=C0301
#
# long lines of test data
# File: test_smp_query.py
# About: e-Invoice testing suite; smp_query.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-11-18 (November 18th, 2021)
#
"""This is a test file to be run using pytest."""
from einvoice.discovery.smp_query import SMPQuery


def test_smp_query():
    """Test smp_query."""
    urns = (
        "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::kellytestsmp",
        "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::kelly2021",
        "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::kellysmbtest",
        "urn:oasis:names:tc:ebcore:partyid-type:iso6523:0088::mnkellyk",
    )

    service_group_urls = (
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3A"
        "names%3Atc%3Aebcore%3Apartyid"
        "-type%3Aiso6523%3A0088%3A%3Akellytestsmp",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames"
        "%3Atc%3Aebcore%3Apartyid-type%"
        "3Aiso6523%3A0088%3A%3Akelly2021",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames%"
        "3Atc%3Aebcore%3Apartyid-type%3Ais"
        "o6523%3A0088%3A%3Akellysmbtest",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames"
        "%3Atc%3Aebcore%3Apartyid-type%"
        "3Aiso6523%3A0088%3A%3Amnkellyk",    # flake8: noqa: E501
    )

    service_urls = (
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Aname"
        "s%3Atc%3Aebcore%3Apartyid-type%"
        "3Aiso6523%3A0088%3A%3Akellytestsmp/services/bdx-doci"
        "d-qns%3A%3Aurn%3Aoasis%3Anames%3Aspecification%3A"
        "ubl%3Aschema%3Axsd%3AInvoice-1"
        "%3A%3AInvoice%23%23BPC-UBL-2.2",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-"
        "smp-2/urn%3Aoasis%3Anames%3Atc%3Aebc"
        "ore%3Apartyid-type%3Aiso6523%3A0"
        "088%3A%3Akelly2021/services/bd"
        "x-docid-qns%3A%3Aurn%3Aoasis%3"
        "Anames%3Aspecification%3Aubl%3"
        "Aschema%3Axsd%3AInvoice-1%3"
        "A%3AInvoice%23%23BPC-UBL-2.2",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-smp-"
        "2/urn%3Aoasis%3Anames%3Atc%3Aebcore%3A"
        "partyid-type%3Aiso6523%3A0"
        "088%3A%3Akellysmbtest/services/bdx-"
        "docid-qns%3A%3Aurn%3Aoasis%"
        "3Anames%3Aspecification%3A"
        "ubl%3Aschema%3Axsd%3AInvoice-1"
        "%3A%3AInvoice%23%23BPC-UBL-2.2",    # flake8: noqa: E501
        "https://smp-api.sc-b2b.us/bdxr-smp-2/urn%3Aoasis%3Anames"
        "%3Atc%3Aebcore%3Apartyid-type%3Aiso6"
        "523%3A0088%3A%3Amnkellyk/services/bdx-docid-qns%3"
        "A%3Aurn%3Aoasis%3Anames%3Aspec"
        "ification%3Aubl%3Aschema%3Axsd%3AInvoice-1%3A"
        "%3AInvoice%23%23BPC-UBL-2.2",    # flake8: noqa: E501
    )

    query = SMPQuery()
    for index, urn in enumerate(urns):
        service_group_url_test = query.smp_create_srvc_group_url_query(urn)
        service_url_test = query.smp_create_service_url_query(urn)
        assert service_group_url_test == service_group_urls[index]
        print(query.smp_execute_qry(service_group_url_test))
        assert service_url_test == service_urls[index]
        print(query.smp_execute_qry(service_url_test))
