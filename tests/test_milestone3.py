import unittest
from required_classes.course import Course
from required_classes.student import Student
from required_classes.data_structures.hash_map import HashMap

class TestMilestone3Course(unittest.TestCase):
    """
    Docstring for TestMilestone3Course
        - Description: Contains unit tests for Milestone 3 Course functionality including prerequisite checks and sorting.
        - Author: Jerod Abraham
    """

    def setUp(self):
        """
        Docstring for TestMilestone3Course.setUp()
            - Description: Runs before every test, so each test has access to initialized Course and Student objects.
            - Author: Jerod Abraham
        """
        self.course = Course("CSE2050", 3, 3)

        self.student1 = Student("STU10001", "Paul")
        self.student2 = Student("STU10002", "Peter")
        self.student3 = Student("STU10003", "John")

    def test_enrollment_prerequisite_missing(self):
        """
        Docstring for TestMilestone3Course.test_enrollment_prerequisite_missing()
            - Description: Tests that a student without required prerequisites is correctly denied enrollment.
            - Author: Jerod Abraham
        """
        self.course.add_prerequisite("CSE1010")
        self.assertFalse(self.course.has_completed_prerequisites(self.student1))

    def test_enrollment_prerequisite_completed(self):
        """
        Docstring for TestMilestone3Course.test_enrollment_prerequisite_completed()
            - Description: Tests that a student who has completed prerequisites with a passing grade is allowed enrollment.
            - Author: Jerod Abraham
        """
        prereq = Course("CSE1010", 3, 3)
        self.student1.courses[prereq] = "A"

        self.course.add_prerequisite("CSE1010")
        self.assertTrue(self.course.has_completed_prerequisites(self.student1))

    def test_sort_roster_by_id_merge(self):
        """
        Docstring for TestMilestone3Course.test_sort_roster_by_id_merge()
            - Description: Tests that the enrolled roster is correctly sorted by student ID using merge sort.
            - Author: Jerod Abraham
        """
        self.course.prerequisite = HashMap()

        self.course.request_enroll(self.student3, "2026-03-27")
        self.course.request_enroll(self.student1, "2026-03-25")
        self.course.request_enroll(self.student2, "2026-03-26")

        self.course.sort_enrolled("id", "merge")

        self.assertEqual(
            [r.student.student_id for r in self.course.enrolled],
            ["STU10001", "STU10002", "STU10003"]
        )

    def test_sort_roster_by_name_quick(self):
        """
        Docstring for TestMilestone3Course.test_sort_roster_by_name_quick()
            - Description: Tests that the enrolled roster is correctly sorted by student name using quick sort.
            - Author: Jerod Abraham
        """
        self.course.prerequisite = HashMap()

        self.course.request_enroll(self.student3, "2026-03-27")
        self.course.request_enroll(self.student1, "2026-03-25")
        self.course.request_enroll(self.student2, "2026-03-26")

        self.course.sort_enrolled("name", "quick")

        self.assertEqual(
            [r.student.name for r in self.course.enrolled],
            ["Peter", "John", "Paul"]
        )

    def test_sort_roster_by_date_merge(self):
        """
        Docstring for TestMilestone3Course.test_sort_roster_by_date_merge()
            - Description: Tests that the enrolled roster is correctly sorted by enrollment date using merge sort.
            - Author: Jerod Abraham
        """
        self.course.prerequisite = HashMap()

        self.course.request_enroll(self.student3, "2026-03-27")
        self.course.request_enroll(self.student1, "2026-03-25")
        self.course.request_enroll(self.student2, "2026-03-26")

        self.course.sort_enrolled("date", "merge")

        self.assertEqual(
            [r.enroll_date for r in self.course.enrolled],
            ["2026-03-25", "2026-03-26", "2026-03-27"]
        )

    def test_sort_roster_by_date_quick(self):
        """
        Docstring for TestMilestone3Course.test_sort_roster_by_date_quick()
            - Description: Tests that the enrolled roster is correctly sorted by enrollment date using quick sort.
            - Author: Jerod Abraham
        """
        self.course.prerequisite = HashMap()

        self.course.request_enroll(self.student3, "2026-03-27")
        self.course.request_enroll(self.student1, "2026-03-25")
        self.course.request_enroll(self.student2, "2026-03-26")

        self.course.sort_enrolled("date", "quick")

        self.assertEqual(
            [r.enroll_date for r in self.course.enrolled],
            ["2026-03-25", "2026-03-26", "2026-03-27"]
        )


if __name__ == "__main__":
    unittest.main()