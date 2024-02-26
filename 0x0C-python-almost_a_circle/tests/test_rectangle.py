#!/usr/bin/python3
"""Defines a tests for rectangle.py"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 5)
        with self.assertRaises(TypeError):
            Rectangle(5, "a")
        with self.assertRaises(TypeError):
            Rectangle(5, 5, "a")
        with self.assertRaises(TypeError):
            Rectangle(5, 5, 1, "a")
        with self.assertRaises(ValueError):
            Rectangle(-5, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, -5)
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -1)
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 1, -1)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)


    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})


if __name__ == '__main__':
    unittest.main()
