#!/usr/bin/python3
""" A function that finds the max integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_empty_list(self):
        """Test an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty), None)

    def test_two_numbers(self):
        """Tests if there are 2 of the same large number"""
        two_numbers = [1, 2, 3, 3]
        self.assertEqual(max_integer(two_numbers), 3)

    def test_negative(self):
        """Tests with negative numbers"""
        negative = [-2, -5, -9]
        self.assertEqual(max_integer(negative), -2)

    def test_max_start(self):
        """Tests for max at the start of the list"""
        max_start = [10, 7, 4, 9]
        self.assertEqual(max_integer(max_start), 10)

    def test_max_middle(self):
        """Tests for max in the middle"""
        max_middle = [9, 4, 10, 5, 1]
        self.assertEqual(max_integer(max_middle), 10)

    def test_max_end(self):
        """Tests for max at the end"""
        max_end = [10, 13, 89, 90]
        self.assertEqual(max_integer(max_end), 90)

    def test_same_number(self):
        """Test for all the same number"""
        same_number = [10, 10, 10, 10]
        self.assertEqual(max_integer(same_number), 10)

    def test_Strings(self):
        """Tests  strings"""
        Strings = ["hello", "true", "waffle", "bunny"]
        self.assertEqual(max_integer(Strings), "waffle")

    def test_string(self):
        """Tests a single string"""
        string = ["jeans"]
        self.assertEqual(max_integer(string), "jeans")

    def test_floats(self):
        """Tests for floats/decimals"""
        floats = [9.2, 7.8, 5.6, 2.3, 7.8]
        self.assertEqual(max_integer(floats), 9.2)

    def test_large_numbers(self):
        """"Tests for large numbers"""
        large_numbers = [829829, 5297407, 23707207091279, 923857238702]
        self.assertEqual(max_integer(large_numbers), 23707207091279)

    def test_ordered(self):
        """Tests for ordered lists"""
        ordered = [7, 8, 9, 10, 11]
        self.assertEqual(max_integer(ordered), 11)

    def test_unordered(self):
        """Tests  for unordered lists"""
        unordered = [8, 6, 2, 10, 290]
        self.assertEqual(max_integer(unordered), 290)


if __name__ == '__main__':
    unittest.main()
