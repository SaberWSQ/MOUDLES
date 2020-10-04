"""
Program: test_inner_functions_assignment.py
Author: Shiqi Wang
Last date modified: 10/01/2020

The purpose of this program is to test function measurements.
"""
import unittest
from main.inner_functions_assignment import measurements

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(measurements([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.main()
