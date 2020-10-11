"""
Program: basic_list.py
Author: Shiqi Wang
Last date modified: 10/05/2020

The purpose of this program is to make a list from user input
"""


def get_input():
    """Prompt to get user input, and return the string

    :return: user input
    """
    string = input("Please input a number")
    return string


def make_list():
    """Call 3 times function get_input() and make the return values
    into list. Then return the list

    :return: list including three user input numbers
    """
    res = []
    for i in range(3):
        try:
            number = float(get_input())
        except ValueError:
            raise ValueError("Then input string is not a valid number")
        else:
            res.append(number)

    return res
