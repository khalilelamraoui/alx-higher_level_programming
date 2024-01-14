#!/usr/bin/python3
"""
Module that contains base class
"""
import json
import os
import csv
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method
        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string method
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            json string representation of list_dictionaries
        """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file method
        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string method
        Args:
            json_string (str): json string
        Returns:
            list of dictionaries
        """
        import json

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """
        create method
        Args:
            dictionary (dict): dictionary of arguments
        Returns:
            instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)

        new.update(**dictionary)
        return new
    
    @classmethod
    def load_from_file(cls):
        """
        load_from_file method
        Returns:
            list of instances
        """
        filename = cls.__name__ + ".json"
        list_dicts = []

        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except:
            pass

        return [cls.create(**obj) for obj in list_dicts]
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv method
        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    f.write("{},{},{},{},{}\n".format(obj.id, obj.width,
                                                      obj.height, obj.x,
                                                      obj.y))
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    f.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x,
                                                   obj.y))
                    
    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv method
        Returns:
            list of instances
        """
        filename = cls.__name__ + ".csv"
        list_dicts = []

        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    for line in f:
                        line = line.split(",")
                        list_dicts.append({"id": int(line[0]),
                                           "width": int(line[1]),
                                           "height": int(line[2]),
                                           "x": int(line[3]),
                                           "y": int(line[4])})
                elif cls.__name__ == "Square":
                    for line in f:
                        line = line.split(",")
                        list_dicts.append({"id": int(line[0]),
                                           "size": int(line[1]),
                                           "x": int(line[2]),
                                           "y": int(line[3])})
        except:
            pass

        return [cls.create(**obj) for obj in list_dicts]
    
    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles:
            list_squares:
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
