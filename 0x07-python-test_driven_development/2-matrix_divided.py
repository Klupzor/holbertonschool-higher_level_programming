#!/usr/bin/python3
"""Divide a matrix
This script divide a matrix by a number

"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Parameters
    ----------
    matrix : Matrix
        List of lists of integers or floats
    div : int
        The int number to divide the matrix

    Raises
    ----------
    TypeError
        matrix must be a list of lists of integers or floats.
        Each row of the matrix must be of the same size.

    Returns
    ----------
    matrix
        A new matrix
    """
    ms = ["matrix must be a matrix (list of lists) of integers/floats",
            "Each row of the matrix must have the same size"]
    for li in matrix:
        if type(li) != list:
            raise TypeError(ms[0])
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError(ms[1])
        if not all(isinstance(i, (int, float)) for i in row): 
            raise TypeError(ms[0])

    return list(map(lambda array: list(map(lambda num:
                round(num / div, 2), array)), matrix))
