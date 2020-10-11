"""
Program: sort_and_search_list.py
Author: Shiqi Wang
Last date modified: 10/05/2020

The purpose of this program is to sort and search list
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


def sort_list(number_list):
    """Sort list
    :param list number_list: input number list
    :return: None
    """
    # method sort() will not return a new list
    number_list.sort()


def search_list(number_list, item):
    """Return the index of item in the index or -1 if not found
    :param list number_list: input number list
    :param int item: the item wants to be found
    :return: index or -1
    """

    try:
        index = number_list.index(item)
    except ValueError:
        return -1
    else:
        return index


a = [2, 3, 1]
sort_list(a)
print(a)