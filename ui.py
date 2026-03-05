#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui.py
-------------

Description: Acts as a user interface for milestoneOne

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development (alpha)
"""

# ===== Imports =====

# Standard library
import csv

# Third-party
import streamlit as st
import pandas as pd

# Local application (your project modules)
from data_handler import DataHandler


# ===== Streamlit UI =====

def main():
    """
    Docstring for main
    """

    # ----- Page Setup -----
    st.set_page_config(page_title="MilestoneOne UI", page_icon="📚", layout="wide")

    st.title("MilestoneOne User Interface")
    st.write("Upload the required CSV files below.")

    st.divider()

    # ===== File Upload Section =====

    st.header("Upload Files")

    column_1, column_2 = st.columns(2)

    # ----- Upload File 1 -----
    with column_1:
        st.subheader("University Data File (CSV)")

        university_data_file = st.file_uploader(
            "University Data File CSV",
            type=["csv"],
            key="university_data_upload"
        )

        if university_data_file is not None:
            student_df = pd.read_csv(university_data_file)
            st.success("Student file uploaded successfully.")
            st.dataframe(student_df)

    # ----- Upload File 2 -----
    with column_2:
        st.subheader("Course Catalog File (CSV)")

        course_catalog_file = st.file_uploader(
            "Upload Course Catalog File CSV",
            type=["csv"],
            key="course_catalog_upload"
        )

        if course_catalog_file is not None:
            course_df = pd.read_csv(course_catalog_file)
            st.success("Course file uploaded successfully.")
            st.dataframe(course_df)

    st.divider()

    # !===== Backend File Handling =====! #

    data_handler_object = None  # (added) safe default

    if university_data_file and course_catalog_file:
        university_data_file.seek(0)
        course_catalog_file.seek(0)

        data_handler_object = DataHandler(university_data_file, course_catalog_file)

        data_handler_object.load_course_catalog()



    # ===== Placeholder for future logic =====
    st.header("Application Output")

    # ===== Action Picker + Conditional Inputs =====

    if not (university_data_file and course_catalog_file):
        st.info("Upload BOTH CSV files to enable the application actions.")
        return

    st.subheader("Choose an operation")

    action_options = [
        "Get list of students enrolled in a course",
        "Print GPA of a student",
        "Print all courses + course info (grades/credits) for a student",
        "Calculate mean/median/mode for a course",
        "Calculate mean/median for GPA of all students",
        "Print common students in two courses (intersection)"
    ]

    selected_action = st.selectbox(
        "What do you want to do?",
        options=action_options,
        key="selected_action"
    )

    st.divider()

    def _call_data_handler(method_names, *args, **kwargs):
        """
        Try multiple possible DataHandler method names without crashing the UI.
        Returns (success: bool, value_or_error: any)
        """
        for name in method_names:
            if hasattr(data_handler_object, name):
                try:
                    return True, getattr(data_handler_object, name)(*args, **kwargs)
                except Exception as e:
                    return False, f"Method '{name}' ran but raised an error: {e}"
        return False, (
            "I couldn't find a matching DataHandler method.\n\n"
            f"Expected one of these names: {method_names}\n"
            "Either rename your DataHandler function to match one of these, "
            "or tell me your real method name and I’ll wire it in."
        )

    # ---- 1) Students in a course ----
    if selected_action == "Get list of students enrolled in a course":
        with st.form("form_students_in_course"):
            course_id = st.text_input("Enter Course ID (ex: CSE2050)", key="course_id_students_list")
            submitted = st.form_submit_button("Get Students")

        if submitted:
            ok, result = _call_data_handler(
                ["get_students_in_course", "students_in_course", "get_course_students"],
                course_id
            )

            if ok:
                st.success("Students retrieved.")
                # If result looks like a DataFrame/list, display nicely:
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result, use_container_width=True)
                elif isinstance(result, (list, tuple, set)):
                    st.write(list(result))
                else:
                    st.write(result)
            else:
                st.error(result)

    # ---- 2) GPA of a student ----
    elif selected_action == "Print GPA of a student":
        with st.form("form_student_gpa"):
            student_id = st.text_input("Enter Student ID", key="student_id_gpa")
            submitted = st.form_submit_button("Get GPA")

        if submitted:
            ok, result = _call_data_handler(
                ["get_student_gpa", "student_gpa", "calculate_student_gpa"],
                student_id
            )

            if ok:
                st.success("GPA calculated.")
                st.write(result)
            else:
                st.error(result)

    # ---- 3) All courses + info for a student ----
    elif selected_action == "Print all courses + course info (grades/credits) for a student":
        with st.form("form_student_courses"):
            student_id = st.text_input("Enter Student ID", key="student_id_courses")
            submitted = st.form_submit_button("Get Student Courses")

        if submitted:
            ok, result = _call_data_handler(
                ["get_student_courses", "student_courses", "get_courses_for_student"],
                student_id
            )

            if ok:
                st.success("Courses retrieved.")
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result, use_container_width=True)
                elif isinstance(result, (list, tuple)):
                    st.write(result)
                elif isinstance(result, dict):
                    st.json(result)
                else:
                    st.write(result)
            else:
                st.error(result)

    # ---- 4) Mean/median/mode for a course ----
    elif selected_action == "Calculate mean/median/mode for a course":
        with st.form("form_course_stats"):
            course_id = st.text_input("Enter Course ID (ex: CSE2050)", key="course_id_stats")
            submitted = st.form_submit_button("Calculate Stats")

        if submitted:
            ok, result = _call_data_handler(
                ["get_course_statistics", "course_statistics", "calculate_course_statistics"],
                course_id
            )

            if ok:
                st.success("Course statistics computed.")
                # Common format: dict like {"mean":..., "median":..., "mode":...}
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.write(result)
            else:
                st.error(result)

    # ---- 5) Mean/median for university GPA ----
    elif selected_action == "Calculate mean/median for GPA of all students":
        with st.form("form_university_gpa_stats"):
            submitted = st.form_submit_button("Calculate University GPA Stats")

        if submitted:
            ok, result = _call_data_handler(
                ["get_university_gpa_statistics", "university_gpa_statistics", "calculate_university_gpa_statistics"]
            )

            if ok:
                st.success("University GPA statistics computed.")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.write(result)
            else:
                st.error(result)

    # ---- 6) Intersection between two courses ----
    elif selected_action == "Print common students in two courses (intersection)":
        with st.form("form_course_intersection"):
            course_id_1 = st.text_input("Enter Course ID #1", key="course_id_1_intersection")
            course_id_2 = st.text_input("Enter Course ID #2", key="course_id_2_intersection")
            submitted = st.form_submit_button("Find Common Students")

        if submitted:
            ok, result = _call_data_handler(
                ["get_common_students", "common_students", "course_intersection"],
                course_id_1, course_id_2
            )

            if ok:
                st.success("Intersection computed.")
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result, use_container_width=True)
                elif isinstance(result, (list, tuple, set)):
                    st.write(list(result))
                else:
                    st.write(result)
            else:
                st.error(result)

    else:
        st.write("Processing results will appear here.")


# ===== Run App =====

if __name__ == "__main__":
    main()