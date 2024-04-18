#!/usr/bin/python3
"""Defines a class: Square"""


class Square:
    """Size of the square"""

    def __init__(self, size=0):
        """
        Initializes square with the given size.

        size (int): length of each side of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size *  self.__size)
