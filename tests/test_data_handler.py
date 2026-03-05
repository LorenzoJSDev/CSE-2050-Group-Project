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
import io

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
        self.university_data_file = open("csv_files/university_data(in).csv",mode='r',newline='', encoding="utf-8")
        self.course_catalog_file = open("csv_files/course_catalog(in).csv",mode='r',newline='', encoding="utf-8")
        self.data_handler1 = DataHandler(self.university_data_file, self.course_catalog_file)
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


    # ---- Test DataHandler.__init__() ---- #

    def test_init(self):
        """
        Docstring for TestDataHandler.test_init()
            - Description: Tests that the data handler object is initialized properly.
            - Author: Lorenzo .S
        """

        self.assertEqual(self.data_handler1.university_data_file, self.university_data_file)
        self.assertEqual(self.data_handler1.course_catalog_file, self.course_catalog_file)
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
        self.assertEqual(list(self.data_handler1.university_obj.courses.keys()), ['CSE1010', 'CSE2050', 'CSE3100', 'MATH1010', 'MATH2010', 'PHYS1010', 'PHYS2010', 'BIO1010', 'CHEM1010', 'ENG1010', 'ECON1010', 'PSYCH1010', 'BUS1010'])

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



if __name__ == "__main__":
    unittest.main()
