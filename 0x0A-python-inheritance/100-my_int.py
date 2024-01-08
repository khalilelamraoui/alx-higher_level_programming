#!/usr/bin/python3
"""
Module for MyInt class
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        eq method to invert the eq method
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        ne method to invert the ne method
        """
        return super().__eq__(other)
