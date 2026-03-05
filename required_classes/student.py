#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student.py
-------------

Description: Contains the student class for the milestone One project

Author: Lorenzo Julian Serrano
Contributors:
Date Created: 03-03-2026
Status: Development (alpha)


TO DO:
    * Add Unenroll method
    * Add __str__ method

"""

# ===== Imports =====

# Standard library


# Third-party


# Local application (your project modules)
from required_classes.course import Course

# ===== Classes =====
class Student:
    """
    Docstring for Student class
        - Description: The student class for the milestone One project
        - Contributor(s): "Lorenzo .J Serrano"
    """

    GRADE_POINTS = {
        'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D': 1.0,
        'F': 0.0
    }

    def __init__(self, student_id: str, name: str, courses: dict = None):
        """
        Docstring for Student.__init__() method
            - Description: The constructor for Student class instances / objects
            - Author: Lorenzo .S
        """
        self.student_id = student_id
        self.name = name
        self.courses = {} if courses is None else courses

    def __str__(self):
        """
        Docstring for Student.__str__() method
            - Description: TBD
            - Contributor(s): Lorenzo .J Serrano
        """
        return f"{self.student_id},{self.name}.{self.courses}"

    def enroll(self, course: Course, grade: str):
        """
        Docstring for Student.enroll() method
            - Description: Adds a course_object:"grade" key value pair to self.courses dictionary if the key does not exist in self.courses
            - Author: Lorenzo .S
        """

        if course not in self.courses.keys():
            if grade in self.GRADE_POINTS:
                self.courses[course] = grade
                course.add_student(self)
            else:
                raise ValueError(f"{grade} is not a valid grade input")
        else:
            raise ValueError(f"Student is already enrolled in '{course}'.")

        return

    def update_grade(self, course: Course, grade: str):
        """
        Docstring for Student.update_grade() method
            - Description: Updates a selected course_object:"grade" key value pair in the self.courses dictionary if the key exists in self.courses
            - Author: Lorenzo .S
        """

        if course in self.courses.keys():
            if grade in self.GRADE_POINTS:
                self.courses[course] = grade
            else:
                raise ValueError(f"{grade} is not a valid grade input")
        else:
            raise ValueError(f"Student is not enrolled in '{course}'.")

        return

    def calculate_gpa(self):
        """
        Docstring for Student.calculate_gpa() method
            - Description: Calculates the GPA for this student.
            - Author: Lorenzo .S
        """
        total_points = 0
        total_credits = 0

        for course in self.courses.keys():

            x = course.course_credits * self.GRADE_POINTS[self.courses[course]]

            total_points += x

            total_credits += course.course_credits

        if total_points == 0 or total_credits == 0:
            gpa = 0.0
        else:
            gpa = total_points/total_credits

        return round(gpa,2)

    def get_courses(self):
        """
        Docstring for Student.get_courses() method
            - Description: Returns a list of courses a student is enrolled in.
            - Author: Lorenzo .S
        """
        return self.courses.keys()


    def get_course_info(self):
        """
        Docstring for Student.get_course_info() method
            - Description: Returns a list of courses a student is enrolled in.
            - Author: Lorenzo .S
        """
        courses_info = []

        for course in self.courses:
            courses_info.append({
                "course_code": course.course_code,
                "grade": self.courses[course],
                "credits": course.course_credits
            })

        return courses_info