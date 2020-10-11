"""
Program: test_basic.py
Author: Shiqi Wang
Last date modified: 10/05/2020



The purpose of this program is to test function make_list
"""
import unittest
from unittest.mock import patch
from fun_with_collections import basic_list

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='2')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [2, 2, 2])


if __name__ == '__main__':
    unittest.main()
