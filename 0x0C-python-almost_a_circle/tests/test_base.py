#!/usr/bin/python3
"""Define tests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), "[]")
        self.assertEqual(Base.from_json_string(""), "[]")
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_create(self):
        dictionary = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)


if __name__ == '__main__':
    unittest.main()
