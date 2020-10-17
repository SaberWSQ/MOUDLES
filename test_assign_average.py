"""
Program: test_assign_average.py
Author: Shiqi Wang
Last date modified: 10/13/2020


The purpose of this program is to test function switch_average
"""
import unittest
from main.assign_average import switch_average


class TestSwitchAverage(unittest.TestCase):
    def test_key_A(self):
        self.assertEqual(switch_average('A'), 90)

    def test_key_a(self):
        self.assertEqual(switch_average('a'), 90)

    def test_key_B(self):
        self.assertEqual(switch_average('B'), 95)

    def test_key_C(self):
        self.assertEqual(switch_average('C'), 98)

    def test_key_D(self):
        self.assertEqual(switch_average('D'), 90)

    def test_non_key(self):
        with self.assertRaises(ValueError):
            switch_average('E')


if __name__ == '__main__':
    unittest.main()
