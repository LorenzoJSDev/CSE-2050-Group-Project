#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_course.py
-------------

Description: Contains the tests cases for the Course class.

Author: Lorenzo .S
Contributor: Jerod Abraham
Date Created: 03-03-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application (your project modules)
from required_classes.student import Student
from required_classes.course import Course
from required_classes.data_structures.enrollment_record import EnrollmentRecord


# ==== Classes ==== #

class TestCourse(unittest.TestCase):

    def setUp(self):
        """
        Docstring for TestCourse.setUp()
            - Description: Runs before every tests, so every tests has access to created objects.
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """

        self.course1 = Course("CSE2050", 3, 2)
        self.student1 = Student("STU10001", "Student1")
        self.student2 = Student("STU10002", "Student2")
        self.student3 = Student("STU10003", "Student3")
        self.student1.courses = {}
        self.student2.courses = {}
        self.student3.courses = {}

    def test_init(self):
        """
        Docstring for TestCourse.test_init()
            - Description: Tests that the course object is initialized properly.
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """

        self.assertEqual(self.course1.course_code, "CSE2050")
        self.assertEqual(self.course1.course_credits, 3)
        self.assertEqual(self.course1.capacity, 2)
        self.assertEqual(self.course1.enrolled, [])
        self.assertTrue(self.course1.waitlist.is_empty())

    def test_add_prerequisite(self):
        """
        Docstring for TestCourse.test_add_prerequisite()
            - Description: Tests that a prerequisite course code is correctly added to the course’s prerequisite HashMap.
            - Author: Jerod Abraham
        """
        self.course1.add_prerequisite("CSE1010")
        self.assertIn("CSE1010", self.course1.prerequisite.keys())

    def test_has_completed_prerequisites_true(self):
        """
        Docstring for TestCourse.test_has_completed_prerequisites_true()
            - Description: Tests that a student who has completed all prerequisite courses with passing grades is correctly identified.
            - Author: Jerod Abraham
        """
        prereq_course = Course("CSE1010", 3, 2)
        self.student1.courses[prereq_course] = "B"

        self.course1.add_prerequisite("CSE1010")

        self.assertTrue(self.course1.has_completed_prerequisites(self.student1))

    def test_has_completed_prerequisites_false_missing_course(self):
        """
        Docstring for TestCourse.test_has_completed_prerequisites_false_missing_course()
            - Description: Tests that a student who has not completed required prerequisite courses is correctly identified.
            - Author: Jerod Abraham
        """
        self.course1.add_prerequisite("CSE1010")
        self.assertFalse(self.course1.has_completed_prerequisites(self.student1))

    def test_has_completed_prerequisites_false_failing_grade(self):
        """
        Docstring for TestCourse.test_has_completed_prerequisites_false_failing_grade()
            - Description: Tests that a student who has completed prerequisite courses with a failing grade does not satisfy requirements.
            - Author: Jerod Abraham
        """
        prereq_course = Course("CSE1010", 3, 2)
        self.student1.courses[prereq_course] = "F"

        self.course1.add_prerequisite("CSE1010")

        self.assertFalse(self.course1.has_completed_prerequisites(self.student1))

    def test_request_enroll_with_space(self):
        """
        Docstring for TestCourse.test_request_enroll_with_space()
            - Description: Tests that a student is enrolled directly when space is available.
            - Author: Jerod Abraham
        """
        self.course1.request_enroll(self.student1, "2026-03-25")

        self.assertEqual(len(self.course1.enrolled), 1)
        self.assertIsInstance(self.course1.enrolled[0], EnrollmentRecord)
        self.assertEqual(self.course1.enrolled[0].student, self.student1)
        self.assertEqual(self.course1.enrolled[0].enroll_date, "2026-03-25")

    def test_request_enroll_when_full_adds_to_waitlist(self):
        """
        Docstring for TestCourse.test_request_enroll_when_full_adds_to_waitlist()
            - Description: Tests that extra students are added to the waitlist when the course is full.
            - Author: Jerod Abraham
        """
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-25")
        self.course1.request_enroll(self.student3, "2026-03-25")

        self.assertEqual(len(self.course1.enrolled), 2)
        self.assertEqual(len(self.course1.waitlist), 1)

    def test_request_enroll_without_prereqs_raises(self):
        """
        Docstring for TestCourse.test_request_enroll_without_prereqs_raises()
            - Description: Tests that a student who does not meet prerequisite requirements cannot enroll in the course.
            - Author: Jerod Abraham
        """
        self.course1.add_prerequisite("CSE1010")

        with self.assertRaises(ValueError):
            self.course1.request_enroll(self.student1, "2026-03-25")

    def test_request_enroll_with_prereqs_succeeds(self):
        """
        Docstring for TestCourse.test_request_enroll_with_prereqs_succeeds()
            - Description: Tests that a student who meets prerequisite requirements is successfully enrolled in the course.
            - Author: Jerod Abraham
        """
        prereq_course = Course("CSE1010", 3, 2)
        self.student1.courses[prereq_course] = "A"
        self.course1.add_prerequisite("CSE1010")

        self.course1.request_enroll(self.student1, "2026-03-25")

        self.assertEqual(len(self.course1.enrolled), 1)
        self.assertEqual(self.course1.enrolled[0].student, self.student1)

    def test_get_student_count(self):
        """
        Docstring for TestCourse.test_get_student_count()
            - Description: Tests that the get_student_count method returns the correct number of enrolled students
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """
        self.assertEqual(self.course1.get_student_count(), 0)

        self.course1.request_enroll(self.student1, "2026-03-25")
        self.assertEqual(self.course1.get_student_count(), 1)

        self.course1.request_enroll(self.student2, "2026-03-25")
        self.assertEqual(self.course1.get_student_count(), 2)

    def test_drop_removes_student(self):
        """
        Docstring for TestCourse.test_drop_removes_student()
            - Description: Tests that dropping a student removes them from the enrolled roster.
            - Author: Jerod Abraham
        """
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-25")

        self.course1.drop("STU10001", "2026-03-26")

        self.assertEqual(len(self.course1.enrolled), 1)
        self.assertEqual(self.course1.enrolled[0].student.student_id, "STU10002")

    def test_drop_promotes_waitlisted_student(self):
        """
        Docstring for TestCourse.test_drop_promotes_waitlisted_student()
            - Description: Tests that dropping a student promotes the next waitlisted student.
            - Author: Jerod Abraham
        """
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-25")
        self.course1.request_enroll(self.student3, "2026-03-25")  # goes to waitlist

        self.course1.drop("STU10001", "2026-03-26")

        self.assertEqual(len(self.course1.enrolled), 2)
        self.assertEqual(len(self.course1.waitlist), 0)

        enrolled_ids = [record.student.student_id for record in self.course1.enrolled]
        self.assertIn("STU10002", enrolled_ids)
        self.assertIn("STU10003", enrolled_ids)

    def test_request_enroll_duplicate_student_raises(self):
        """
        Docstring for TestCourse.test_request_enroll_duplicate_student_raises()
            - Description: Tests that enrolling the same student twice raises an error.
            - Author: Jerod Abraham
        """
        self.course1.request_enroll(self.student1, "2026-03-25")

        with self.assertRaises(ValueError):
            self.course1.request_enroll(self.student1, "2026-03-26")

    def test_sort_enrolled_by_id_merge(self):
        """
        Docstring for TestCourse.test_sort_enrolled_by_id_merge()
            - Description: Tests that the enrolled roster is correctly sorted by student ID using merge sort.
            - Author: Jerod Abraham
        """
        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("id", "merge")

        sorted_ids = [record.student.student_id for record in self.course1.enrolled]
        self.assertEqual(sorted_ids, ["STU10001", "STU10002", "STU10003"])
        self.assertEqual(self.course1.enrolled_sorted_by, "id")

    def test_sort_enrolled_by_name_quick(self):
        """
        Docstring for TestCourse.test_sort_enrolled_by_name_quick()
            - Description: Tests that the enrolled roster is correctly sorted by student name using quick sort.
            - Author: Jerod Abraham
        """
        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("name", "quick")

        sorted_names = [record.student.name for record in self.course1.enrolled]
        self.assertEqual(sorted_names, ["Student1", "Student2", "Student3"])
        self.assertEqual(self.course1.enrolled_sorted_by, "name")

    def test_sort_enrolled_by_date_merge(self):
        """
        Docstring for TestCourse.test_sort_enrolled_by_date_merge()
            - Description: Tests that the enrolled roster is correctly sorted by enrollment date using merge sort.
            - Author: Jerod Abraham
        """
        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("date", "merge")

        sorted_dates = [record.enroll_date for record in self.course1.enrolled]
        self.assertEqual(sorted_dates, ["2026-03-25", "2026-03-26", "2026-03-27"])
        self.assertEqual(self.course1.enrolled_sorted_by, "date")

    def test_sort_enrolled_invalid_algorithm_raises(self):
        """
        Docstring for TestCourse.test_sort_enrolled_invalid_algorithm_raises()
            - Description: Tests that providing an invalid sorting algorithm raises a ValueError.
            - Author: Jerod Abraham
        """
        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student1, "2026-03-25")

        with self.assertRaises(ValueError):
            self.course1.sort_enrolled("id", "insertion")

    """
    def test_sort_enrolled_by_id_insertion(self):
<<<<<<< HEAD
        
        Docstring for TestCourse.test_sort_enrolled_by_id_insertion()
            - Description: Tests that the enrolled roster is sorted by student ID using insertion sort.
            - Author: Jerod Abraham
        
=======

        Docstring for TestCourse.test_sort_enrolled_by_id_insertion()
            - Description: Tests that the enrolled roster is sorted by student ID using insertion sort.
            - Author: Jerod Abraham

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("id", "insertion")

        sorted_ids = [record.student.student_id for record in self.course1.enrolled]
        self.assertEqual(sorted_ids, ["STU10001", "STU10002", "STU10003"])
        self.assertEqual(self.course1.enrolled_sorted_by, "id")


    def test_sort_enrolled_by_name_selection(self):
<<<<<<< HEAD
        
        Docstring for TestCourse.test_sort_enrolled_by_name_selection()
            - Description: Tests that the enrolled roster is sorted by student name using selection sort.
            - Author: Jerod Abraham
        
=======

        Docstring for TestCourse.test_sort_enrolled_by_name_selection()
            - Description: Tests that the enrolled roster is sorted by student name using selection sort.
            - Author: Jerod Abraham

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("name", "selection")

        sorted_names = [record.student.name for record in self.course1.enrolled]
        self.assertEqual(sorted_names, ["Student1", "Student2", "Student3"])
        self.assertEqual(self.course1.enrolled_sorted_by, "name")


    def test_sort_enrolled_by_date_insertion(self):
<<<<<<< HEAD
        
        Docstring for TestCourse.test_sort_enrolled_by_date_insertion()
            - Description: Tests that the enrolled roster is sorted by enrollment date using insertion sort.
            - Author: Jerod Abraham
        
=======

        Docstring for TestCourse.test_sort_enrolled_by_date_insertion()
            - Description: Tests that the enrolled roster is sorted by enrollment date using insertion sort.
            - Author: Jerod Abraham

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.sort_enrolled("date", "insertion")

        sorted_dates = [record.enroll_date for record in self.course1.enrolled]
        self.assertEqual(sorted_dates, ["2026-03-25", "2026-03-26", "2026-03-27"])
        self.assertEqual(self.course1.enrolled_sorted_by, "date")
    """

    def test_recursive_binary_search_finds_students(self):
        """
        Docstring for TestCourse.test_recursive_binary_search_finds_students()
            - Description: Tests that recursive binary search finds the first, middle, and last student in a sorted enrolled roster.
            - Author: Jerod Abraham
        """

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")
        self.course1.request_enroll(self.student3, "2026-03-27")

        self.course1.sort_enrolled("id", "merge")

<<<<<<< HEAD
        index1 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10001", 0, len(self.course1.enrolled) - 1)
        index2 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10002", 0, len(self.course1.enrolled) - 1)
        index3 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10003", 0, len(self.course1.enrolled) - 1)
=======
        index1 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10001", 0,
                                                      len(self.course1.enrolled) - 1)
        index2 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10002", 0,
                                                      len(self.course1.enrolled) - 1)
        index3 = self.course1.recursive_binary_search(self.course1.enrolled, "STU10003", 0,
                                                      len(self.course1.enrolled) - 1)
>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

        self.assertEqual(self.course1.enrolled[index1].student.student_id, "STU10001")
        self.assertEqual(self.course1.enrolled[index2].student.student_id, "STU10002")
        self.assertEqual(self.course1.enrolled[index3].student.student_id, "STU10003")

    def test_recursive_binary_search_not_found(self):
        """
        Docstring for TestCourse.test_recursive_binary_search_not_found()
            - Description: Tests that recursive binary search returns -1 when the student ID is not found.
            - Author: Jerod Abraham
        """

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")
        self.course1.request_enroll(self.student3, "2026-03-27")

        self.course1.sort_enrolled("id", "merge")

<<<<<<< HEAD
        result = self.course1.recursive_binary_search(self.course1.enrolled, "STU99999", 0, len(self.course1.enrolled) - 1)
=======
        result = self.course1.recursive_binary_search(self.course1.enrolled, "STU99999", 0,
                                                      len(self.course1.enrolled) - 1)
>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

        self.assertEqual(result, -1)

    def test_drop_uses_binary_search(self):
        """
        Docstring for TestCourse.test_drop_uses_binary_search()
            - Description: Tests that dropping a student removes the correct record after sorting by student ID.
            - Author: Jerod Abraham
        """

        self.course1 = Course("CSE2050", 3, 3)
        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")

        self.course1.drop("STU10002", "2026-03-28")

        enrolled_ids = [record.student.student_id for record in self.course1.enrolled]

        self.assertNotIn("STU10002", enrolled_ids)
        self.assertEqual(len(self.course1.enrolled), 2)

    def test_drop_binary_search_promotes_waitlisted_student(self):
        """
        Docstring for TestCourse.test_drop_binary_search_promotes_waitlisted_student()
            - Description: Tests that dropping a student with binary search promotes the next waitlisted student.
            - Author: Jerod Abraham
        """

        self.course1 = Course("CSE2050", 3, 3)
        student4 = Student("STU10004", "Student4")

        self.course1.request_enroll(self.student3, "2026-03-27")
        self.course1.request_enroll(self.student1, "2026-03-25")
        self.course1.request_enroll(self.student2, "2026-03-26")
        self.course1.request_enroll(student4, "2026-03-28")

        self.assertEqual(len(self.course1.waitlist), 1)

        self.course1.drop("STU10002", "2026-03-29")

        enrolled_ids = [record.student.student_id for record in self.course1.enrolled]

        self.assertNotIn("STU10002", enrolled_ids)
        self.assertIn("STU10004", enrolled_ids)
        self.assertEqual(len(self.course1.waitlist), 0)

<<<<<<< HEAD
=======

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
if __name__ == "__main__":
    unittest.main()