#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_milestone2.py
------------------

Description: Contains the unit tests for Milestone 2 functionality.

Author: Jerod Abraham
Contributors: Lorenzo .S
Date Created: 04-07-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application (your project modules)
from required_classes.student import Student
from required_classes.course import Course
from required_classes.data_structures.linked_queue import LinkedQueue
from required_classes.data_structures.enrollment_record import EnrollmentRecord


# ===== Classes =====

class TestLinkedQueue(unittest.TestCase):
    """
    Docstring for TestLinkedQueue class
        - Description: Contains the unit tests for the LinkedQueue class.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestLinkedQueue.setUp()
            - Description: Runs before every test so each test has a fresh LinkedQueue object.
            - Author: Lorenzo .S
        """
        self.queue = LinkedQueue()

    def test_enqueue_dequeue_fifo_order(self):
        """
        Docstring for TestLinkedQueue.test_enqueue_dequeue_fifo_order()
            - Description: Tests that the queue follows FIFO order.
            - Author: Jerod Abraham
        """
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.queue.enqueue("C")

        self.assertEqual(self.queue.dequeue(), "A")
        self.assertEqual(self.queue.dequeue(), "B")
        self.assertEqual(self.queue.dequeue(), "C")

    def test_dequeue_empty_raises(self):
        """
        Docstring for TestLinkedQueue.test_dequeue_empty_raises()
            - Description: Tests that dequeue raises a ValueError when the queue is empty.
            - Author: Jerod Abraham
        """
        with self.assertRaises(ValueError):
            self.queue.dequeue()

    def test_size_tracking(self):
        """
        Docstring for TestLinkedQueue.test_size_tracking()
            - Description: Tests that the size of the queue updates correctly after enqueue and dequeue operations.
            - Author: Jerod Abraham
        """
        self.assertEqual(len(self.queue), 0)

        self.queue.enqueue("A")
        self.assertEqual(len(self.queue), 1)

        self.queue.enqueue("B")
        self.assertEqual(len(self.queue), 2)

        self.queue.dequeue()
        self.assertEqual(len(self.queue), 1)


class TestCourseMilestone2(unittest.TestCase):
    """
    Docstring for TestCourseMilestone2 class
        - Description: Contains the unit tests for Milestone 2 Course functionality.
        - Author: Lorenzo .S
    """

    def setUp(self):
        """
        Docstring for TestCourseMilestone2.setUp()
            - Description: Runs before every test so each test has fresh Course and Student objects.
            - Author: Lorenzo .S
        """
        self.course2 = Course("CSE2050", 3, 2)
        self.course3 = Course("CSE2050", 3, 3)

        self.student1 = Student("STU10001", "Student1")
        self.student2 = Student("STU10002", "Student2")
        self.student3 = Student("STU10003", "Student3")
        self.student4 = Student("STU10004", "Student4")

    def test_enroll_until_capacity(self):
        """
        Docstring for TestCourseMilestone2.test_enroll_until_capacity()
            - Description: Tests that students are enrolled directly until the course reaches capacity.
            - Author: Jerod Abraham
        """
        self.course2.request_enroll(self.student1, "2026-03-25")
        self.course2.request_enroll(self.student2, "2026-03-26")

        self.assertEqual(len(self.course2.enrolled), 2)
        self.assertEqual(self.course2.get_student_count(), 2)
        self.assertTrue(self.course2.waitlist.is_empty())
        self.assertIsInstance(self.course2.enrolled[0], EnrollmentRecord)

    def test_extra_students_go_to_waitlist(self):
        """
        Docstring for TestCourseMilestone2.test_extra_students_go_to_waitlist()
            - Description: Tests that students are placed on the waitlist after the course reaches capacity.
            - Author: Jerod Abraham
        """
        self.course2.request_enroll(self.student1, "2026-03-25")
        self.course2.request_enroll(self.student2, "2026-03-26")
        self.course2.request_enroll(self.student3, "2026-03-27")

        self.assertEqual(len(self.course2.enrolled), 2)
        self.assertEqual(len(self.course2.waitlist), 1)
        self.assertEqual(self.course2.waitlist.front.data, self.student3)

    def test_drop_triggers_waitlist_promotion(self):
        """
        Docstring for TestCourseMilestone2.test_drop_triggers_waitlist_promotion()
            - Description: Tests that dropping a student promotes the next waitlisted student into the enrolled roster.
            - Author: Jerod Abraham
        """
        self.course2.request_enroll(self.student1, "2026-03-25")
        self.course2.request_enroll(self.student2, "2026-03-26")
        self.course2.request_enroll(self.student3, "2026-03-27")

        self.course2.drop("STU10001", "2026-03-28")

        enrolled_ids = [record.student.student_id for record in self.course2.enrolled]

        self.assertEqual(len(self.course2.enrolled), 2)
        self.assertEqual(len(self.course2.waitlist), 0)
        self.assertIn("STU10002", enrolled_ids)
        self.assertIn("STU10003", enrolled_ids)
        self.assertNotIn("STU10001", enrolled_ids)

    def test_sort_by_id_insertion(self):
        """
        Docstring for TestCourseMilestone2.test_sort_by_id_insertion()
            - Description: Tests that the enrolled roster is correctly sorted by student ID using insertion sort.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student3, "2026-03-27")
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")

        self.course3.sort_enrolled("id", "insertion")

        sorted_ids = [record.student.student_id for record in self.course3.enrolled]
        self.assertEqual(sorted_ids, ["STU10001", "STU10002", "STU10003"])
        self.assertEqual(self.course3.enrolled_sorted_by, "id")

    def test_sort_by_name_selection(self):
        """
        Docstring for TestCourseMilestone2.test_sort_by_name_selection()
            - Description: Tests that the enrolled roster is correctly sorted by student name using selection sort.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student3, "2026-03-27")
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")

        self.course3.sort_enrolled("name", "selection")

        sorted_names = [record.student.name for record in self.course3.enrolled]
        self.assertEqual(sorted_names, ["Student1", "Student2", "Student3"])
        self.assertEqual(self.course3.enrolled_sorted_by, "name")

    def test_sort_by_date_insertion(self):
        """
        Docstring for TestCourseMilestone2.test_sort_by_date_insertion()
            - Description: Tests that the enrolled roster is correctly sorted by enrollment date using insertion sort.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student3, "2026-03-27")
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")

        self.course3.sort_enrolled("date", "insertion")

        sorted_dates = [record.enroll_date for record in self.course3.enrolled]
        self.assertEqual(sorted_dates, ["2026-03-25", "2026-03-26", "2026-03-27"])
        self.assertEqual(self.course3.enrolled_sorted_by, "date")

    def test_recursive_binary_search_finds_first_middle_last(self):
        """
        Docstring for TestCourseMilestone2.test_recursive_binary_search_finds_first_middle_last()
            - Description: Tests that recursive binary search finds the first, middle, and last student in a roster sorted by student ID.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")
        self.course3.request_enroll(self.student3, "2026-03-27")

        self.course3.sort_enrolled("id", "insertion")

        first_index = self.course3.recursive_binary_search(self.course3.enrolled, "STU10001", 0, len(self.course3.enrolled) - 1)
        middle_index = self.course3.recursive_binary_search(self.course3.enrolled, "STU10002", 0, len(self.course3.enrolled) - 1)
        last_index = self.course3.recursive_binary_search(self.course3.enrolled, "STU10003", 0, len(self.course3.enrolled) - 1)

        self.assertEqual(self.course3.enrolled[first_index].student.student_id, "STU10001")
        self.assertEqual(self.course3.enrolled[middle_index].student.student_id, "STU10002")
        self.assertEqual(self.course3.enrolled[last_index].student.student_id, "STU10003")

    def test_recursive_binary_search_not_found_returns_negative_one(self):
        """
        Docstring for TestCourseMilestone2.test_recursive_binary_search_not_found_returns_negative_one()
            - Description: Tests that recursive binary search returns -1 when the student ID is not found.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")
        self.course3.request_enroll(self.student3, "2026-03-27")

        self.course3.sort_enrolled("id", "insertion")

        result = self.course3.recursive_binary_search(self.course3.enrolled, "STU99999", 0, len(self.course3.enrolled) - 1)

        self.assertEqual(result, -1)

    def test_drop_auto_sorts_when_not_sorted_by_id(self):
        """
        Docstring for TestCourseMilestone2.test_drop_auto_sorts_when_not_sorted_by_id()
            - Description: Tests that drop works correctly even when the roster is not currently sorted by student ID.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student3, "2026-03-27")
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")

        self.course3.sort_enrolled("name", "selection")
        self.course3.drop("STU10002", "2026-03-28")

        enrolled_ids = [record.student.student_id for record in self.course3.enrolled]

        self.assertNotIn("STU10002", enrolled_ids)
        self.assertEqual(len(self.course3.enrolled), 2)

    def test_drop_with_waitlist_and_binary_search(self):
        """
        Docstring for TestCourseMilestone2.test_drop_with_waitlist_and_binary_search()
            - Description: Tests that dropping a student uses binary search and promotes the next waitlisted student.
            - Author: Jerod Abraham
        """
        self.course3.request_enroll(self.student3, "2026-03-27")
        self.course3.request_enroll(self.student1, "2026-03-25")
        self.course3.request_enroll(self.student2, "2026-03-26")
        self.course3.request_enroll(self.student4, "2026-03-28")

        self.assertEqual(len(self.course3.waitlist), 1)

        self.course3.drop("STU10002", "2026-03-29")

        enrolled_ids = [record.student.student_id for record in self.course3.enrolled]

        self.assertNotIn("STU10002", enrolled_ids)
        self.assertIn("STU10004", enrolled_ids)
        self.assertEqual(len(self.course3.waitlist), 0)


if __name__ == "__main__":
    unittest.main()