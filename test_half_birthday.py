"""
Program: test_half_birthday.py
Author: Shiqi Wang
Last date modified: 10/13/2020


The purpose of this program is to test function half_birthday
"""
import unittest
from main.half_birthday import half_birthday
from datetime import datetime


class TestHalfBirthday(unittest.TestCase):
    def setUp(self):
        self.date = datetime.strptime("2000-01-01", "%Y-%m-%d")
        self.target = datetime.strptime("2000-07-01", "%Y-%m-%d")

    def test_half_birthday(self):
        self.assertEqual(half_birthday(self.date), self.target)


if __name__ == '__main__':
    unittest.main()
