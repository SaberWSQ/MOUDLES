"""
Program: test_set_membership.py
Author: Shiqi Wang
Last date modified: 10/13/2020

The purpose of this program is to test function in_set
"""
import unittest
from more_fun_with_collections.set_membership import in_set


class TestSetMembership(unittest.TestCase):
    def setUp(self):
        self.s = {'a', 'b', 'c', 'd', 'e', 'f'}

    def test_in_set_true(self):
        self.assertTrue(in_set(self.s, 'f'))

    def test_in_set_false(self):
        self.assertFalse(in_set(self.s, 'g'))


if __name__ == '__main__':
    unittest.main()
