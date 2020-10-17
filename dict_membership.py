"""
Program: dict_membership.py
Author: Shiqi Wang
Last date modified: 10/13/2020

The purpose of this program is to write a function that decides if an element
is in the dictionary
"""


def in_dict(dic, item):
    """Return True if the item is in the dic
    :param dict dic: input dictionary
    :param item: input element
    :return: boolean
    """

    if not isinstance(dic, dict):
        raise ValueError("First input parameter is not a dict")

    return item in dic
