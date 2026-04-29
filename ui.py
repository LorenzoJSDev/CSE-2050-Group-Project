#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui.py
-------------

Description: Streamlit user interface for the CSE2050 group project through Milestone 3.

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development (alpha)
"""

# ===== Imports =====

# Standard library
import io

# Third-party
import streamlit as st
import pandas as pd

# Local application
from data_handler import DataHandler


def display_result(result) -> None:
    """
    Docstring for display_result()
        - Description: Displays query results in Streamlit using the best available format.
        - Author: Lorenzo .S
    """
    if isinstance(result, pd.DataFrame):
        st.dataframe(result, use_container_width=True)
    elif isinstance(result, dict):
        st.json(result)
    elif isinstance(result, (list, tuple, set)):
        st.write(list(result))
    else:
        st.write(result)


def convert_uploaded_file(uploaded_file):
    """
    Docstring for convert_uploaded_file()
        - Description: Converts a Streamlit uploaded file into a text file-like object.
        - Author: Lorenzo .S
    """
    uploaded_file.seek(0)
    return io.TextIOWrapper(uploaded_file, encoding="utf-8")


def preview_csv(uploaded_file, success_message: str) -> None:
    """
    Docstring for preview_csv()
        - Description: Displays a preview of an uploaded CSV file in the Streamlit interface.
        - Author: Lorenzo .S
    """
    if uploaded_file is not None:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file)
        st.success(success_message)
        st.dataframe(df, use_container_width=True)
        uploaded_file.seek(0)


def main():
    """
    Docstring for main()
        - Description: Sets up and runs the Streamlit user interface for project data loading and queries.
        - Author: Lorenzo .S
    """

    st.set_page_config(page_title="CSE2050 Milestone 3 UI", page_icon="📚", layout="wide")

    st.title("CSE2050 Group Project Interface")
    st.write("Upload the required CSV files below to load the university system.")

    st.divider()

    # ===== File Upload Section =====

    st.header("Upload Files")

    column_1, column_2 = st.columns(2)

    with column_1:
        st.subheader("University Data File")

        university_data_file = st.file_uploader(
            "Upload university_data.csv",
            type=["csv"],
            key="university_data_upload"
        )

        preview_csv(university_data_file, "University data file uploaded successfully.")

    with column_2:
        st.subheader("Course Catalog File")

        course_catalog_file = st.file_uploader(
            "Upload course catalog CSV",
            type=["csv"],
            key="course_catalog_upload"
        )

        preview_csv(course_catalog_file, "Course catalog file uploaded successfully.")

    column_3, column_4 = st.columns(2)

    with column_3:
        st.subheader("Enrollment File")

        enrollment_file = st.file_uploader(
            "Upload enrollment CSV",
            type=["csv"],
            key="enrollment_upload"
        )

        preview_csv(enrollment_file, "Enrollment file uploaded successfully.")

    with column_4:
        st.subheader("Prerequisite File")

        prerequisite_file = st.file_uploader(
            "Upload prerequisite CSV",
            type=["csv"],
            key="prerequisite_upload"
        )

        preview_csv(prerequisite_file, "Prerequisite file uploaded successfully.")

    st.divider()

    required_files_uploaded = (
        university_data_file is not None
        and course_catalog_file is not None
        and enrollment_file is not None
        and prerequisite_file is not None
    )

    if not required_files_uploaded:
        st.info("Upload all four CSV files to enable the application actions.")
        return

    # ===== Backend File Handling =====

    try:
        university_data_file_text = convert_uploaded_file(university_data_file)
        course_catalog_file_text = convert_uploaded_file(course_catalog_file)
        enrollment_file_text = convert_uploaded_file(enrollment_file)
        prerequisite_file_text = convert_uploaded_file(prerequisite_file)

        data_handler_object = DataHandler(
            university_data_file_text,
            course_catalog_file_text,
            enrollment_file_text,
            prerequisite_file_text
        )

        data_handler_object.load_course_catalog()
        data_handler_object.load_university_data()
        data_handler_object.load_prerequisite_data()
        data_handler_object.load_enrollment_data()

        st.success("All files loaded successfully.")

    except Exception as error:
        st.error(f"Error while loading files: {error}")
        return

    # ===== Query Section =====

    st.header("Query Data")

    action_options = [
        "Get list of students enrolled in a course",
        "Get waitlist for a course",
        "Get course enrollment status",
        "Get prerequisites for a course",
        "Check student prerequisite eligibility",
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

    # ===== Query Actions =====

    if selected_action == "Get list of students enrolled in a course":
        with st.form("form_students_in_course"):
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Get Students")

        if submitted:
            result = data_handler_object.query_list_of_enrolled_students(course_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Get waitlist for a course":
        with st.form("form_course_waitlist"):
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Get Waitlist")

        if submitted:
            result = data_handler_object.query_waitlist_for_course(course_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Get course enrollment status":
        with st.form("form_course_enrollment_status"):
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Get Enrollment Status")

        if submitted:
            result = data_handler_object.query_course_enrollment_status(course_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Get prerequisites for a course":
        with st.form("form_course_prerequisites"):
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Get Prerequisites")

        if submitted:
            result = data_handler_object.query_prerequisites_for_course(course_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Check student prerequisite eligibility":
        with st.form("form_student_prerequisite_eligibility"):
            student_id = st.text_input("Enter Student ID, example: STU00001")
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Check Eligibility")

        if submitted:
            result = data_handler_object.query_student_prerequisite_eligibility(
                student_id.strip(),
                course_id.strip()
            )
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Print GPA of a student":
        with st.form("form_student_gpa"):
            student_id = st.text_input("Enter Student ID, example: STU00001")
            submitted = st.form_submit_button("Get GPA")

        if submitted:
            result = data_handler_object.query_student_gpa(student_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Print all courses + course info (grades/credits) for a student":
        with st.form("form_student_courses"):
            student_id = st.text_input("Enter Student ID, example: STU00001")
            submitted = st.form_submit_button("Get Student Courses")

        if submitted:
            result = data_handler_object.query_student_courses_and_course_info(student_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Calculate mean/median/mode for a course":
        with st.form("form_course_stats"):
            course_id = st.text_input("Enter Course ID, example: CSE2050")
            submitted = st.form_submit_button("Calculate Stats")

        if submitted:
            result = data_handler_object.query_mean_median_mode_for_course(course_id.strip())
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Calculate mean/median for GPA of all students":
        with st.form("form_university_gpa_stats"):
            submitted = st.form_submit_button("Calculate University GPA Stats")

        if submitted:
            result = data_handler_object.query_university_gpa_mean_and_median()
            st.success("Query completed.")
            display_result(result)

    elif selected_action == "Print common students in two courses (intersection)":
        with st.form("form_course_intersection"):
            course_id_1 = st.text_input("Enter Course ID #1")
            course_id_2 = st.text_input("Enter Course ID #2")
            submitted = st.form_submit_button("Find Common Students")

        if submitted:
            result = data_handler_object.query_common_students_in_two_courses(
                course_id_1.strip(),
                course_id_2.strip()
            )
            st.success("Query completed.")
            display_result(result)


if __name__ == "__main__":
    main()