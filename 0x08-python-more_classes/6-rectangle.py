#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Represents a rectangle shape

        width(int): the width of the rectangle

            Raises:
                TypeError: if width is not an int
                ValueError: if width is less than 0

        height(int): height of the rectangle

            Raises:
                TypeError: if height is not an int
                ValueError: if height is less than 0
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """allows the rectangle to be displayed using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for m in range(self.__height):
            [rec.append('#') for n in range(self.__width)]
            if m != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self_):
        """Prints a message when the rectangle is deleted"""
        print("Bye rectangle...")
