#!/usr/bin/python3
"""Defines a function that checks the class and inheritance of an object"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    from a specified class, otherwise False

    Arguments:
        obj: An object that is a specific class
        a_class: The class to match the object to

    Returns:
        True: if the object matches the class
        False: If otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
