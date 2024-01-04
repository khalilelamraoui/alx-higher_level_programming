#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Method to get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >=0")
        else:
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
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Method that returns string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width) + "\n") * self.__height
