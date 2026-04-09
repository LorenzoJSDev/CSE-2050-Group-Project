#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_enrollment_record.py
-------------

Description: Contains the test cases for the EnrollmentRecord class.

Author: Lorenzo .S
Contributors:
Date Created: 04-08-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest
import datetime

# Local application (your project modules)
from required_classes.data_structures.enrollment_record import EnrollmentRecord
from required_classes.student import Student


# ==== Classes ==== #
class TestEnrollmentRecord(unittest.TestCase):
    """
    Docstring for TestEnrollmentRecord.
        - Description: Contains the test cases for the EnrollmentRecord class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestEnrollmentRecord.setUp()
            - Description: Sets up objects for testing.
            - Author: Lorenzo .S
        """
        self.student = Student("STU00001", "John Doe")
        self.custom_date = datetime.date(2026, 4, 8)

    # ---- Test EnrollmentRecord.__init__() ---- #

    def test_init_with_date(self):
        """
        Docstring for TestEnrollmentRecord.test_init_with_date()
            - Description: Tests initialization with a provided enrollment date.
            - Author: Lorenzo .S
        """
        record = EnrollmentRecord(self.student, self.custom_date)

        self.assertEqual(record.student, self.student)
        self.assertEqual(record.enroll_date, self.custom_date)

    def test_init_default_date(self):
        """
        Docstring for TestEnrollmentRecord.test_init_default_date()
            - Description: Tests initialization when no enrollment date is provided.
            - Author: Lorenzo .S
        """
        today = datetime.date.today()
        record = EnrollmentRecord(self.student)

        self.assertEqual(record.student, self.student)
        self.assertEqual(record.enroll_date, today)

    # ---- Test EnrollmentRecord.__repr__() ---- #

    def test_repr(self):
        """
        Docstring for TestEnrollmentRecord.test_repr()
            - Description: Tests the string representation of the EnrollmentRecord.
            - Author: Lorenzo .S
        """
        record = EnrollmentRecord(self.student, self.custom_date)

        expected_string = f"{self.student}, {self.custom_date}"
        self.assertEqual(repr(record), expected_string)


if __name__ == "__main__":
    unittest.main()