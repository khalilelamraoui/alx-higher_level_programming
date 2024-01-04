#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    @property
    def width(self):
        """Method to get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """Method to get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.height = height
        self.width = width
