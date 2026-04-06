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


# ===== Classes =====

class Course:
    """
    Docstring for Course class
        - Description: The course class for the milestone One project
        - Author: Jerod Abraham
        - Contributor(s): Lorenzo .S
    """
    
    def __init__(self, course_code: str, course_credits: int, students: list = None, capacity: int = None) -> None:
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

        self.course_code = course_code.strip()
        self.course_credits = course_credits
        self.students = [] if students is None else students
        self.capacity = None if capacity is None else capacity
        



    def add_student(self, student: object):
        """
        Docstring for Course.add_student()
            - Description: Adds a student to the course’s enrollment list and raises a ValueError if the student is already enrolled.
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """
        if student in self.students:
            raise ValueError(f"Student {student} already enrolled in course {self.course_code}")
        else:
            self.students.append(student)


    def get_student_count(self):
        """
        Docstring for Course.get_student_count()
            - Description: Returns the number of students currently enrolled in the course.
            - Author: Jerod Abraham
        """
        return len(self.students)

    def __str__(self) -> str:
        """
        Docstring for Course.__str__()
            - Description: Returns a readable string representation of the course including its code, credits, and enrolled student count.
            - Author: Lorenzo .S
        """
        return f"{self.course_code} ({self.course_credits} credits) - {self.get_student_count()} students"
