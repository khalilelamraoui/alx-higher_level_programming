#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.
        Args:
            width(int): width of rectangle, defaults to 0
            height(int): height of rectangle, defaults to 0
        """
        self.height = height
        self.width = width


    @property
    def width(self):
        """Method to get value of width
        Return:
            value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width
        Args:
            value(int): value to set width to
        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """Method to get value of height
        Return:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of height
        Args:
            value(int): value to set height to
        Raises:
            TypeError: if height is not an int
            ValueError: if height is < 0
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value
