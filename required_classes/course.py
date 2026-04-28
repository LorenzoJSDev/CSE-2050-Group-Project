#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
course.py
-------------

Description: Contains the course class for the milestone One project

Author: Jerod Abraham
Contributors: Lorenzo .S
Date Created: 03-03-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library
import datetime

# Third-party


# Local application (your project modules)
from required_classes.data_structures.linked_queue import LinkedQueue
from required_classes.data_structures.enrollment_record import EnrollmentRecord
from required_classes.data_structures.hash_map import HashMap
<<<<<<< HEAD
=======

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34

# ===== Classes =====

class Course:
    """
    Docstring for Course class
        - Description: The course class for the milestone Two project
        - Author: Jerod Abraham
        - Contributor(s): Lorenzo .S
    """

<<<<<<< HEAD
    def __init__( self, course_code: str, course_credits: int, capacity: int = 30, students: list = None,
    prerequisite: HashMap = None,enrolled: list = None, waitlist: list = None) -> None:
=======
    def __init__(self, course_code: str, course_credits: int, capacity: int = 30, students: list = None,
                 prerequisite: HashMap = None, enrolled: list = None, waitlist: list = None) -> None:
>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
        """
        Docstring for __init__
            - Description: Initializes a Course object with a course code, number of credits, and an optional list of enrolled students after validating the input values.
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """

        # Exception Handling
        if not isinstance(course_code, str) or not course_code.strip():
            raise ValueError("course_code must be a non-empty string")

        if not isinstance(course_credits, int) or course_credits <= 0:
            raise ValueError("course_credits must be a positive integer")

        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")

        self.course_code = course_code.strip()
        self.course_credits = course_credits
        self.capacity = capacity
        self.students = [] if students is None else students
        self.prerequisite = prerequisite if prerequisite is not None else HashMap()
        self.enrolled = [] if enrolled is None else enrolled
        self.waitlist = LinkedQueue() if waitlist is None else waitlist
        self.enrolled_sorted_by = None

    def get_student_count(self) -> int:
        """
        Docstring for Course.get_student_count()
            - Description: Returns the number of students currently enrolled in the course.
            - Author: Jerod Abraham
        """
        return len(self.enrolled)

    def add_prerequisite(self, prereq_course_code: str, value=True) -> None:
        """
        Docstring for Course.add_prerequisite()
            - Description: Adds a prerequisite course code to the prerequisite HashMap.
            - Author: Jerod Abraham
        """
        if not isinstance(prereq_course_code, str) or not prereq_course_code.strip():
            raise ValueError("prereq_course_code must be a non-empty string")

        self.prerequisite.put(prereq_course_code.strip(), value)

    def has_completed_prerequisites(self, student) -> bool:
        """
        Docstring for Course.has completed_prerequisities()
            - Description: Checks whether the student has completed all prerequisites with a passing grade.
            - Author: Jerod Abraham
        """
        passing_grades = {"A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D"}

        completed_course_codes = set()

        for course, grade in student.courses.items():
            if grade in passing_grades:
                completed_course_codes.add(course.course_code)

        for prereq_code in self.prerequisite.keys():
            if prereq_code not in completed_course_codes:
                return False

        return True

    def _get_sort_key(self, record, by):
        """
        Docstring for Course._get_sort_key()
            - Description: Returns the sort key for an EnrollmentRecord based on the requested field.
            - Author: Lorenzo .S
        """
        if by == "name":
            return record.student.name
        if by == "id":
            return record.student.student_id
        if by == "date":
            return record.enroll_date
        raise ValueError("Sort key must be 'name', 'id', or 'date'")
<<<<<<< HEAD
    
=======

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
    def _merge_sort(self, records, by):
        """
        Docstring for Course._merge_sort()
            - Description: Sorts the enrolled roster using merge sort.
            - Author: Jerod Abraham
        """
        if len(records) <= 1:
            return records

        mid = len(records) // 2
        left = self._merge_sort(records[:mid], by)
        right = self._merge_sort(records[mid:], by)

        return self._merge(left, right, by)

    def _merge(self, left, right, by):
        """
        Docstring for Course._merge()
            - Description: Part of the merge sort.
            - Author: Jerod Abraham
        """
        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if self._get_sort_key(left[i], by) <= self._get_sort_key(right[j], by):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def _quick_sort(self, records, by):
        """
        Docstring for Course._quick_sort()
            - Description: Sorts the enrolled roster using quick sort.
            - Author: Jerod Abraham
        """
        if len(records) <= 1:
            return records

        pivot = records[len(records) // 2]
        pivot_key = self._get_sort_key(pivot, by)

        less = [r for r in records if self._get_sort_key(r, by) < pivot_key]
        equal = [r for r in records if self._get_sort_key(r, by) == pivot_key]
        greater = [r for r in records if self._get_sort_key(r, by) > pivot_key]

        return self._quick_sort(less, by) + equal + self._quick_sort(greater, by)

    """
    def insertion_sort_enrolled(self, by):
<<<<<<< HEAD
        
        Docstring for Course.insertion_sort_enrolled()
            - Description: Sorts the enrolled roster using insertion sort.
            - Author: Lorenzo .S
        
=======

        Docstring for Course.insertion_sort_enrolled()
            - Description: Sorts the enrolled roster using insertion sort.
            - Author: Lorenzo .S

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
        for i in range(1, len(self.enrolled)):
            current_record = self.enrolled[i]
            j = i - 1

            while j >= 0 and self._get_sort_key(self.enrolled[j], by) > self._get_sort_key(current_record, by):
                self.enrolled[j + 1] = self.enrolled[j]
                j -= 1

            self.enrolled[j + 1] = current_record

    def selection_sort_enrolled(self, by):
<<<<<<< HEAD
        
        Docstring for Course.selection_sort_enrolled()
            - Description: Sorts the enrolled roster using selection sort.
            - Author: Lorenzo .S
        
=======

        Docstring for Course.selection_sort_enrolled()
            - Description: Sorts the enrolled roster using selection sort.
            - Author: Lorenzo .S

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
        n = len(self.enrolled)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if self._get_sort_key(self.enrolled[j], by) < self._get_sort_key(self.enrolled[min_index], by):
                    min_index = j

            self.enrolled[i], self.enrolled[min_index] = self.enrolled[min_index], self.enrolled[i]

    def sort_enrolled(self, by, algorithm):
<<<<<<< HEAD
        
        Docstring for Course.sort_enrolled()
            - Description: Sorts the enrolled roster by the requested key using the requested algorithm.
            - Author: Lorenzo .S
        
=======

        Docstring for Course.sort_enrolled()
            - Description: Sorts the enrolled roster by the requested key using the requested algorithm.
            - Author: Lorenzo .S

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
        if algorithm == "insertion":
            self.insertion_sort_enrolled(by)
        elif algorithm == "selection":
            self.selection_sort_enrolled(by)
        else:
            raise ValueError("Algorithm must be 'insertion' or 'selection'")

        self.enrolled_sorted_by = by
    """
<<<<<<< HEAD
=======

>>>>>>> 810a99955526e9f9e5fd8dcca493647ec882aa34
    def sort_enrolled(self, by, algorithm):
        """
        Docstring for Course.sort_enrolled()
            - Description: Sorts the enrolled roster by the requested key using the new algorithms.
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """
        if algorithm == "merge":
            self.enrolled = self._merge_sort(self.enrolled, by)
        elif algorithm == "quick":
            self.enrolled = self._quick_sort(self.enrolled, by)
        else:
            raise ValueError("Algorithm must be 'merge' or 'quick'")

        self.enrolled_sorted_by = by

    def recursive_binary_search(self, records, target_id, low, high):
        """
        Docstring for Course.recursive_binary_search()
            - Description: Recursively performs binary search on an enrolled roster sorted by student id.
            - Author: Lorenzo .S
        """
        if low > high:
            return -1

        mid = (low + high) // 2
        mid_student_id = records[mid].student.student_id

        if mid_student_id == target_id:
            return mid
        if target_id < mid_student_id:
            return self.recursive_binary_search(records, target_id, low, mid - 1)
        return self.recursive_binary_search(records, target_id, mid + 1, high)

    def request_enroll(self, student, enroll_date=None):
        """
        Docstring for Course.request_enroll()
            - Description: Requests enrollment for a student.
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """
        if enroll_date is None:
            enroll_date = datetime.date.today()

        if not self.has_completed_prerequisites(student):
            raise ValueError(
                f"Student {student.student_id} has not fulfilled prerequisite requirements for {self.course_code}"
            )

        for record in self.enrolled:
            if record.student.student_id == student.student_id:
                raise ValueError(f"Student {student.student_id} is already enrolled in {self.course_code}")

        current = self.waitlist.front
        while current is not None:
            if current.data.student_id == student.student_id:
                raise ValueError(f"Student {student.student_id} is already on the waitlist for {self.course_code}")
            current = current.next

        if len(self.enrolled) < self.capacity:
            record = EnrollmentRecord(student, enroll_date)
            self.enrolled.append(record)
            self.enrolled_sorted_by = None
        else:
            self.waitlist.enqueue(student)

        self.enrolled_sorted_by = None

    def drop(self, student_id, enroll_date_for_replacement=None):
        """
        Docstring for Course.drop()
            - Description: Drops a student from the roster of enrolled students.
            - Author: Jerod Abraham
        """
        if self.enrolled_sorted_by != "id":
            self.sort_enrolled("id", "merge")

        remove_index = self.recursive_binary_search(self.enrolled, student_id, 0, len(self.enrolled) - 1)

        if remove_index == -1:
            raise ValueError(f"Student {student_id} is not enrolled in {self.course_code}")

        self.enrolled.pop(remove_index)

        if not self.waitlist.is_empty():
            next_student = self.waitlist.dequeue()

            if enroll_date_for_replacement is None:
                enroll_date_for_replacement = datetime.date.today()

            replacement_record = EnrollmentRecord(next_student, enroll_date_for_replacement)
            self.enrolled.append(replacement_record)
            self.enrolled_sorted_by = None

        self.enrolled_sorted_by = None

    def __str__(self) -> str:
        """
        Docstring for Course.__str__()
            - Description: Returns a readable string representation of the course including its code, credits, and enrolled student count.
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """
        return f"{self.course_code} ({self.course_credits} credits) - {len(self.enrolled)}/{self.capacity} enrolled"