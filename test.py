"""
Program: test.py
Author: Shiqi Wang
Last date modified: 10/26/2020

The purpose of this program is to test method from Student class
"""
import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student_only_required = s.Student("Wang", "Shiqi", "Computer Science")
        self.student_all = s.Student("Wang", "Shiqi", "Computer Science", 4.0)

    def tearDown(self):
        del self.student_only_required
        del self.student_all

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student_only_required.last_name, 'Wang')
        self.assertEqual(self.student_only_required.first_name, "Shiqi")
        self.assertEqual(self.student_only_required.major, "Computer Science")

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student_all.last_name, 'Wang')
        self.assertEqual(self.student_all.first_name, "Shiqi")
        self.assertEqual(self.student_all.major, "Computer Science")
        self.assertEqual(self.student_all.gpa, 4.0)

    def test_student_str(self):
        self.assertEqual(str(self.student_all), 'Wang, Shiqi has major Computer Science with gpa: 4.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s.Student("123", "Shiqi", "Computer Science")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s.Student("Wang", "123", "Computer Science")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = s.Student("Wang", "Shiqi", "123")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s.Student("Wang", "Shiqi", "Computer Science", 3)
        with self.assertRaises(ValueError):
            student = s.Student("Wang", "Shiqi", "Computer Science", "abc")
        with self.assertRaises(ValueError):
            student = s.Student("Wang", "Shiqi", "Computer Science", 5.0)

if __name__ == '__main__':
    unittest.main()

