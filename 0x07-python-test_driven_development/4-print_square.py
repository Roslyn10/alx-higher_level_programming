#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """
    Returns a square made from the # character

    Arguments:
        size (int): height and width of the square

    Raises:
        TypeError: If size is a float and not an int
        ValueError: If size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
