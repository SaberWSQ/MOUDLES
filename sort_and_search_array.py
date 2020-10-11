"""
Program: sort_and_search_array.py
Author: Shiqi Wang
Last date modified: 10/05/2020

The purpose of this program is to make a list from user input
"""

import array as arr


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


def sort_array(array):
    """Return sorted array
    :param array: input array
    :return: new sorted array
    """
    res = arr.array('d', [])
    temp = array.tolist()
    temp.sort()
    res.fromlist(temp)
    return res


def search_array(array, item):
    """Return the index of item in the index or -1 if not found
    :param array: input number array
    :param item: the item wants to be found
    :return: index or -1
    """
    try:
        return array.index(item)
    except ValueError:
        return -1


def main():
    array = arr.array('d', [])
    array.fromlist(make_list())
    print(sort_array(array))
    print(search_array(array, 1))


if __name__ == '__main__':
    main()
