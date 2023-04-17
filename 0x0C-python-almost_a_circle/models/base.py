#!/usr/bin/python3
"""
Base Class
This module contains the definition of the
Base Class, which is the parent class of all
the classes in this project and manages the id
attribute for the child classes.
"""


import json
import os
import csv
import turtle


class Base(object):
    """defines the Base "base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates an instance of the Bass class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        list_to_save = []
        if list_objs is not None:
            if len(list_objs) != 0:
                for objs in list_objs:
                    if objs is not None:
                        to_dict = objs.to_dictionary()
                        list_to_save.append(to_dict)
                    else:
                        continue
        json_dict = cls.to_json_string(list_to_save)
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(json_dict)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary is None:
            raise TypeError("dictionary must be a dictionary")
        elif len(dictionary) == 0:
            raise TypeError("dictionary xannot be empty")
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_to_return = []
        filename = f"{cls.__name__}.json"
        if os.path.isfile(filename) is False:
            return list_to_return
        with open(filename, "r", encoding="utf-8") as f:
            json_string = f.read()
        obj_list = cls.from_json_string(json_string)
        if obj_list is None:
            return list_to_return
        for obj in obj_list:
            if obj is not None:
                new_instance = cls.create(**obj)
                list_to_return.append(new_instance)
            else:
                continue
        return list_to_return

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes list_objs to a CSV file"""
        list_to_save = []
        if list_objs is not None and len(list_objs) != 0:
            for objs in list_objs:
                if objs is not None:
                    to_dict = objs.to_dictionary()
                    list_to_save.append(to_dict)
                else:
                    continue
        with open(f"{cls.__name__}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for item in list_to_save:
                if cls.__name__ == "Rectangle":
                    writer.writerow([item["id"], item["width"],
                                     item["height"], item["x"], item["y"]])
                elif cls.__name__ == "Square":
                    writer.writerow([item["id"], item["size"],
                                     item["x"], item["y"]])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes list_objs from a CSV file"""
        list_to_return = []
        dictionary = {}
        filename = f"{cls.__name__}.csv"
        if os.path.isfile(filename) is False:
            return list_to_return
        with open(filename, "r") as f:
            reader = csv.reader(f)
            if reader is None:
                return list_to_return
            for line in reader:
                if cls.__name__ == "Rectangle":
                    dictionary["id"] = int(line[0])
                    dictionary["width"] = int(line[1])
                    dictionary["height"] = int(line[2])
                    dictionary["x"] = int(line[3])
                    dictionary["y"] = int(line[4])
                elif cls.__name__ == "Square":
                    dictionary["id"] = int(line[0])
                    dictionary["size"] = int(line[1])
                    dictionary["x"] = int(line[2])
                    dictionary["y"] = int(line[3])
                new_instance = cls.create(**dictionary)
                list_to_return.append(new_instance)
        return list_to_return

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        s = turtle.getscreen
        t = turtle.Turtle()
        t.fillcolor("purple")
        t.shape("turtle")
        t.pencolor("purple")
        t.pensize(5)
        t.speed(1)
        if list_rectangles is not None or len(list_rectangles) != 0:
            for rect in list_rectangles:
                t.penup()
                t.goto(rect.x, rect.y)
                t.pendown()
                t.fd(rect.width)
                t.rt(90)
                t.fd(rect.height)
                t.rt(90)
                t.fd(rect.width)
                t.rt(90)
                t.fd(rect.height)
        if list_squares is not None or len(list_squares) != 0:
            for squares in list_squares:
                t.penup()
                t.goto(squares.x, squares.y)
                t.pendown()
                t.fd(squares.width)
                t.rt(90)
                t.fd(squares.height)
                t.rt(90)
                t.fd(squares.width)
                t.rt(90)
                t.fd(squares.height)
        turtle.exitonclick()
