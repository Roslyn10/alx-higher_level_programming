#!/usr/bin/python3
"""Defines a function that adds integers"""


def add_integer(a=56, b=98):
    """Returns the addition of two number 
    raises:
        TypeError if a and b is not float or int 
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer") 
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b) 
    return a + b 
