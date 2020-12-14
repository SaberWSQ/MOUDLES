"""
Program: Anagram.py
Author: Shiqi Wang
Last date modified: 12/12/2020

The purpose of this program is to write a Anagram class to read data and provide
searching anagram methods
"""

import os


class Anagram:
    def __init__(self):
        """Initialize the class Anagram with setting filename to None
        and data_dict to be an empty dictionary
        """
        self.filename = None
        self.data_dict = {}

    def read_file(self, filename):
        """Read data from the given filename and assign data_dict values
        :param str filename: input filename
        :return: None
        """
        self.filename = filename
        # filename is None
        if self.filename is None:
            raise FileNotFoundError(f"File name should not be empty.")

        # check if the file is exist or not
        try:
            f = open(self.filename, 'r')
        except IOError:
            # use build-in Error
            raise FileNotFoundError(f"{self.filename} not found, please try again!")
        else:
            f.close()

        # second check if the file is empty
        if os.stat(self.filename).st_size == 0:
            # use own created Error
            raise EmptyFileError(self.filename, message="File is empty, please try again!")

        # open file and preprocess
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                sorted_line = self.string_to_sorted_string(line)
                if sorted_line not in self.data_dict:
                    self.data_dict[sorted_line] = [line]
                else:
                    self.data_dict[sorted_line].append(line)

    @staticmethod
    def preprocess_word(word):
        """preprocess the word and check if the word is in correct format
        :param str word: input word
        :return: str
        """
        word = word.strip()
        # not an alphabet word
        if not word.isalpha():
            raise ValueError(f"The word '{word}' is not a correct single word")
        return word.lower()

    def find_anagram_list(self, word):
        """Find the corresponding anagram list. If the given word not in the dictionary,
        return None. If the return value is the word itself, return empty list, otherwise
        return the rest of the anagram words list.
        :param str word: input word
        :return: None or list
        """
        sorted_word = self.string_to_sorted_string(word)
        # not in the dictionary
        if sorted_word not in self.data_dict:
            return None

        # sorted_word in the dictionary key, remove it from the value list
        res = self.data_dict[sorted_word][:]
        try:
            res.remove(word)
        except ValueError:
            # do nothing
            pass
        return res

    @staticmethod
    def string_to_sorted_string(string):
        """Sort a string by alphabet
        :param str string: input word
        :return: str
        """
        return ''.join(sorted(string))


class EmptyFileError(Exception):
    """Raised when the file is empty"""
    def __init__(self, *args, **kwargs):
        self.filename = args[0]
        self.message = kwargs["message"]
        super().__init__(self.message)

    def __str__(self):
        return f"{self.filename}: {self.message}"
