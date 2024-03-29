#!/usr/bin/python3
"""
This Module uses the function matrix divided to divide the contents of
a matrix with multiple list of the same size by a divisor
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div"""
    if not(matrix or isinstance(matrix, list)):
        TypeError("matrix must be a matrix (list of lists)"
                  " of integers/floats")
    if not all(len(sub_list) == len(matrix[0]) for sub_list in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for x in matrix:
        if len(x) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in lists] for lists in matrix]
