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
    
    def add_course(self, course_code, course_credits):
        """
        Docstring for University.add_course() method
            - Description: Adds a course to the university
            - Author: Jerod Abraham
        """
        if course_code not in self.courses:
            course = Course(course_code, course_credits)
            self.courses[course_code] = course
        return self.courses[course_code]
    
    def add_student(self, student_id, name):
        """
        Docstring for University.add_student()
            - Description: Adds a student object to the self.students dictionary
            - Author: Lorenzo .S
        """

        if student_id in self.students.keys():
            raise ValueError(f"Student_ID {student_id} already exists in University object")
        elif not isinstance(student_id, str):
            raise ValueError(f"Student_ID {student_id} must be a string")
        elif len(student_id) != 8:
            raise ValueError(f"Student_ID {student_id} must be 8 characters long")
        elif student_id[0:3] != "STU":
            raise ValueError(f"Student_ID {student_id} must start with STU")
        else:
            student = Student(student_id, name)
            self.students[student_id] = student

    def get_student(self, student_id):
        """
        Docstring for University.get_student()
            - Description: Returns the student object from the self.students dictionary.
            - Author: Lorenzo .S
        """
        if student_id in self.students.keys():
            return self.students[student_id]
        else:
            raise ValueError(f"Student_ID {student_id} does not exist in University object")

    def get_course(self, course_code):
        """
        Docstring for University.get_course()
            - Description: Returns the course object from the self.courses dictionary.
            - Author: Lorenzo .S
        """
        return self.courses.get(course_code)

    def get_course_enrollment(self, course_code):
        course = self.get_course(course_code)
        if course:
            return course.get_student_count()
        return 0

    def get_students_in_course(self, course_code):
        """
        Docstring for University.students_in_class()
            - Description: Returns the list of students in a specific course
            - Author: Jerod Abraham
            - Contributor(s): Lorenzo .S
        """
        course = self.get_course(course_code)
        if course:
            return course.students
        return []