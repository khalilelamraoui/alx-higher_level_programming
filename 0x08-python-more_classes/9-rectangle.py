#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """ returns set of rectangle """
        empty = ''
        if self.__height == 0 or self.__width == 0:
            return empty
        for i in range(self.__height):
            for j in range(self.__width):
                empty += str(self.print_symbol)
            empty += '\n'
        return empty[:-1]

    def print(self):
        """Method that prints rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for i in range(self.__height):
                print(self.print_symbol * self.__width)

    def __repr__(self):
        """Method that returns rectangle with eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method that prints message when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Method that returns biggest rectangle based on area"""
        if isinstance(rect_1, Rectangle) == 0:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) == 0:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new Rectangle instance with size"""
        return cls(size, size)
