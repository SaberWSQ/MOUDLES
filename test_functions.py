"""
Program: unit_test.py
Author: Shiqi Wang
Last date modified: 09/02/2020



The purpose of this program is to test function convert_to_months
"""

import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_correct_age(self):
        self.assertEqual(camper_age_input.convert_to_months('3'), 36)

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, camper_age_input.convert_to_months, 'years')

    def test_invalid_input_value(self):
        self.assertRaises(ValueError, camper_age_input.convert_to_months, '80')


if __name__ == '__main__':
    unittest.main()
