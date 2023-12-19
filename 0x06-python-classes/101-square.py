# !/usr/bin/python3
"""Initialized Square class"""


class Square:
    """Square class with private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialized Square with size attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculation of square's area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square"""
        result = []
        if self.__size == 0:
            return ""
        else:
            for _ in range(self.__position[1]):
                result.append("")
            for _ in range(self.__size):
                result.append(" " * self.__position[0] + "#" * self.__size)
            return '\n'.join(result)
