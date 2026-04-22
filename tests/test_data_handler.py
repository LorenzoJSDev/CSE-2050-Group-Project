#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_data_handler.py
-------------

Description: Contains the tests cases for the DataHandler class.

Author: Lorenzo .S
Contributors:
Date Created: 04-08-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest
import os
import datetime

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
        self.university_data_file = open("csv_files/milestone_2_university_data(in).csv", mode='r', newline='',
                                         encoding="utf-8")
        self.course_catalog_file = open("csv_files/milestone_2_course_catalog_CSE10_with_capacity(in).csv", mode='r',
                                        newline='', encoding="utf-8")
        self.enrollment_file = open("csv_files/milestone_2_enrollments_CSE10(in).csv", mode='r', newline='',
                                    encoding="utf-8")
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

    # ---- Test DataHandler.load_course_catalog() ---- #

    def test_load_course_catalog(self):
        """
        Docstring for TestDataHandler.test_load_course_catalog()
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
            course = self.data_handler1.university_obj.get_course(course_code)
            self.assertIsInstance(course, Course)
            self.assertGreater(course.capacity, 0)

    # ---- Test DataHandler.load_university_data() ---- #

    def test_load_university_data(self):
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

    # ---- Test DataHandler.load_enrollment_data() ---- #

    def test_load_enrollment_data(self):
        """
        Docstring for TestDataHandler.test_load_enrollment_data()
            - Description: Tests that the data from enrollment data is loaded properly into the university object.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()
        self.assertEqual(self.data_handler1.enrollment_file, self.enrollment_file)

        self.data_handler1.load_enrollment_data()

        course = self.data_handler1.university_obj.get_course("CSE2050")
        self.assertIsInstance(course, Course)

        total_processed = len(course.enrolled) + len(course.waitlist)
        self.assertGreaterEqual(total_processed, 0)

        for record in course.enrolled:
            self.assertIsInstance(record.student, Student)
            self.assertIsInstance(record.enroll_date, datetime.date)

    # ---- Test DataHandler.query_list_of_enrolled_students() ---- #

    def test_query_list_of_enrolled_students_invalid_course(self):
        """
        Docstring for TestDataHandler.test_query_list_of_enrolled_students_invalid_course()
            - Description: Tests that querying a non-existent course returns the correct message.
            - Author: Lorenzo .S
        """
        result = self.data_handler1.query_list_of_enrolled_students("CSE9999")
        self.assertEqual(result, "CSE9999 is not a registered course.")

    # ---- Test DataHandler.query_student_gpa() ---- #

    def test_query_student_gpa_invalid_student(self):
        """
        Docstring for TestDataHandler.test_query_student_gpa_invalid_student()
            - Description: Tests that querying GPA for a non-existent student returns the correct message.
            - Author: Lorenzo .S
        """
        result = self.data_handler1.query_student_gpa("STU99999")
        self.assertEqual(result, "STU99999 is not a registered student.")

    def test_query_student_gpa(self):
        """
        Docstring for TestDataHandler.test_query_student_gpa()
            - Description: Tests that querying GPA for a valid student returns a string.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()

        result = self.data_handler1.query_student_gpa("STU00001")
        self.assertIsInstance(result, str)
        self.assertIn("STU00001", result)

    # ---- Test DataHandler.query_student_courses_and_course_info() ---- #

    def test_query_student_courses_and_course_info_invalid_student(self):
        """
        Docstring for TestDataHandler.test_query_student_courses_and_course_info_invalid_student()
            - Description: Tests that querying course info for a non-existent student returns the correct message.
            - Author: Lorenzo .S
        """
        result = self.data_handler1.query_student_courses_and_course_info("STU99999")
        self.assertEqual(result, "STU99999 is not a registered student.")

    # ---- Test DataHandler.query_university_gpa_mean_and_median() ---- #

    def test_query_university_gpa_mean_and_median(self):
        """
        Docstring for TestDataHandler.test_query_university_gpa_mean_and_median()
            - Description: Tests that university GPA mean and median are returned in a dataframe.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()

        result = self.data_handler1.query_university_gpa_mean_and_median()

        self.assertEqual(list(result.columns), ["Mean", "Median"])
        self.assertEqual(len(result), 1)

    # ---- Test DataHandler.query_common_students_in_two_courses() ---- #

    def test_query_common_students_in_two_courses(self):
        """
        Docstring for TestDataHandler.test_query_common_students_in_two_courses()
            - Description: Tests that querying common students between two courses returns either a dataframe or a valid message.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()
        self.data_handler1.load_enrollment_data()

        result = self.data_handler1.query_common_students_in_two_courses("CSE2050", "CSE3100")

        valid_message = "There are no common students in CSE2050 and CSE3100"

        self.assertTrue(
            hasattr(result, "columns") or result == valid_message
        )


if __name__ == "__main__":
    unittest.main()