#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_course.py
-------------

Description: Contains the tests cases for the Course class.

Author: Lorenzo .S
Contributors:
Date Created: 03-03-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application (your project modules)
from required_classes.course import Course
from required_classes.student import Student


# ==== Classes ==== #

class TestCourse(unittest.TestCase):

    def setUp(self):
        """
        Docstring for TestCourse.setUp()
            - Description: Runs before every tests, so every tests has access to created objects.
            - Author: Lorenzo .S
        """

        self.course1 = Course("CSE2050",3,[])
        self.student1 = Student("STU100", "Student1", {self.course1: "A"})
        self.student2 = Student("STU200", "Student2", {self.course1: "C"})
        self.course2 = Course("MATH1010", 3, [self.student1, self.student2])


    def test_init(self):
        """
        Docstring for TestCourse.test_init()
            - Description: Tests that the course object is initialized properly.
            - Author: Lorenzo .S
        """

        #Course1 Init
        self.assertEqual(self.course1.course_code, "CSE2050")
        self.assertEqual(self.course1.course_credits, 3)
        self.assertEqual(self.course1.students, [])

        #Course2 Init
        self.assertEqual(self.course2.course_code, "MATH1010")
        self.assertEqual(self.course2.course_credits, 3)
        self.assertEqual(self.course2.students, [self.student1,self.student2])

    def test_add_student(self):
        """
        Docstring for TestCourse.test_add_student()
            - Description: Tests that the add_student method adds a student to the course
            - Author: Lorenzo .S
        """
        #Course1
        self.assertEqual(self.course1.students, [])
        self.course1.add_student(self.student1)
        self.assertEqual(self.course1.students[0], self.student1)
        self.course1.add_student(self.student2)
        self.assertEqual(self.course1.students, [self.student1, self.student2])
        self.assertEqual(self.course1.students[1], self.student2)

    def test_add_student_existing_student(self):
        """
        Docstring for TestCourse.test_add_student_existing_student()
            - Description: Tests that the Course.add_student() raises an exception when trying to add an existing student.
            - Author: Lorenzo .S
        """

        self.assertRaises(ValueError, self.course2.add_student, self.student1)

    def test_get_student_count(self):
        """
        Docstring for TestCourse.get_student_count()
            - Description: Tests that the get_student_count method returns the correct number of students
            - Author: Lorenzo .S
        """
        #Course1
        self.assertEqual(self.course1.get_student_count(), 0)
        self.course1.add_student(self.student1)
        self.assertEqual(self.course1.get_student_count(), 1)

        #Course2
        self.assertEqual(self.course2.get_student_count(), 2)



if __name__ == "__main__":
    unittest.main()