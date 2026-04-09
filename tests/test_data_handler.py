#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_data_handler.py
-------------

Description: Contains the tests cases for the DataHandler class.

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application (your project modules)
from data_handler import DataHandler
from required_classes.course import Course
from required_classes.student import Student
from required_classes.university import University


# ==== Classes ==== #
class TestDataHandler(unittest.TestCase):
    """
    Docstring for TestDataHandler.
        - Description: Contains the tests cases for the DataHandler class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestDataHandler.setUp()
            - Description: Sets up the objects for testing.
            - Author: Lorenzo .S
        """
        self.university_data_file = open("csv_files/milestone_2_university_data(in).csv", mode='r', newline='', encoding="utf-8")
        self.course_catalog_file = open("csv_files/milestone_2_course_catalog_CSE10_with_capacity(in).csv", mode='r', newline='', encoding="utf-8")
        self.enrollment_file = open("csv_files/milestone_2_enrollments_CSE10(in).csv", mode='r', newline='', encoding="utf-8")
        self.data_handler1 = DataHandler(self.university_data_file, self.course_catalog_file, self.enrollment_file)
        return

    def tearDown(self):
        """
        Docstring for TestDataHandler.tearDown()
            - Description: Closes files after every test.
            - Author: Lorenzo .S
        :return:
        """
        self.university_data_file.close()
        self.course_catalog_file.close()
        self.enrollment_file.close()

    # ---- Test DataHandler.__init__() ---- #

    def test_init(self):
        """
        Docstring for TestDataHandler.test_init()
            - Description: Tests that the data handler object is initialized properly.
            - Author: Lorenzo .S
        """

        self.assertEqual(self.data_handler1.university_data_file, self.university_data_file)
        self.assertEqual(self.data_handler1.course_catalog_file, self.course_catalog_file)
        self.assertEqual(self.data_handler1.enrollment_file, self.enrollment_file)
        self.assertIsInstance(self.data_handler1.university_obj, University)
        self.assertEqual(self.data_handler1.university_obj.courses, {})
        self.assertEqual(self.data_handler1.university_obj.students, {})

    # ---- Test DataHandler.load_course_catalog_data() ---- #

    def test_load_course_catalog(self):
        """
        Docstring for TestDataHandler.test_load_university_data()
            - Description: Tests that the data from course catalog is loaded properly into the university object.
            - Author: Lorenzo .S
        """

        self.assertEqual(self.data_handler1.course_catalog_file, self.course_catalog_file)
        self.data_handler1.load_course_catalog()

        expected_courses = [
            'CSE1010', 'CSE2050', 'CSE2102', 'CSE2500', 'CSE2600',
            'CSE3100', 'CSE3140', 'CSE3150', 'CSE3500', 'CSE3666'
        ]

        self.assertEqual(list(self.data_handler1.university_obj.courses.keys()), expected_courses)

        for course_code in expected_courses:
            self.assertIsInstance(self.data_handler1.university_obj.get_course(course_code), Course)

    # ---- Test DataHandler.load_university_data() ---- #

    def test_load_university(self):
        """
        Docstring for TestDataHandler.test_load_university_data()
            - Description: Tests that the data from university data is loaded properly into the university object.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.assertEqual(self.data_handler1.university_data_file, self.university_data_file)
        self.data_handler1.load_university_data()
        self.assertEqual(list(self.data_handler1.university_obj.students.keys())[2], 'STU00003')
        self.assertIsInstance(self.data_handler1.university_obj.get_student('STU00001'), Student)


if __name__ == "__main__":
    unittest.main()