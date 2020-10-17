"""
Program: test_dict_membership.py
Author: Shiqi Wang
Last date modified: 10/13/2020

The purpose of this program is to test function in_dict
"""
import unittest
from more_fun_with_collections.dict_membership import in_dict



class TestDictMembership(unittest.TestCase):
    def setUp(self):
        self.dic = {'a': 1, 'b': 2}

    def test_in_dict_true(self):
        self.assertTrue(in_dict(self.dic, 'b'))

    def test_in_dict_false(self):
        self.assertFalse(in_dict(self.dic, 'c'))


if __name__ == '__main__':
    unittest.main()
