#!/usr/bin/python3
"""
Module that defines a function that multiplies 2 matrices
by using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    return np.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
