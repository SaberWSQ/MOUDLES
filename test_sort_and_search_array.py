"""
Program: test_sort_and_search_array.py
Author: Shiqi Wang
Last date modified: 10/05/2020

The purpose of this program is to test function sort_array and search_array
"""
import unittest
from main.sort_and_search_array import search_array, sort_array
import array as arr


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.initial_array = arr.array('d', [2.2, 3.2, 1.2])
        self.expected = arr.array('d', [1.2, 2.2, 3.2])

    def test_search_array(self):
        self.assertEqual(search_array(self.initial_array, 1.2), 2)
        self.assertEqual(search_array(self.initial_array, 12), -1)

    def test_sort_array(self):
        self.assertEqual(sort_array(self.initial_array), self.expected)


if __name__ == '__main__':
    unittest.main()
