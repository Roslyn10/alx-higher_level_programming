#!/usr/bin/python3
"""Defines Class: MyList"""


class MyList(list):
    """Implements a sorted list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
