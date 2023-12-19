#!/usr/bin/python3
"""Initialized Square class"""


class Square:
    """Square class with private attribute"""
    def __init__(self, size=0):
        """Initialized Square with size attribute"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculation of square's area"""
        area = self.__size ** 2
        return area
