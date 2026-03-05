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

# Third-party


# Local application (your project modules)
from required_classes.university import University



# ===== Classes =====

class DataHandler:
    """
    Docstring for Course class
        - Description: The data_handler class for milestone one, handles loading data, and data query's for milestoneOne project
        - Author: Lorenzo .S
    """

    def __init__(self, university_data_file, course_catalog_file) -> None:
        """
        Docstring for __init__
            - Description: TBD
            - Author: Lorenzo .S

        """
        self.university_data_file = university_data_file
        self.course_catalog_file = course_catalog_file
        self.university_obj = University()




    # ---- Data Loaders ---- #

    def load_course_catalog(self):
        """
        Docstring for load_course_catalog
            - Description: Loads the data from course_catalog into the university object.
            - Author: Lorenzo .S

        """
        csv_reader = csv.DictReader(self.course_catalog_file)

        for row in csv_reader:
            self.university_obj.add_course(row['course_code'], int(row['credits']))



    def load_university_data(self) -> None:

        csv_reader = csv.DictReader(self.university_data_file)

        for row in csv_reader:
            self.university_obj.add_student(row['student_id'], row['name'])

