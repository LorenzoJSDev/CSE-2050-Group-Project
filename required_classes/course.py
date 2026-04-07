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


# Third-party


# Local application (your project modules)
from required_classes.data_structures.linked_queue import LinkedQueue
from required_classes.data_structures.enrollment_record import EnrollmentRecord

# ===== Classes =====

class Course:
    """
    Docstring for Course class
        - Description: The course class for the milestone Two project
        - Author: Jerod Abraham
        - Contributor(s): Lorenzo .S
    """
    
    def __init__(self, course_code: str, course_credits: int, capacity: int) -> None:
        """
        Docstring for __init__
            - Description: Initializes a Course object with a course code, number of credits, and an optional list of enrolled students after validating the input values.
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """

        #Exception Handling
        if not isinstance(course_code, str) or not course_code.strip():
            raise ValueError("course_code must be a non-empty string")

        if not isinstance(course_credits, int) or course_credits <= 0:
            raise ValueError("course_credits must be a positive integer")
        
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")

        self.course_code = course_code.strip()
        self.course_credits = course_credits
        self.capacity = capacity
        self.enrolled = []
        self.waitlist = LinkedQueue()

    def get_student_count(self) -> int:
        """
        Docstring for Course.get_student_count()
            - Description: Returns the number of students currently enrolled in the course.
            - Author: Jerod Abraham
        """
        return len(self.enrolled)
    
    def request_enroll(self, student, enroll_date):
        """
        Docstring for Course.request_enroll()
            - Description: Requests enrollment for a student.
            - Author: Jerod Abraham
        """
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
        else:
            self.waitlist.enqueue(student)

    def drop(self, student_id, enroll_date_for_replacement=None):
        """
        Docstring for Course.drop()
            - Description: Drops a student from the enrolled roster.
            - Author: Jerod Abraham
        """
        remove_index = -1

        for i, record in enumerate(self.enrolled):
            if record.student.student_id == student_id:
                remove_index = i
                break

        if remove_index == -1:
            raise ValueError(f"Student {student_id} is not enrolled in {self.course_code}")

        self.enrolled.pop(remove_index)

        if not self.waitlist.is_empty():
            next_student = self.waitlist.dequeue()
            replacement_record = EnrollmentRecord(next_student, enroll_date_for_replacement)
            self.enrolled.append(replacement_record)

    def __str__(self) -> str:
        """
        Docstring for Course.__str__()
            - Description: Returns a readable string representation of the course including its code, credits, and enrolled student count.
            - Author: Lorenzo .S
            - Contributor: Jerod Abraham
        """
        return (f"{self.course_code} ({self.course_credits} credits) - "f"{len(self.enrolled)}/{self.capacity} enrolled")