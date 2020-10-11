"""
Program: test_sort_and_search_list.py
Author: Shiqi Wang
Last date modified: 10/05/2020



The purpose of this program is to test function sort_list and search_list
"""
import unittest
from main.sort_and_search_list import search_list, sort_list


class ListTest(unittest.TestCase):
    def setUp(self):
        self.initial_list = [2, 3, 1]
        self.expected = [1, 2, 3]

    def test_search_list(self):
        self.assertEqual(search_list(self.initial_list, 2), 0)
        self.assertEqual(search_list(self.initial_list, 10), -1)

    def test_sort_list(self):
        sort_list(self.initial_list)
        self.assertListEqual(self.initial_list, self.expected)


if __name__ == '__main__':
    unittest.main()
