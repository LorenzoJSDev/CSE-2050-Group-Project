#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data_handler.py
-------------

Description: Handles uploaded data, and data query's

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development (alpha)

"""


# ===== Imports =====

# Standard library
import csv
import statistics

# Third-party
import pandas as pd


# Local application (your project modules)
from required_classes.university import University



# ===== Classes =====

class DataHandler:
    """
    Docstring for Course class
        - Description: The data_handler class for milestone one, handles loading data, and data query's for milestoneOne project
        - Author: Lorenzo .S
    """

    def __init__(self, university_data_file, course_catalog_file, enrollment_file) -> None:
        """
        Docstring for DataHandler.__init__()
            - Description: TBD
            - Author: Lorenzo .S
        """
        self.university_data_file = university_data_file
        self.course_catalog_file = course_catalog_file
        self.enrollment_file = enrollment_file
        self.university_obj = University()


    # ---- Data Loaders ---- #

    def load_course_catalog(self) -> None:
        csv_reader = csv.DictReader(self.course_catalog_file)

        for row in csv_reader:
            course_id = row["course_id"].strip()
            credits = int(row["credits"])
            capacity = int(row["capacity"])

            self.university_obj.add_course(course_id, credits, capacity)
        return

    def load_university_data(self) -> None:
        csv_reader = csv.DictReader(self.university_data_file)

        for row in csv_reader:
            student_id = row["student_id"].strip()
            name = row["name"].strip()

            self.university_obj.add_student(student_id, name)

            courses_field = row.get("courses", "").strip()

            if not courses_field:
                continue

            courses = courses_field.split(";")

            for course_entry in courses:
                course_entry = course_entry.strip()

                if not course_entry or ":" not in course_entry:
                    continue

                course_id, course_grade = course_entry.split(":", 1)
                course_id = course_id.strip()
                course_grade = course_grade.strip()

                if course_id not in self.university_obj.courses:
                    continue

                course_obj = self.university_obj.get_course(course_id)
                student_obj = self.university_obj.get_student(student_id)
                student_obj.enroll(course_obj, course_grade)
        return

    def load_enrollment_data(self) -> None:
        pass

    # ---- Data Query Methods ---- #

    def query_list_of_enrolled_students(self, course_code):
        """
        Docstring for DataHandler.list_enrolled_students()
            - Description: Queries the list of enrolled students for a given course code.
            - Author: Lorenzo .S
        """
        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        students_in_course = self.university_obj.get_students_in_course(course_code)

        if students_in_course:
            rows = []
            for student in students_in_course:
                rows.append({"student_id": student.student_id , "student_name":student.name})
            return pd.DataFrame(rows)
        else:
            return f"There are currently no students enrolled in course: {course_code}"


    def query_student_gpa(self,student_id):
        """
        Docstring for DataHandler.query_student_gpa()
            - Description: Queries the GPA for a given student ID.
            - Author: Lorenzo .S
        """

        if student_id not in self.university_obj.students:
            return f"{student_id} is not a registered student."

        student = self.university_obj.get_student(student_id)

        gpa = student.calculate_gpa()

        return f" {student_id}s current gpa is {gpa}"

    def query_student_courses_and_course_info(self,student_id):
        """
        Docstring for DataHandler.query_student_courses_and_course_info()
            - Description: Queries the courses and courses info for a given student ID.
            - Author: Lorenzo .S
        """
        if student_id not in self.university_obj.students:
            return f"{student_id} is not a registered student."

        student_courses_and_course_info = self.university_obj.students[student_id].get_course_info()

        if student_courses_and_course_info:
            return pd.DataFrame(student_courses_and_course_info)
        else:
            return f"{student_id} is currently not enrolled in any courses"

    def query_mean_median_mode_for_course(self, course_code):
        """
        Docstring for DataHandler.query_mean_median_for_course()
            - Description: Queries the mean median mode for a given course code.
            - Author: Lorenzo .S
        """

        total_student_points = 0

        student_grades = []

        for student in self.university_obj.get_course(course_code).students:
            student_grade_points = student.GRADE_POINTS[student.courses[self.university_obj.get_course(course_code)]]
            total_student_points += student_grade_points
            student_grades.append(student_grade_points)

        mean = round(total_student_points / len(student_grades),2)
        student_grades.sort()
        median = student_grades[len(student_grades)//2]
        mode = statistics.mode(student_grades)

        rows = []
        rows.append({"Course":course_code,"Mean": mean , "Median": median, "Mode": mode})
        return pd.DataFrame(rows)

    def query_university_gpa_mean_and_median(self):

        students = self.university_obj.students.values()

        total_gpa = 0

        individual_gpa = []

        for student in students:
            gpa = student.calculate_gpa()
            total_gpa += gpa
            individual_gpa.append(gpa)

        total_students = len(students)

        mean = round(total_gpa / len(students),2)
        individual_gpa.sort()
        median = round(total_students / len(students),2)

        rows = []
        rows.append({"Mean": mean, "Median": median})
        return pd.DataFrame(rows)

    def query_common_students_in_two_courses(self,course_code1,course_code2):

        students_in_course1 = self.university_obj.get_students_in_course(course_code1)

        students_in_course2 = self.university_obj.get_students_in_course(course_code2)

        common_students_in_two_courses = set(students_in_course1).intersection(set(students_in_course2))

        if common_students_in_two_courses:
            rows = []
            for student in common_students_in_two_courses:
                rows.append({"student_id": student.student_id , "student_name":student.name})

            return pd.DataFrame(rows)





