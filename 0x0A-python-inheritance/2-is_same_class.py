#!/usr/bin/python3
"""Defines a function that checks classes"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specific class

    Arguments: 
        obj: An object that is a specific class
        a_class: The class to match the object to

    Returns: 
        True if the object is exactly a specified class
        False if otherwise
     """

    if type(obj) == a_class:
        return True
    return False 
