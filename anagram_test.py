"""
Program: anagram_test.py
Author: Shiqi Wang
Last date modified: 12/12/2020

The purpose of this program is to test methods from class anagram
"""
from main.Anagram import Anagram, EmptyFileError
import unittest


class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.anagram = Anagram()

    def tearDown(self):
        del self.anagram

    def test_read_non_exist_file(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.anagram.read_file("not_exist_file.txt")

    def test_read_empty_file(self):
        with self.assertRaises(EmptyFileError) as e:
            self.anagram.read_file("../main/empty.txt")

    def test_correct_file(self):
        self.anagram.read_file("../main/10000.txt")
        self.assertListEqual(self.anagram.data_dict['ceorsu'], ['course', 'source'])

    def test_find_word_not_in_the_dictionary(self):
        self.anagram.read_file("../main/10000.txt")
        self.assertIsNone(self.anagram.find_anagram_list("bbbbbb"))

    def test_find_word_list_only_itself(self):
        self.anagram.read_file("../main/10000.txt")
        # if the anagram list only has itself, then should return empty list
        self.assertListEqual(self.anagram.find_anagram_list("best"), [])

    def test_find_word_list_not_only_itself(self):
        self.anagram.read_file("../main/10000.txt")
        self.assertListEqual(self.anagram.find_anagram_list("course"), ["source"])

    def test_string_to_sorted_string(self):
        string = "course"
        self.assertEqual(self.anagram.string_to_sorted_string(string), "ceorsu")

    def test_preprocess_word_with_number(self):
        word = "happy26"
        with self.assertRaises(ValueError) as e:
            self.anagram.preprocess_word(word)

    def test_preprocess_word_with_two_words(self):
        word = "happy funny"
        with self.assertRaises(ValueError) as e:
            self.anagram.preprocess_word(word)

    def test_preprocess_word(self):
        word = "HAPPY "
        self.assertEqual(self.anagram.preprocess_word(word), "happy")


if __name__ == '__main__':
    unittest.main()
