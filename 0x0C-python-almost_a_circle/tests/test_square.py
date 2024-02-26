#!/usr/bin/python3
"""Unittests for module Square"""

import unittest
from models.square import Square

class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""
    def test_constructor(self):
        with self.assertRaises(TypeError):
            Square("a")
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1)2/3 - 5")

    def test_size_property(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(TypeError):
            s.size = "a"
        with self.assertRaises(ValueError):
            s.size = -5

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(5, 10, 4, 5)
        self.assertEqual(str(s), "[Square] (5)4/5 - 10")
        s.update(6)
        self.assertEqual(str(s), "[Square] (6)4/5 - 10")
        s.update(6, 20)
        self.assertEqual(str(s), "[Square] (6)4/5 - 20")
        s.update(6, 20, 7)
        self.assertEqual(str(s), "[Square] (6)7/5 - 20")
        s.update(6, 20, 7, 8)
        self.assertEqual(str(s), "[Square] (6)7/8 - 20")
        s.update(x=1, y=2, size=3, id=7)
        self.assertEqual(str(s), "[Square] (7)1/2 - 3")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 3)
        self.assertEqual(s.to_dictionary(), {'id': 3, 'size': 10, 'x': 2, 'y': 1})


if __name__ == '__main__':
    unittest.main()
