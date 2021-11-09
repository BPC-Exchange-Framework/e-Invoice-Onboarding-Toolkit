#!/usr/bin/env python3
# pylint: disable=R0903
# Too few public methods.
# File: create_urn_id.py
# About: Generate a unique identifier for the einvoice to use to
# track through the process.
# Development: Kelly Kinney, Leo Rubiano
# Date: 2021-11-05 (November 11th, 2021)
"""This class creates a random 10 character alphanumeric id to
track the request
through the process end-to-end."""
import secrets
import string
from einvoice.app_logging import create_logger


class CreateTrackingID:
    """Class to create a tracking Id for the einvoice."""

    def __init__(self):
        """Entry point into the application and define variables upon
        class instantiation."""
        self.log = create_logger("create_tracking_id")
        self.tracking_id = ""
        self.alphabet = string.ascii_uppercase + string.digits
        self.log.info(
            "Created domain of allowed characters for tracking id: %s",
            self.alphabet
        )

    def create_tracking_id(self, id_size):
        """Creates a completely random uuid not associated with mac address,
        node or timestamp."""
        for _ in range(id_size):
            self.tracking_id = self.tracking_id +\
                (secrets.choice(self.alphabet))
        return self.tracking_id
