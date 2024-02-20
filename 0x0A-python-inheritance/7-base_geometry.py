#!/usr/bin/python3
"""defines a class: BaseGeometry"""


class BaseGeometry:
    """Represents a base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates an integer

        Arguments:
            value(int): The validator of the parameter
            name(str): The name of the parameter

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
