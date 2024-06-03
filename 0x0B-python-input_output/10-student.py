#!/usr/bin/python3
"""Defines a class; Student; that defines a student"""


class Student:
    """
    Attributes
    first_name(str): first name of the student
    last_name(str): last name of the student
    age(int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of the student"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                    key: value for key,
                    value in self.__dict__.items() if key in attrs
                    }
