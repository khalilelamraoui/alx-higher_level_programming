#!/usr/bin/python3
"""
Module that contains Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init method
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coord of rectangle
            y (int): y coord of rectangle
            id (int): id of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width getter and setter
    @property
    def width(self):
        """
        width getter
        Returns:
            width (int): width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value (int): value to set width to
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    # height getter and setter
    @property
    def height(self):
        """
        height getter
        Returns:
            height (int): height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value (int): value to set height to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # x getter and setter
    @property
    def x(self):
        """
        x getter
        Returns:
            x (int): x coord of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        Args:
            value (int): value to set x to
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # y getter and setter
    @property
    def y(self):
        """
        y getter
        Returns:
            y (int): y coord of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        Args:
            value (int): value to set y to
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        area method
        Returns:
            area (int): area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        display method
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        str method
        Returns:
            string representation of rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        update method
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of arguments
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionary method
        Returns:
            dictionary representation of rectangle
        """
        attrs = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attrs}

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string method
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            json representation of list_dictionaries
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
        import json
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
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
        if (cls.__name__ + ".json") is None:
            return []
        with open(cls.__name__ + ".json", "r") as f:
            list_dicts = cls.from_json_string(f.read())

        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv method
        Args:
            list_objs (list): list of objects
        """
        import csv
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".csv", "w") as f:
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=attrs)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv method
        Returns:
            list of instances
        """
        import csv
        if (cls.__name__ + ".csv") is None:
            return []
        with open(cls.__name__ + ".csv", "r") as f:
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            reader = csv.DictReader(f, fieldnames=attrs)
            list_dicts = [dict([key, int(value)] for key, value in d.items())
                          for d in reader]

        return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw method
        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        """
        import turtle
        import random
        import time
        turtle.bgcolor("black")
        turtle.pensize(3)
        turtle.speed(0)
        turtle.hideturtle()
        turtle.up()
        turtle.setpos(-200, 200)
        turtle.down()
        turtle.color("white")
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
