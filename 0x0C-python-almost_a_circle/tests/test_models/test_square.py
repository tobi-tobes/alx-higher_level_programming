#!/usr/bin/python3
"""
test_square Module
This module tests the Square Class defined in
the `models.square` module
"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """subclass of TestCase class in unittest
    module used to test the Square class"""
    def test_if_subclass(self):
        """Tests that Square is a subclass of
        Rectangle"""
        s1 = Square(4, 2, 1, 12)
        self.assertTrue(issubclass(type(s1), Rectangle))
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s1, Rectangle)

    def test_init(self):
        """Tests that an instance of Square is created with
        the given id, width, height, x, and y"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 12)

    def test_init_no_args(self):
        """Tests that an error is raised when creating
        an instance without arguments"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_unassigned_x_or_y(self):
        """Tests that an instance of Square that is
        created with x or y not assigned gets its
        default values"""
        s2 = Square(5, id=11)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 11)

    def test_raises_value_error(self):
        """Tests that bad inputs for Square instance
        raise a ValueError"""
        s2 = Square(5)
        with self.assertRaises(ValueError):
            s2.size = -10
        with self.assertRaises(ValueError):
            s2.size = 0
        with self.assertRaises(ValueError):
            s2.x = -10
        with self.assertRaises(ValueError):
            s2.y = -1
        with self.assertRaises(ValueError):
            s4 = Square(10, 3, -1)

    def test_raises_type_error(self):
        """Tests that bad inputs for Square instance
        raise a TypeError"""
        s2 = Square(5)
        with self.assertRaises(TypeError):
            s2.size = (2,)
        with self.assertRaises(TypeError):
            s2.size = [5]
        with self.assertRaises(TypeError):
            s2.x = "10"
        with self.assertRaises(TypeError):
            s2.y = None
        with self.assertRaises(TypeError):
            s4 = Square(10, "2", 3)

    def test_area(self):
        """Tests that the right area is computed
        for the given width and height of the
        Square"""
        s1 = Square(6, 2, 1, 12)
        s2 = Square(5)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s1.area(), 36)
        self.assertEqual(s2.area(), 25)
        self.assertEqual(s3.area(), 64)

    def test_str(self):
        """Tests that __str__ method has been
        properly overwritten"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")

    def test_update_args1(self):
        """Tests that instance attributes are updated with args"""
        s1 = Square(5, id=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

    def test_update_kwargs(self):
        """Tests that instance attributes are updated with kwargs
        if args is not present"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
        s1.update(size=1)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 1")
        s1.update(x=2)
        self.assertEqual(s1.__str__(), "[Square] (10) 2/10 - 1")
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/1 - 2")

    def test_update_args2(self):
        """Tests that instance attributes are updated with only
        args even if kwargs are present"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
        s1.update(89, 2, 3, height=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/10 - 2")

    def test_update_bad_input(self):
        """Tests that errors are raised when update is
        called with wrong input"""
        s1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s1.update(size="1", x=2)
        with self.assertRaises(TypeError):
            s1.update(89, [2])
        with self.assertRaises(TypeError):
            s1.update(89, (2,), 3)
        with self.assertRaises(ValueError):
            s1.update(89, -2, 3)
        with self.assertRaises(ValueError):
            s1.update(89, 0, 0)

    def test_update_no_args(self):
        """Tests that update does nothing when called without arguments"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")

    def test_to_dictionary(self):
        """Tests that to_dictionary() returns desired output"""
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)

    def test_to_dictionary_with_update(self):
        """Tests that output of to_dictionary()
        can be used to update another instance"""
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s2.__str__(), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)

    def test_to_json_string(self):
        """Tests that output of to_json_string is as desired"""
        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 7, 'size': 10, 'id': 8, 'y': 2})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file_normal(self):
        """Tests that file was created and contains json string"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            string = file.read()
        self.assertEqual(type(string), str)

    def test_save_to_file_none(self):
        """Tests that file was created and contains empty list
        string if input is None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            string = file.read()
        self.assertEqual(string, "[]")

    def test_from_json_string(self):
        """Tests that output of from_json_string is as desired"""
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'size': 10, 'id': 89},
                                       {'size': 7, 'id': 7}])
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_none(self):
        """Tests that output of to_json_string when input is
        None is a string of an empty list"""
        list_output = Square.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Tests that output of to_json_string when input is
        an empty list is a string of an empty list"""
        list_output = Square.from_json_string("")
        self.assertEqual(list_output, [])

    def test_create(self):
        """Tests that create works"""
        s1 = Square(3, 5, 1, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), "[Square] (1) 5/1 - 3")
        self.assertEqual(s2.__str__(), "[Square] (1) 5/1 - 3")
        self.assertFalse(s1 == s2)

    def test_create_none(self):
        """Tests that create raises error if None or empty"""
        dictionary1 = None
        dictionary2 = {}
        with self.assertRaises(TypeError):
            s1 = Square.create(**dictionary1)
        with self.assertRaises(TypeError):
            s2 = Square.create(**dictionary2)

    def test_load_from_file_normal(self):
        """Tests that list was created and contains instances"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, id=1)
        list_Squares_input = [s1, s2]
        Square.save_to_file(list_Squares_input)
        list_Squares_output = Square.load_from_file()
        self.assertEqual(list_Squares_output[0].__str__(), "[Square] (8) 7/2\
 - 10")
        self.assertEqual(list_Squares_output[1].__str__(), "[Square] (1) 4/0\
 - 2")

    def test_load_from_file_csv_normal(self):
        """Tests that list was created and contains instances"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, id=1)
        list_Squares_input = [s1, s2]
        Square.save_to_file_csv(list_Squares_input)
        list_Squares_output = Square.load_from_file_csv()
        self.assertEqual(list_Squares_output[0].__str__(), "[Square] (8) 7/2\
 - 10")
        self.assertEqual(list_Squares_output[1].__str__(), "[Square] (1) 4/0\
 - 2")


if __name__ == "__main__":
    unittest.main()
