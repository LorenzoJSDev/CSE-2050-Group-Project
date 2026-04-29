# CSE 2050 – Group Project 
### University Course Management System (Milestones 1–3)

**Author(s):** Lorenzo Julian Serrano and Jerod Abraham  
**Course:** CSE 2050 – Object-Oriented Programming & Data Structures  
**Institution:** University of Connecticut  

---

# Project Overview

This project implements a comprehensive **University Course Management System** using object-oriented programming principles and custom data structures in Python.

The system models relationships between **students, courses, enrollment records, prerequisites, and university operations**, allowing advanced academic management across all three project milestones.

### Core system operations include:

- Enrolling students in courses
- Managing course capacities
- Maintaining waitlists
- Recording grades
- Calculating GPA
- Querying course rosters
- Sorting rosters
- Binary searching student records
- Managing prerequisite validation
- Performing statistical analysis
- Loading multiple CSV datasets
- Providing a full Streamlit-based interface

The goal of this project is to demonstrate:

- Modular software design
- Object-oriented programming
- Custom data structures
- Algorithm implementation
- Data management in Python

---

# Features

### Student Management
- Create and validate student objects
- Enroll students in courses
- Prevent duplicate enrollments
- Store grades
- Update grades
- Calculate GPA
- Retrieve complete academic history

### Course Management
- Create course objects
- Store course credits and capacities
- Maintain enrolled rosters
- Maintain waitlists
- Add/drop students
- Promote waitlisted students automatically
- Sort rosters by:
  - Name
  - Student ID
  - Enrollment date
- Support:
  - Merge Sort
  - Quick Sort
- Perform recursive binary search

### Prerequisite Management (Milestone 3)
- Store prerequisites using custom HashMap
- Validate student eligibility
- Prevent invalid enrollments
- Query prerequisites
- Query student eligibility

### Data Queries
- List students enrolled in a course
- View course waitlists
- View course enrollment capacity
- View course prerequisites
- Check student prerequisite eligibility
- Retrieve course information for a student
- Retrieve GPA
- Compute:
  - Mean
  - Median
  - Mode
- Compute university-wide GPA mean and median
- View common students between courses

### Data Handling
- Load:
  - University student data
  - Course catalog
  - Enrollment requests
  - Prerequisite data
- Parse malformed or nonstandard CSV formatting
- Manage operations through a centralized **DataHandler** class

### User Interface
- Streamlit-based web interface
- Upload CSV files
- Interactive query tools
- Full academic management dashboard

---

# Project Structure

```bash
CSE-2050-Group-Project/
│
├── required_classes/
│   ├── student.py
│   ├── course.py
│   ├── university.py
│   │
│   └── data_structures/
│       ├── linked_queue.py
│       ├── hash_map.py
│       └── enrollment_record.py
│
├── tests/
│   ├── test_student.py
│   ├── test_course.py
│   ├── test_university.py
│   ├── test_data_handler.py
│   ├── test_linked_queue.py
│   ├── test_hash_map.py
│   ├── test_enrollment_record.py
│   └── test_milestone3.py
│
├── csv_files/
│   ├── milestone3_university_data.csv
│   ├── milestone3_course_catalog_CSE10_with_capacity.csv
│   ├── milestone_3_enrollments_CSE10.csv
│   └── milestone3_cse_prerequisites.csv
│
├── README.md
├── data_handler.py
├── ui.py
└── requirements.txt
---

# Installation

Clone the repository:

```bash
git clone https://github.com/LorenzoJSDev/CSE-2050-Group-Project
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
