#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_student.py
-------------

Description: Contains the test cases for the Student class.

Author: Lorenzo .S
Contributors:
Date Created: 03-03-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application
from required_classes.course import Course
from required_classes.student import Student


class TestStudent(unittest.TestCase):
    """
    Docstring for TestStudent
        - Description: Contains unit tests for the Student class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestStudent.setUp()
            - Description: Creates fresh Student and Course objects before each test.
            - Author: Lorenzo .S
        """
        self.course1 = Course("CSE2050", 3, 1)
        self.course2 = Course("MATH1010", 2, 1)
        self.course3 = Course("PHYS1401", 4, 1)

        self.student1 = Student("STU00001", "Student_1")
        self.student2 = Student("STU00002", "Student_2", {self.course1: "A"})

    # ===== Test __init__ =====

    def test_init(self):
        """
        Docstring for TestStudent.test_init()
            - Description: Tests that Student initializes correctly.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student1.student_id, "STU00001")
        self.assertEqual(self.student1.name, "Student_1")
        self.assertEqual(self.student1.courses, {})

        self.assertEqual(self.student2.student_id, "STU00002")
        self.assertEqual(self.student2.name, "Student_2")
        self.assertEqual(self.student2.courses, {self.course1: "A"})

    def test_invalid_student_id_raises(self):
        """
        Docstring for TestStudent.test_invalid_student_id_raises()
            - Description: Tests invalid student IDs raise ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            Student("BAD001", "Bad Student")

    def test_empty_name_raises(self):
        """
        Docstring for TestStudent.test_empty_name_raises()
            - Description: Tests empty student names raise ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            Student("STU99999", "")

    # ===== Test enroll =====

    def test_enroll(self):
        """
        Docstring for TestStudent.test_enroll()
            - Description: Tests successful enrollment in new courses.
            - Author: Lorenzo .S
        """
        self.student1.enroll(self.course1, "A")
        self.assertEqual(self.student1.courses, {self.course1: "A"})

        self.student2.enroll(self.course2, "B")
        self.assertEqual(
            self.student2.courses,
            {self.course1: "A", self.course2: "B"}
        )

    def test_enroll_already_enrolled(self):
        """
        Docstring for TestStudent.test_enroll_already_enrolled()
            - Description: Tests duplicate enrollment raises ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.student2.enroll(self.course1, "B")

    def test_enroll_invalid_grade(self):
        """
        Docstring for TestStudent.test_enroll_invalid_grade()
            - Description: Tests invalid grades raise ValueError.
            - Author: Lorenzo .S
        """
        invalid_grades = ["8", 8, True, None, "Z", "Fail"]

        for invalid_grade in invalid_grades:
            with self.assertRaises(ValueError):
                self.student2.enroll(self.course2, invalid_grade)

    # ===== Test update_grade =====

    def test_update_grade(self):
        """
        Docstring for TestStudent.test_update_grade()
            - Description: Tests updating an existing course grade.
            - Author: Lorenzo .S
        """
        self.student2.update_grade(self.course1, "B")

        self.assertEqual(self.student2.courses[self.course1], "B")

    def test_update_grade_invalid_course_raises(self):
        """
        Docstring for TestStudent.test_update_grade_invalid_course_raises()
            - Description: Tests updating a course not enrolled in raises ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.student1.update_grade(self.course1, "A")

    def test_update_grade_invalid_grade_raises(self):
        """
        Docstring for TestStudent.test_update_grade_invalid_grade_raises()
            - Description: Tests invalid updated grades raise ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.student2.update_grade(self.course1, "Z")

    # ===== Test calculate_gpa =====

    def test_calculate_gpa(self):
        """
        Docstring for TestStudent.test_calculate_gpa()
            - Description: Tests GPA calculation.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.calculate_gpa(), 4.0)
        self.assertEqual(self.student1.calculate_gpa(), 0.0)

    def test_calculate_gpa_multiple_courses(self):
        """
        Docstring for TestStudent.test_calculate_gpa_multiple_courses()
            - Description: Tests GPA calculation across multiple courses.
            - Author: Lorenzo .S
        """
        self.student2.enroll(self.course2, "B")
        self.student2.enroll(self.course3, "C")

        gpa = self.student2.calculate_gpa()

        self.assertGreater(gpa, 0.0)
        self.assertLess(gpa, 4.0)

    # ===== Test get_course_info =====

    def test_get_course_info(self):
        """
        Docstring for TestStudent.test_get_course_info()
            - Description: Tests retrieving student course information.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.get_course_info(),[{"course_code": "CSE2050","grade": "A","credits": 3}])

        self.student2.enroll(self.course2, "B")

        self.assertEqual(self.student2.get_course_info(),[{"course_code": "CSE2050","grade": "A","credits": 3},{"course_code": "MATH1010","grade": "B","credits": 2}])

        self.assertEqual(self.student1.get_course_info(), [])


if __name__ == "__main__":
    unittest.main()