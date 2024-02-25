#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base classs representing unique objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inititalize an object with a uniquie id

        Arguments:
            id (int): The identifier for the object.

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
