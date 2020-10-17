"""
Program: set_membership.py
Author: Shiqi Wang
Last date modified: 10/13/2020

The purpose of this program is to write a function that decides if an element
is in the set
"""


def in_set(s, item):
    """Return True if the item is in the set
    :param set s: input set
    :param item: input element
    :return: boolean
    """
    if not isinstance(s, set):
        raise ValueError("First input parameter is not a set")

    return item in s

