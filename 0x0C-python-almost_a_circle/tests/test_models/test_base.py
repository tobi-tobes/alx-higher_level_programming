#!/usr/bin/python3
"""
test_base Module
This module tests the Base Class defined in
the `models.base` module
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """subclass of TestCase class in unittest
    module used to test the Base class"""
    def test_creation(self):
        """Tests that an instance of Base is created with
        the given id"""
        b1 = Base(12)
        b2 = Base(23)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 23)

    def test_none(self):
        """Tests that an instance of Base that is
        created with an id on None gets its id from
        __nb_objects"""
        b3 = Base()
        b4 = Base()
        b5 = Base(5)
        b6 = Base()
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b5.id, 5)
        self.assertEqual(b6.id, 3)


if __name__ == "__main__":
    unittest.main()
