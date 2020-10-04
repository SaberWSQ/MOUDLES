"""
Program: inner_functions_assignment.py
Author: Shiqi Wang
Last date modified: 10/01/2020

The purpose of this program is to write inner functions to calculate area and perimeter
"""


def area(a_list):
    """Return the area of the rectangle.

    :param list a_list: 2 elements as rectangle's edges
    :return: the area of the rectangle
    """
    return a_list[0] * a_list[1]


def perimeter(a_list):
    """Return the perimeter of the rectangle.

    :param list a_list: 2 elements as rectangle's edges
    :return: the perimeter of the rectangle
    """
    return (a_list[0] + a_list[1]) * 2


def measurements(a_list):
    """Return a string including the rectangle's area and perimeter

    :param list a_list: either 1 element(square) or 2 elements
    :return: a string about the rectangle's area and perimeter
    """
    if len(a_list) == 1:
        a_list.append(a_list[0])

    return f"Perimeter = {perimeter(a_list)} Area = {area(a_list)}"