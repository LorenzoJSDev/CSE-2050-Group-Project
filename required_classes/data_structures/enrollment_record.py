#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
enrollment_record.py
-------------

Description: Contains the EnrollmentRecord class for Milestone 2

Author: Lorenzo .S
Date Created: 04-06-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library
import datetime

# Third-party


# Local application (your project modules)


class EnrollmentRecord:
    """
    Docstring for EnrollmentRecord class
        - Description: The EnrollmentRecord class for the Milestone Two project
        - Author: Lorenzo .S
    """

    def __init__(self, student: object, enroll_date=None) -> None:
        """
        Docstring for EnrollmentRecord.__init__()
         - Description: This constructor creates the EnrollmentRecord class instance
         - Author: Lorenzo .S
        """
        if enroll_date is None:
            enroll_date = datetime.date.today()

        self.student = student
        self.enroll_date = enroll_date
        return

    def __repr__(self):
        """
        Docstring for EnrollmentRecord.__repr__()
            - Description: This method creates a string representation of the EnrollmentRecord
            - Author: Lorenzo .S
        """
        return f"{self.student}, {self.enroll_date}"