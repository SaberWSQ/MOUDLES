"""
Program: test_valid_input_in_functions.py
Author: Shiqi Wang
Last date modified: 09/10/2020



The purpose of this program is to test function score_input
"""
import unittest
from more_functions.validate_input_in_functions import score_input


class ScoreInputCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input(test_name="Shiqi Wang"), "Test name: Shiqi Wang\nTest score: 0.0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input(test_name="Shiqi Wang", test_score='50'), "Test name: Shiqi Wang\nTest score: 50.0")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input(test_name="Shiqi Wang", test_score='-20'), "Invalid test score, try again")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(score_input(test_name="Shiqi Wang", test_score='200'), "Invalid test score, try again")

    def test_test_score_non_numeric(self):
        with self.assertRaises(ValueError):
            score_input(test_name="Shiqi Wang", test_score='$%&*&')

    def test_score_input_invalid_message(self):
        self.assertEqual(score_input(test_name="Shiqi Wang", test_score='-50', invalid_message="Try again"), "Try again")


if __name__ == '__main__':
    unittest.main()
