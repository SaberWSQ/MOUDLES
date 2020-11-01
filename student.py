"""
Program: student.py
Author: Shiqi Wang
Last date modified: 10/26/2020

The purpose of this program is to create student class
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")

        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not major_characters.issuperset(major):
            raise ValueError
        if not (isinstance(gpa, float) and 0.0 <= gpa <= 4.0):
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
