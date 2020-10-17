"""
Program: assign_average.py
Author: Shiqi Wang
Last date modified: 10/13/2020


The purpose of this program is to write a function to switch the average
"""


# The instruction doesn't explain what the parameters are and what the function returns
def switch_average(key):
    """Return dic[key] if the key is valid, otherwise raise
    ValueError
    :param string key: key
    :return:
    """
    dic = {'a': 90, 'b': 95, 'c': 98, 'd': 90}
    key = key.lower()
    if key not in dic:
        raise ValueError("The key is not valid.")

    return dic[key]
