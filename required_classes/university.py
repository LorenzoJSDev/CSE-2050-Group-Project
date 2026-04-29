#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
university.py
-------------

Description: Contains the University class for the milestone One project

Author: Jerod Abraham
Contributors: Lorenzo .S
Date Created: 03-03-2026
Status: Development (alpha)

"""

# ===== Imports =====

# Standard library


# Third-party


# Local application (your project modules)
from required_classes.course import Course
from required_classes.student import Student

# ===== Classes =====


class University:
    """
    Docstring for University class
        - Description: The university class for the milestone One project
        - Author: Jerod Abraham
        - Contributors: Lorenzo .S
    """

    def __init__(self):
        """
        Docstring for University class
            - Description: The constructor for university class instances / objects
            - Author: Jerod Abraham
        """
        self.students = {}
        self.courses = {}

    def add_course(self, course_code, course_credits, capacity=30):
        """
        Docstring for University.add_course() method
            - Description: Adds a course to the university if it does not already exist and returns the Course object.
            - Author: Jerod Abraham
        """
        if course_code not in self.courses:
            course = Course(course_code, course_credits, capacity)
            self.courses[course_code] = course
        return self.courses[course_code]

    def add_student(self, student_id, name):
        """
        Docstring for University.add_student()
            - Description: Adds a student object to the self.students dictionary if it does not already exist and returns the Student object.
            - Author: Lorenzo .S
        """
        if not isinstance(student_id, str):
            raise ValueError(f"Student_ID {student_id} must be a string")
        if len(student_id) != 8:
            raise ValueError(f"Student_ID {student_id} must be 8 characters long")
        if not student_id.startswith("STU"):
            raise ValueError(f"Student_ID {student_id} must start with STU")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string")

        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name.strip())

        return self.students[student_id]

    def get_student(self, student_id):
        """
        Docstring for University.get_student()
            - Description: Returns the student object from the self.students dictionary, or None if not found.
            - Author: Lorenzo .S
        """
        return self.students.get(student_id)

    def get_course(self, course_code):
        """
        Docstring for University.get_course()
            - Description: Returns the course object from the self.courses dictionary, or None if not found.
            - Author: Lorenzo .S
        """
        return self.courses.get(course_code)

    def get_course_enrollment(self, course_code):
        """
        Docstring for University.get_course_enrollment()
            - Description: Returns the current number of enrolled students in a course.
            - Author: Lorenzo .S
        """
        course = self.get_course(course_code)
        return course.get_student_count()

    def get_students_in_course(self, course_code):
        """
        Docstring for University.students_in_class()
            - Description: Returns the list of students in a specific course
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """
        course = self.get_course(course_code)
        return [record.student for record in course.enrolled]

    def request_enroll(self, student_id, course_code, enroll_date=None):
        """
        Docstring for University.request_enroll()
            - Description: Requests enrollment for a student in a course.
            - Author: Lorenzo .S
        """
        student = self.get_student(student_id)
        course = self.get_course(course_code)
        course.request_enroll(student, enroll_date)

    def drop_student(self, student_id, course_code, enroll_date_for_replacement=None):
        """
        Docstring for University.drop_student()
            - Description: Drops a student from a course.
            - Author: Lorenzo .S
        """
        course = self.get_course(course_code)
        course.drop(student_id, enroll_date_for_replacement)