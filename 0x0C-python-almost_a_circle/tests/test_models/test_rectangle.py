#!/usr/bin/python3
"""
test_rectangle Module
This module tests the Rectangle Class defined in
the `models.rectangle` module
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """subclass of TestCase class in unittest
    module used to test the Rectangle class"""
    def test_if_subclass(self):
        """Tests that Rectangle is a subclass of
        Base"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(issubclass(type(r1), Base))
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_init(self):
        """Tests that an instance of Rectangle is created with
        the given id, width, height, x, and y"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 12)

    def test_init_no_args(self):
        """Tests that an error is raised when creating
        an instance without arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_unassigned_x_or_y(self):
        """Tests that an instance of Rectangle that is
        created with x or y not assigned gets its
        default values"""
        r2 = Rectangle(5, 4, 0, 0, 1)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

    def test_raises_value_error(self):
        """Tests that bad inputs for Rectangle instance
        raise a ValueError"""
        r2 = Rectangle(5, 4)
        with self.assertRaises(ValueError):
            r2.width = -10
        with self.assertRaises(ValueError):
            r2.height = 0
        with self.assertRaises(ValueError):
            r2.x = -10
        with self.assertRaises(ValueError):
            r2.y = -1
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 2, 3, -1)

    def test_raises_type_error(self):
        """Tests that bad inputs for Rectangle instance
        raise a TypeError"""
        r2 = Rectangle(5, 4)
        with self.assertRaises(TypeError):
            r2.width = (2,)
        with self.assertRaises(TypeError):
            r2.height = [5]
        with self.assertRaises(TypeError):
            r2.x = "10"
        with self.assertRaises(TypeError):
            r2.y = None
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "2", 3, 4)

    def test_area(self):
        """Tests that the right area is computed
        for the given width and height of the
        rectangle"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 4)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 24)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """Tests that __str__ method has been
        properly overwritten"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args1(self):
        """Tests that instance attributes are updated with args"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_kwargs(self):
        """Tests that instance attributes are updated with kwargs
        if args is not present"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args2(self):
        """Tests that instance attributes are updated with only
        args even if kwargs are present"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_bad_input(self):
        """Tests that errors are raised when update is
        called with wrong input"""
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(width="1", x=2)
        with self.assertRaises(TypeError):
            r1.update(89, [2])
        with self.assertRaises(TypeError):
            r1.update(89, (2,), 3)
        with self.assertRaises(ValueError):
            r1.update(89, -2, 3)
        with self.assertRaises(ValueError):
            r1.update(89, 2, 0)

    def test_update_no_args(self):
        """Tests that an error is raised when update is
        called without arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

    def test_to_dictionary(self):
        """Tests that to_dictionary() returns desired output"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                         'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)

    def test_to_dictionary_with_update(self):
        """Tests that output of to_dictionary()
        can be used to update another instance"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertFalse(r1 == r2)

    def test_to_json_string(self):
        """Tests that output of to_json_string is as desired"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1,
                                      'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_none(self):
        """Tests that output of to_json_string when input is
        None is a string of an empty list"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_empty(self):
        """Tests that output of to_json_string when input is
        an empty list is a string of an empty list"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_list_with_none(self):
        """Tests that to_json_string ignores None in a
        list"""
        json_dictionary = Base.to_json_string([None])
        self.assertEqual(json_dictionary, "[null]")

    def test_to_json_string_list_with_empty(self):
        """Tests that to_json_string ignores an empty dictionary
        in a list"""
        json_dictionary = Base.to_json_string([{}])
        self.assertEqual(json_dictionary, "[{}]")

    def test_save_to_file_normal(self):
        """Tests that file was created and contains json string"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            string = file.read()
        self.assertEqual(type(string), str)

    def test_save_to_file_none(self):
        """Tests that file was created and contains empty list
        string if input is None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            string = file.read()
        self.assertEqual(string, "[]")

    def test_from_json_string(self):
        """Tests that output of from_json_string is as desired"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_none(self):
        """Tests that output of to_json_string when input is
        None is a string of an empty list"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Tests that output of to_json_string when input is
        an empty list is a string of an empty list"""
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

    def test_create(self):
        """Tests that create works"""
        r1 = Rectangle(3, 5, 1, id=1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 == r2)

    def test_create_none(self):
        """Tests that create raises error if None or empty"""
        dictionary1 = None
        dictionary2 = {}
        with self.assertRaises(TypeError):
            r1 = Rectangle.create(**dictionary1)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**dictionary2)

    def test_load_from_file_normal(self):
        """Tests that list was created and contains instances"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(), "[Rectangle] (1)\
 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(), "[Rectangle] (2)\
 0/0 - 2/4")

    def test_load_from_file_csv_normal(self):
        """Tests that list was created and contains instances"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output[0].__str__(), "[Rectangle] (1)\
 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(), "[Rectangle] (2)\
 0/0 - 2/4")


if __name__ == "__main__":
    unittest.main()
