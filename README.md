# CSE 2050 – Group Project 
### University Course Management System

**Author(s):** Lorenzo Julian Serrano and Jerod Abraham
**Course:** CSE 2050 – Object-Oriented Programming & Data Structures  
**Institution:** University of Connecticut  

---

# Project Overview

This project implements a simple **University Course Management System** using object-oriented programming principles in Python.

The system models relationships between **students and courses**, allowing operations such as:

- Enrolling students in courses
- Recording grades
- Calculating GPA
- Querying course rosters
- Performing statistical analysis on course grades

The goal of this project is to demonstrate **modular design, object-oriented programming, and data management in Python**.

---

# Features

### Student Management
- Create student objects
- Enroll students in courses
- Store grades
- Calculate GPA

### Course Management
- Create course objects
- Maintain course rosters
- Associate students with courses

### Data Queries
- List students enrolled in a course
- Retrieve course information for a student
- Compute statistics such as:
  - Mean
  - Median
  - Mode

### Data Handling
- Load student and course data from CSV files
- Manage operations through a centralized **DataHandler** class

---

# Project Structure

```
milestoneOne/
│
├── required_classes/
│   ├── student.py
│   ├── course.py
│   ├── university.py
│
├── tests/
│   ├── test_student.py
│   ├── test_course.py
│   ├── test_university.py
│   └── test_data_handler.py
│
├── csv_files/
│   └── course_catalog(in).csv
|   └── university_data(in).csv
│
└── README.md
└── data_handler.py
└── ui.py (this will be run with streamlit)
└── requirement.txt

```

---

# Class Overview

## Student

Represents an individual student.

Responsibilities:
- Store student ID and name
- Track enrolled courses
- Store grades
- Compute GPA

---

## Course

Represents a university course.

Responsibilities:
- Store course code
- Maintain a roster of enrolled students
- Add or remove students

---

## University

Represents the overall academic system.

Responsibilities:
- Maintain collections of students and courses
- Coordinate interactions between students and courses

---

## DataHandler

Handles external data operations.

Responsibilities:
- Load data from CSV files
- Query enrolled students
- Compute course statistics

---

# Installation

Clone the repository:

```bash
git clone https://github.com/LorenzoJSDev/CSE-2050-Milestone-One
```

Navigate to the project directory:

```bash
cd milestoneOne
```

Install dependencies (if needed):

```bash
pip install -r requirements.txt
```

---

# Running the Project

Cd into the repo and in your terminal write the following command.

```bash
  python -m streamlit run ui.py
```

This will open a tab in your browser that will allow you to access the UI.

---

# Running Tests

Tests are implemented using Python's **unittest** framework.

Run all tests:

```bash
python -m unittest discover tests
```

Run a specific test file:

```bash
python -m unittest tests/test_student.py
```

---
