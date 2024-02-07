#!/usr/bin/python3

"""A class Square that defines a square"""


class Square:

    """
    Represents square shape

    __size (int): Length of each side of square
    """

    def __init__(self, size=0):
        """
        Initializes square with given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
