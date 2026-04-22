#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_student.py
-------------

Description: Contains the tests cases for the Student class.

Author: Lorenzo .S
Contributors:
Date Created: 03-03-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Third-party


# Local application (your project modules)
from required_classes.course import Course
from required_classes.student import Student


# ==== Classes ==== #

class TestStudent(unittest.TestCase):

    def setUp(self):
        """
        Docstring for TestStudent.setUp()
            - Description: Runs before every tests, so every tests has access to
            - Author: Lorenzo .S
        """

        # Test Courses
        self.course1 = Course("CSE2050", 3, 1)
        self.course2 = Course("MATH1010", 2, 1)

        # Test Students
        self.student1 = Student("STU00001", "Student_1")
        self.student2 = Student("STU00002", "Student_2", {self.course1: "A"})

    # ---- Test Student.__init__() ---- #

    def test_init(self):
        """
        Docstring for TestStudent.test_init()
            - Description: Tests that the constructor correctly initializes.
            - Author: Lorenzo .S
        """
        # Student1
        self.assertEqual(self.student1.student_id, "STU00001")
        self.assertEqual(self.student1.name, "Student_1")
        self.assertEqual(self.student1.courses, {})

        # Student2
        self.assertEqual(self.student2.student_id, "STU00002")
        self.assertEqual(self.student2.name, "Student_2")
        self.assertEqual(self.student2.courses, {self.course1: "A"})
        self.assertEqual(self.student2.courses[self.course1], "A")

    # ---- Test Student.enroll() ---- #

    def test_enroll(self):
        """
        Docstring for TestStudent.test_enroll()
            - Description: Enrolls the student with the given course
            - Author: Lorenzo .S
        """
        # Student1
        self.assertEqual(self.student1.courses, {})
        self.student1.enroll(self.course1, "A")
        self.assertEqual(self.student1.courses, {self.course1: "A"})

        # Student2
        self.assertEqual(self.student2.courses, {self.course1: "A"})
        self.student2.enroll(self.course2, "B")
        self.assertEqual(self.student2.courses, {self.course1: "A", self.course2: "B"})

        return

    def test_enroll_already_enrolled(self):
        """
        Docstring for TestStudent.test_enroll_already_enrolled()
            - Description: Tests that a ValueError is raised if the student is already enrolled in the course.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.courses, {self.course1: "A"})
        self.assertRaises(ValueError, self.student2.enroll, self.course1, "B")

    def test_enroll_invalid_grade(self):
        """
        Docstring for TestStudent.test_enroll_invalid_grade()
            - Description: Tests that a ValueError is raised if the student is enrolled with an invalid grade value.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.courses, {self.course1: "A"})
        self.assertRaises(ValueError, self.student2.enroll, self.course2, "8")
        self.assertRaises(ValueError, self.student2.enroll, self.course2, 8)
        self.assertRaises(ValueError, self.student2.enroll, self.course2, True)

    # ---- Test Student.update_grade() ---- #

    def test_update_grade(self):
        """
        Docstring for TestStudent.test_update_grade()
            - Description: Tests that Student.update_grade() works as expected.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.courses, {self.course1: "A"})
        self.assertEqual(self.student2.courses[self.course1], "A")
        self.student2.update_grade(self.course1, "B")
        self.assertEqual(self.student2.courses, {self.course1: "B"})

    # ---- Test Student.calculate_gpa() ---- #

    def test_calculate_gpa(self):
        """
        Docstring for TestStudent.test_calculate_gpa()
            - Description: Tests that Student.calculate_gpa() works as expected.
            - Author: Lorenzo .S
        """
        self.assertEqual(self.student2.calculate_gpa(), 4.0)
        self.assertEqual(self.student1.calculate_gpa(), 0.0)

    # ---- Test Student.get_course_info() ---- #

    def test_get_course_info(self):
        """
        Docstring for TestStudent.get_course_info()
            - Description: Tests that Student.get_course_info() works as expected.
            - Author: Lorenzo .S
        """
        self.assertEqual(
            self.student2.get_course_info(),
            [{'course_code': 'CSE2050', 'grade': 'A', 'credits': 3}]
        )

        self.student2.enroll(self.course2, "B")

        self.assertEqual(
            self.student2.get_course_info(),
            [
                {'course_code': 'CSE2050', 'grade': 'A', 'credits': 3},
                {'course_code': 'MATH1010', 'grade': 'B', 'credits': 2}
            ]
        )

        # Student1
        self.assertEqual(self.student1.get_course_info(), [])
        return


if __name__ == "__main__":
    unittest.main()