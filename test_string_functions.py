"""
Program: test_string_functions.py
Author: Shiqi Wang
Last date modified: 09/10/2020



The purpose of this program is to test function multiply_string
"""
import unittest
from more_functions import string_functions

class StringTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string("Shiqi", 5), "ShiqiShiqiShiqiShiqiShiqi")


if __name__ == '__main__':
    unittest.main()
