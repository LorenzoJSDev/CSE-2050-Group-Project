#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_university.py
-------------

Description: Contains the test cases for the University class.

Author: Lorenzo .S
Contributor(s): Jerod Abraham
Date Created: 03-04-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest
import datetime

# Local application
from required_classes.university import University
from required_classes.course import Course
from required_classes.student import Student


class TestUniversity(unittest.TestCase):
    """
    Docstring for TestUniversity
        - Description: Contains unit tests for the University class.
        - Author: Lorenzo .S
        - Contributor(s): Jerod Abraham
    """

    def setUp(self):
        """
        Docstring for TestUniversity.setUp()
            - Description: Creates fresh test objects before each test.
            - Author: Lorenzo .S
        """
        self.university1 = University()

        self.student1 = Student("STU00001", "Student_1")
        self.student2 = Student("STU00002", "Student_2")
        self.student3 = Student("STU00003", "Student_3")

    # ===== Test add_course =====

    def test_add_course(self):
        """
        Docstring for TestUniversity.test_add_course()
            - Description: Tests that a course is added and stored successfully.
            - Author: Jerod Abraham
        """
        course1 = self.university1.add_course("CSE2050", 3, 2)

        self.assertEqual(course1.course_code, "CSE2050")
        self.assertEqual(course1.course_credits, 3)
        self.assertEqual(course1.capacity, 2)
        self.assertIn("CSE2050", self.university1.courses)

    def test_duplicate_course(self):
        """
        Docstring for TestUniversity.test_duplicate_course()
            - Description: Tests that duplicate course additions return the same object.
            - Author: Jerod Abraham
        """
        c1 = self.university1.add_course("CSE2050", 3, 2)
        c2 = self.university1.add_course("CSE2050", 3, 2)

        self.assertIs(c1, c2)
        self.assertEqual(len(self.university1.courses), 1)

    # ===== Test add_student =====

    def test_add_student(self):
        """
        Docstring for TestUniversity.test_add_student()
            - Description: Tests that a student is added and stored successfully.
            - Author: Jerod Abraham
        """
        student = self.university1.add_student("STU00001", "Student_1")

        self.assertEqual(student.student_id, "STU00001")
        self.assertEqual(student.name, "Student_1")
        self.assertIn("STU00001", self.university1.students)

    def test_duplicate_student(self):
        """
        Docstring for TestUniversity.test_duplicate_student()
            - Description: Tests that duplicate student IDs return the same object.
            - Author: Jerod Abraham
        """
        s1 = self.university1.add_student("STU00001", "Student_1")
        s2 = self.university1.add_student("STU00001", "Student_2")

        self.assertIs(s1, s2)
        self.assertEqual(len(self.university1.students), 1)

    def test_invalid_student_id_raises(self):
        """
        Docstring for TestUniversity.test_invalid_student_id_raises()
            - Description: Tests that invalid student IDs raise ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.university1.add_student("BAD001", "Student_1")

    def test_empty_student_name_raises(self):
        """
        Docstring for TestUniversity.test_empty_student_name_raises()
            - Description: Tests that empty student names raise ValueError.
            - Author: Lorenzo .S
        """
        with self.assertRaises(ValueError):
            self.university1.add_student("STU99999", "")

    # ===== Test get_student =====

    def test_get_student(self):
        """
        Docstring for TestUniversity.test_get_student()
            - Description: Tests that a student can be retrieved by student ID.
            - Author: Jerod Abraham
        """
        self.university1.add_student("STU00001", "Student_1")

        student = self.university1.get_student("STU00001")

        self.assertEqual(student.student_id, "STU00001")

    def test_get_imaginary_student(self):
        """
        Docstring for TestUniversity.test_get_imaginary_student()
            - Description: Tests that requesting a non-existent student returns None.
            - Author: Jerod Abraham
        """
        self.assertIsNone(self.university1.get_student("STU12028"))

    # ===== Test get_course =====

    def test_get_course(self):
        """
        Docstring for TestUniversity.test_get_course()
            - Description: Tests that a course can be retrieved by course code.
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3, 2)

        course = self.university1.get_course("CSE2050")

        self.assertEqual(course.course_code, "CSE2050")

    def test_get_imaginary_course(self):
        """
        Docstring for TestUniversity.test_get_imaginary_course()
            - Description: Tests that requesting a non-existent course returns None.
            - Author: Jerod Abraham
        """
        self.assertIsNone(self.university1.get_course("CSE2500"))

    # ===== Test enrollment counts =====

    def test_get_course_enrollment(self):
        """
        Docstring for TestUniversity.test_get_course_enrollment()
            - Description: Tests that a course with no enrolled students returns zero.
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3, 2)

        count = self.university1.get_course_enrollment("CSE2050")

        self.assertEqual(count, 0)

    def test_get_students_in_course_empty(self):
        """
        Docstring for TestUniversity.test_get_students_in_course_empty()
            - Description: Tests that a course with no students returns an empty list.
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3, 2)

        self.assertEqual(self.university1.get_students_in_course("CSE2050"), [])

    # ===== Test request_enroll =====

    def test_request_enroll(self):
        """
        Docstring for TestUniversity.test_request_enroll()
            - Description: Tests that a student can be enrolled through the University object.
            - Author: Lorenzo .S
        """
        self.university1.add_student("STU00001", "Student_1")
        self.university1.add_course("CSE2050", 3, 2)

        enroll_date = datetime.date(2026, 4, 8)

        self.university1.request_enroll("STU00001", "CSE2050", enroll_date)

        course = self.university1.get_course("CSE2050")

        self.assertEqual(len(course.enrolled), 1)
        self.assertEqual(course.enrolled[0].student.student_id, "STU00001")
        self.assertEqual(course.enrolled[0].enroll_date, enroll_date)

    def test_request_enroll_course_full_waitlist(self):
        """
        Docstring for TestUniversity.test_request_enroll_course_full_waitlist()
            - Description: Tests that students are added to the waitlist when the course is full.
            - Author: Lorenzo .S
        """
        self.university1.add_course("CSE2050", 3, 2)

        self.university1.add_student("STU00001", "Student_1")
        self.university1.add_student("STU00002", "Student_2")
        self.university1.add_student("STU00003", "Student_3")

        self.university1.request_enroll("STU00001", "CSE2050")
        self.university1.request_enroll("STU00002", "CSE2050")
        self.university1.request_enroll("STU00003", "CSE2050")

        course = self.university1.get_course("CSE2050")

        self.assertEqual(len(course.enrolled), 2)
        self.assertEqual(len(course.waitlist), 1)

    # ===== Test prerequisites =====

    def test_request_enroll_missing_prerequisites_raises(self):
        """
        Docstring for TestUniversity.test_request_enroll_missing_prerequisites_raises()
            - Description: Tests that students missing prerequisites cannot enroll.
            - Author: Lorenzo .S
        """
        self.university1.add_student("STU00001", "Student_1")

        prereq_course = self.university1.add_course("CSE1010", 3, 2)
        target_course = self.university1.add_course("CSE2050", 3, 2)

        target_course.add_prerequisite("CSE1010")

        with self.assertRaises(ValueError):
            self.university1.request_enroll("STU00001", "CSE2050")

    def test_request_enroll_with_prerequisites_succeeds(self):
        """
        Docstring for TestUniversity.test_request_enroll_with_prerequisites_succeeds()
            - Description: Tests that students meeting prerequisites can enroll.
            - Author: Lorenzo .S
        """
        student = self.university1.add_student("STU00001", "Student_1")

        prereq_course = self.university1.add_course("CSE1010", 3, 2)
        target_course = self.university1.add_course("CSE2050", 3, 2)

        student.courses[prereq_course] = "A"

        target_course.add_prerequisite("CSE1010")

        self.university1.request_enroll("STU00001", "CSE2050")

        self.assertEqual(len(target_course.enrolled), 1)

    # ===== Test drop_student =====

    def test_drop_student(self):
        """
        Docstring for TestUniversity.test_drop_student()
            - Description: Tests that a student can be dropped from a course.
            - Author: Lorenzo .S
        """
        self.university1.add_student("STU00001", "Student_1")
        self.university1.add_course("CSE2050", 3, 2)

        enroll_date = datetime.date(2026, 4, 8)

        self.university1.request_enroll("STU00001", "CSE2050", enroll_date)
        self.university1.drop_student("STU00001", "CSE2050")

        course = self.university1.get_course("CSE2050")

        self.assertEqual(len(course.enrolled), 0)

    def test_drop_student_promotes_waitlist(self):
        """
        Docstring for TestUniversity.test_drop_student_promotes_waitlist()
            - Description: Tests that dropping a student promotes the next waitlisted student.
            - Author: Lorenzo .S
        """
        self.university1.add_course("CSE2050", 3, 2)

        self.university1.add_student("STU00001", "Student_1")
        self.university1.add_student("STU00002", "Student_2")
        self.university1.add_student("STU00003", "Student_3")

        self.university1.request_enroll("STU00001", "CSE2050")
        self.university1.request_enroll("STU00002", "CSE2050")
        self.university1.request_enroll("STU00003", "CSE2050")

        self.university1.drop_student("STU00001", "CSE2050")

        course = self.university1.get_course("CSE2050")

        enrolled_ids = [record.student.student_id for record in course.enrolled]

        self.assertIn("STU00003", enrolled_ids)
        self.assertEqual(len(course.waitlist), 0)


if __name__ == "__main__":
    unittest.main()