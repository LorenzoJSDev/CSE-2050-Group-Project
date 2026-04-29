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
import datetime

# Third-party
import pandas as pd

# Local application
from required_classes.university import University


# ===== Classes =====

class DataHandler:
    """
    Docstring for Course class
        - Description: The data_handler class for milestone one, handles loading data, and data query's for milestoneOne project
        - Author: Lorenzo .S
    """

    def __init__(self, university_data_file, course_catalog_file, enrollment_file, prerequisite_file=None) -> None:
        """
        Docstring for DataHandler.__init__()
            - Description: Initializes the DataHandler with file objects and creates a University object.
            - Author: Lorenzo .S
        """
        self.university_data_file = university_data_file
        self.course_catalog_file = course_catalog_file
        self.enrollment_file = enrollment_file
        self.prerequisite_file = prerequisite_file
        self.university_obj = University()

    # ---- Data Loaders ---- #

    def load_course_catalog(self) -> None:
        """
        Docstring for DataHandler.load_course_catalog()
            - Description: Loads the data from the course catalog file into the university object.
            - Author: Lorenzo .S
        """
        csv_reader = csv.DictReader(self.course_catalog_file)

        for row in csv_reader:
            course_id = row["course_id"].strip()
            credits = int(row["credits"])
            capacity = int(row["capacity"])

            self.university_obj.add_course(course_id, credits, capacity)
        return

    def load_university_data(self) -> None:
        """
        Docstring for DataHandler.load_university_data()
            - Description: Loads the data from the university data file into the university object.
            - Author: Lorenzo .S
        """
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
        """
        Docstring for DataHandler.load_enrollment_data()
            - Description: Loads active enrollment request data into the university object while skipping invalid prerequisite enrollments.
            - Author: Lorenzo .S
        """
        csv_reader = csv.DictReader(self.enrollment_file)

        for row in csv_reader:
            student_id = row["student_id"].strip()
            course_id = row["course_id"].strip()

            if student_id not in self.university_obj.students:
                continue

            if course_id not in self.university_obj.courses:
                continue

            student = self.university_obj.get_student(student_id)
            course = self.university_obj.get_course(course_id)

            enroll_date = datetime.date.today()

            try:
                course.request_enroll(student, enroll_date)
            except ValueError:
                continue

    def load_prerequisite_data(self) -> None:
        """
        Docstring for DataHandler.load_prerequisite_data()
            - Description: Loads prerequisite data into each Course object's HashMap.
            - Author: Lorenzo .S
        """
        if self.prerequisite_file is None:
            return

        self.prerequisite_file.seek(0)

        for line in self.prerequisite_file:
            line = line.strip().replace('"', "")

            if not line or line.lower().startswith("course_id"):
                continue

            parts = line.split()

            if len(parts) < 2:
                continue

            course_id = parts[0].strip()
            prerequisite = parts[1].strip()

            if course_id in self.university_obj.courses:
                course = self.university_obj.get_course(course_id)
                course.add_prerequisite(prerequisite)

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
                rows.append({"student_id": student.student_id, "student_name": student.name})
            return pd.DataFrame(rows)
        else:
            return f"There are currently no students enrolled in course: {course_code}"

    def query_student_gpa(self, student_id):
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

    def query_student_courses_and_course_info(self, student_id):
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
        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        course = self.university_obj.get_course(course_code)
        students_in_course = self.university_obj.get_students_in_course(course_code)

        if not students_in_course:
            return f"There are currently no students enrolled in course: {course_code}"

        total_student_points = 0
        student_grades = []

        for student in students_in_course:
            if course in student.courses:
                student_grade_points = student.GRADE_POINTS[student.courses[course]]
                total_student_points += student_grade_points
                student_grades.append(student_grade_points)

        if not student_grades:
            return f"There are currently no graded students enrolled in course: {course_code}"

        mean = round(total_student_points / len(student_grades), 2)
        median = statistics.median(student_grades)
        mode = statistics.mode(student_grades)

        rows = []
        rows.append({"Course": course_code, "Mean": mean, "Median": median, "Mode": mode})
        return pd.DataFrame(rows)

    def query_university_gpa_mean_and_median(self):
        """
        Docstring for DataHandler.query_university_gpa_mean_and_median()
            - Description: Queries the university GPA mean and median.
            - Author: Lorenzo .S
        """
        students = list(self.university_obj.students.values())

        if not students:
            rows = []
            rows.append({"Mean": 0.0, "Median": 0.0})
            return pd.DataFrame(rows)

        individual_gpa = []

        for student in students:
            gpa = student.calculate_gpa()
            individual_gpa.append(gpa)

        mean = round(sum(individual_gpa) / len(individual_gpa), 2)
        median = round(statistics.median(individual_gpa), 2)

        rows = []
        rows.append({"Mean": mean, "Median": median})
        return pd.DataFrame(rows)

    def query_common_students_in_two_courses(self, course_code1, course_code2):
        """
        Docstring for DataHandler.query_common_students_in_two_courses()
            - Description: Returns the students common to two courses.
            - Author: Lorenzo .S
        """
        students_in_course1 = self.university_obj.get_students_in_course(course_code1)
        students_in_course2 = self.university_obj.get_students_in_course(course_code2)

        common_students_in_two_courses = set(students_in_course1).intersection(set(students_in_course2))

        if common_students_in_two_courses:
            rows = []
            for student in common_students_in_two_courses:
                rows.append({"student_id": student.student_id, "student_name": student.name})

            return pd.DataFrame(rows)

        return f"There are no common students in {course_code1} and {course_code2}"

    def query_waitlist_for_course(self, course_code):
        """
        Docstring for DataHandler.query_waitlist_for_course()
            - Description: Returns the students currently waiting for a given course.
            - Author: Lorenzo .S
        """
        course_code = course_code.strip()

        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        course = self.university_obj.get_course(course_code)

        rows = []
        current = course.waitlist.front

        while current is not None:
            student = current.data
            rows.append({
                "student_id": student.student_id,
                "student_name": student.name
            })
            current = current.next

        if not rows:
            return f"There are currently no students on the waitlist for {course_code}."

        return pd.DataFrame(rows)

    def query_course_enrollment_status(self, course_code):
        """
        Docstring for DataHandler.query_course_enrollment_status()
            - Description: Returns enrollment count, capacity, available seats, and waitlist size for a course.
            - Author: Lorenzo .S
        """
        course_code = course_code.strip()

        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        course = self.university_obj.get_course(course_code)

        rows = [{
            "course_code": course.course_code,
            "enrolled_count": len(course.enrolled),
            "capacity": course.capacity,
            "available_seats": course.capacity - len(course.enrolled),
            "waitlist_count": len(course.waitlist)
        }]

        return pd.DataFrame(rows)

    def query_prerequisites_for_course(self, course_code):
        """
        Docstring for DataHandler.query_prerequisites_for_course()
            - Description: Returns the prerequisite course codes for a given course.
            - Author: Lorenzo .S
        """
        course_code = course_code.strip()

        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        course = self.university_obj.get_course(course_code)
        prerequisite_codes = course.prerequisite.keys()

        if not prerequisite_codes:
            return f"{course_code} does not have any listed prerequisites."

        rows = []

        for prerequisite in prerequisite_codes:
            rows.append({
                "course_code": course_code,
                "prerequisite": prerequisite
            })

        return pd.DataFrame(rows)

    def query_student_prerequisite_eligibility(self, student_id, course_code):
        """
        Docstring for DataHandler.query_student_prerequisite_eligibility()
            - Description: Checks whether a student has completed the prerequisites for a course.
            - Author: Lorenzo .S
        """
        student_id = student_id.strip()
        course_code = course_code.strip()

        if student_id not in self.university_obj.students:
            return f"{student_id} is not a registered student."

        if course_code not in self.university_obj.courses:
            return f"{course_code} is not a registered course."

        student = self.university_obj.get_student(student_id)
        course = self.university_obj.get_course(course_code)

        is_eligible = course.has_completed_prerequisites(student)

        rows = [{
            "student_id": student_id,
            "student_name": student.name,
            "course_code": course_code,
            "eligible": is_eligible
        }]

        return pd.DataFrame(rows)