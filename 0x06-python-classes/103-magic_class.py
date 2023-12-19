#!/usr/bin/python3
"""Initialized MagicClass class"""
import math


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius=0):
        """Initialized MagicClass with radius attribute"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculation of MagicClass's area"""
        area = self.__radius ** 2 * math.pi
        return area

    def circumference(self):
        """Calculation of MagicClass's circumference"""
        circumference = 2 * math.pi * self.__radius
        return circumference
