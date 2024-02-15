#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Arguments:
        matrix(int/float): list of lists
        div(int/float): element that the matrices are divided by

    Raises:
        TypeError: if the list is not ints or floats
        TypeError: if the matrices are not the same size
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is equal to 0
    """
    if type(matrix) is not list:
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for s in matrix:
        if type(s) is not list:
            raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(s)
        elif size != len(s):
            raise TypeError
            ("Each row of the matrix must have the same size")
        for p in s:
            if type(p) is not int and type(p) is not float:
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(p / div, 2) for p in s] for s in matrix]
