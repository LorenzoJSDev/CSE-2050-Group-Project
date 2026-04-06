#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
enrollment_record.py
-------------

Description: Contains the EnrollmentRecord class for Milestone 2

Author: Lorenzo .S
Contributors: Jerod Abraham
Date Created: 04-06-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library


# Third-party


# Local application (your project modules)
from required_classes.student import Student

class EnrollmentRecord:
    def __init__(self, student: Student):
        self.student = student
        self.enroll_date = None

    pass