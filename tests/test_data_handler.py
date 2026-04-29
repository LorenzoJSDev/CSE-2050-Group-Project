#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_data_handler.py
-------------

Description: Contains test cases for the DataHandler class for Milestone 3.

Author: Lorenzo .S
Contributors:
Date Created: 04-08-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest
import datetime

# Third-party
import pandas as pd

# Local application
from data_handler import DataHandler
from required_classes.course import Course
from required_classes.student import Student
from required_classes.university import University


class TestDataHandler(unittest.TestCase):
    """
    Docstring for TestDataHandler.
        - Description: Contains unit tests for DataHandler loading and query behavior.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestDataHandler.setUp()
            - Description: Opens test CSV files and creates a DataHandler object before each test.
            - Author: Lorenzo .S
        """
        self.university_data_file = open(
            "csv_files/milestone3_university_data.csv",
            mode="r",
            newline="",
            encoding="utf-8"
        )

        self.course_catalog_file = open(
            "csv_files/milestone3_course_catalog_CSE10_with_capacity.csv",
            mode="r",
            newline="",
            encoding="utf-8"
        )

        self.enrollment_file = open(
            "csv_files/milestone_3_enrollments_CSE10.csv",
            mode="r",
            newline="",
            encoding="utf-8"
        )

        self.prerequisite_file = open(
            "csv_files/milestone3_cse_prerequisites.csv",
            mode="r",
            newline="",
            encoding="utf-8"
        )

        self.data_handler1 = DataHandler(
            self.university_data_file,
            self.course_catalog_file,
            self.enrollment_file,
            self.prerequisite_file
        )

    def tearDown(self):
        """
        Docstring for TestDataHandler.tearDown()
            - Description: Closes all opened CSV files after each test.
            - Author: Lorenzo .S
        """
        self.university_data_file.close()
        self.course_catalog_file.close()
        self.enrollment_file.close()
        self.prerequisite_file.close()

    def load_all_data(self):
        """
        Docstring for TestDataHandler.load_all_data()
            - Description: Helper method that loads all project data in the correct Milestone 3 order.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()
        self.data_handler1.load_prerequisite_data()
        self.data_handler1.load_enrollment_data()

    def test_init(self):
        """
        Docstring for TestDataHandler.test_init()
            - Description: Tests that the DataHandler object initializes properly.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.data_handler1.university_data_file, self.university_data_file)
        self.assertEqual(self.data_handler1.course_catalog_file, self.course_catalog_file)
        self.assertEqual(self.data_handler1.enrollment_file, self.enrollment_file)
        self.assertEqual(self.data_handler1.prerequisite_file, self.prerequisite_file)
        self.assertIsInstance(self.data_handler1.university_obj, University)
        self.assertEqual(self.data_handler1.university_obj.courses, {})
        self.assertEqual(self.data_handler1.university_obj.students, {})

    def test_load_course_catalog(self):
        """
        Docstring for TestDataHandler.test_load_course_catalog()
            - Description: Tests that course catalog data loads into the University object.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()

        expected_courses = [
            "CSE1010", "CSE2050", "CSE2102", "CSE2500", "CSE2600",
            "CSE3100", "CSE3140", "CSE3150", "CSE3500", "CSE3666"
        ]

        self.assertEqual(list(self.data_handler1.university_obj.courses.keys()), expected_courses)

        for course_code in expected_courses:
            course = self.data_handler1.university_obj.get_course(course_code)
            self.assertIsInstance(course, Course)
            self.assertGreater(course.capacity, 0)

    def test_load_university_data(self):
        """
        Docstring for TestDataHandler.test_load_university_data()
            - Description: Tests that university student data loads into the University object.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()

        self.assertIn("STU00001", self.data_handler1.university_obj.students)
        self.assertIsInstance(self.data_handler1.university_obj.get_student("STU00001"), Student)

    def test_load_prerequisite_data(self):
        """
        Docstring for TestDataHandler.test_load_prerequisite_data()
            - Description: Tests that prerequisite data loads into Course prerequisite HashMaps.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_prerequisite_data()

        courses_with_prereqs = []

        for course in self.data_handler1.university_obj.courses.values():
            if len(course.prerequisite.keys()) > 0:
                courses_with_prereqs.append(course.course_code)

        self.assertGreater(len(courses_with_prereqs), 0)

    def test_specific_course_has_prerequisite_after_loading(self):
        """
        Docstring for TestDataHandler.test_specific_course_has_prerequisite_after_loading()
            - Description: Tests that at least one course has its prerequisite attached after loading.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_prerequisite_data()

        found_prerequisite = False

        for course in self.data_handler1.university_obj.courses.values():
            if course.prerequisite.keys():
                found_prerequisite = True

        self.assertTrue(found_prerequisite)

    def test_load_enrollment_data(self):
        """
        Docstring for TestDataHandler.test_load_enrollment_data()
            - Description: Tests that enrollment data loads into Course enrolled lists or waitlists.
            - Author: Lorenzo .S
        """
        self.load_all_data()

        total_processed = 0

        for course in self.data_handler1.university_obj.courses.values():
            total_processed += len(course.enrolled)
            total_processed += len(course.waitlist)

        self.assertGreaterEqual(total_processed, 0)

        for course in self.data_handler1.university_obj.courses.values():
            for record in course.enrolled:
                self.assertIsInstance(record.student, Student)
                self.assertIsInstance(record.enroll_date, datetime.date)

    def test_query_list_of_enrolled_students_invalid_course(self):
        """
        Docstring for TestDataHandler.test_query_list_of_enrolled_students_invalid_course()
            - Description: Tests that querying an invalid course returns the correct message.
            - Author: Lorenzo .S
        """
        result = self.data_handler1.query_list_of_enrolled_students("CSE9999")
        self.assertEqual(result, "CSE9999 is not a registered course.")

    def test_query_student_gpa_invalid_student(self):
        """
        Docstring for TestDataHandler.test_query_student_gpa_invalid_student()
            - Description: Tests that querying GPA for an invalid student returns the correct message.
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

    def test_query_student_courses_and_course_info_invalid_student(self):
        """
        Docstring for TestDataHandler.test_query_student_courses_and_course_info_invalid_student()
            - Description: Tests that querying course info for an invalid student returns the correct message.
            - Author: Lorenzo .S
        """
        result = self.data_handler1.query_student_courses_and_course_info("STU99999")
        self.assertEqual(result, "STU99999 is not a registered student.")

    def test_query_university_gpa_mean_and_median(self):
        """
        Docstring for TestDataHandler.test_query_university_gpa_mean_and_median()
            - Description: Tests that university GPA statistics return a DataFrame.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()

        result = self.data_handler1.query_university_gpa_mean_and_median()

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(list(result.columns), ["Mean", "Median"])
        self.assertEqual(len(result), 1)

    def test_query_common_students_in_two_courses(self):
        """
        Docstring for TestDataHandler.test_query_common_students_in_two_courses()
            - Description: Tests that querying common students returns a DataFrame or valid message.
            - Author: Lorenzo .S
        """
        self.load_all_data()

        result = self.data_handler1.query_common_students_in_two_courses("CSE2050", "CSE3100")
        valid_message = "There are no common students in CSE2050 and CSE3100"

        self.assertTrue(isinstance(result, pd.DataFrame) or result == valid_message)

    def test_query_waitlist_for_course(self):
        """
        Docstring for TestDataHandler.test_query_waitlist_for_course()
            - Description: Tests that querying a waitlist returns a DataFrame or valid no-waitlist message.
            - Author: Lorenzo .S
        """
        self.load_all_data()

        result = self.data_handler1.query_waitlist_for_course("CSE2050")
        valid_message = "There are currently no students on the waitlist for CSE2050."

        self.assertTrue(isinstance(result, pd.DataFrame) or result == valid_message)

    def test_query_course_enrollment_status(self):
        """
        Docstring for TestDataHandler.test_query_course_enrollment_status()
            - Description: Tests that course enrollment status returns the expected DataFrame columns.
            - Author: Lorenzo .S
        """
        self.load_all_data()

        result = self.data_handler1.query_course_enrollment_status("CSE2050")

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(
            list(result.columns),
            ["course_code", "enrolled_count", "capacity", "available_seats", "waitlist_count"]
        )

    def test_query_prerequisites_for_course(self):
        """
        Docstring for TestDataHandler.test_query_prerequisites_for_course()
            - Description: Tests that prerequisite query returns a DataFrame or no-prerequisite message.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_prerequisite_data()

        result = self.data_handler1.query_prerequisites_for_course("CSE2050")
        valid_message = "CSE2050 does not have any listed prerequisites."

        self.assertTrue(isinstance(result, pd.DataFrame) or result == valid_message)

    def test_query_student_prerequisite_eligibility(self):
        """
        Docstring for TestDataHandler.test_query_student_prerequisite_eligibility()
            - Description: Tests that prerequisite eligibility returns a DataFrame with eligibility information.
            - Author: Lorenzo .S
        """
        self.data_handler1.load_course_catalog()
        self.data_handler1.load_university_data()
        self.data_handler1.load_prerequisite_data()

        result = self.data_handler1.query_student_prerequisite_eligibility("STU00001", "CSE2050")

        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn("eligible", result.columns)


if __name__ == "__main__":
    unittest.main()