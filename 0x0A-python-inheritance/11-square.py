#!/usr/bin/python3
"""
Module for Square class
that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        init method to initialize the Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area method to calculate the area of the Square
        """
        return self.__size ** 2

    def __str__(self):
        """
        str method to print the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
