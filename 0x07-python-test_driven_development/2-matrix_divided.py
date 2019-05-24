#!/usr/bin/python3


def matrix_divided(matrix, div):
    r = 0

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
            if not len(row) == len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            if not all(isinstance(i, (int, float)) for i in row):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return list(map(lambda array: list(map(lambda num: round(num / div, 2), array)) , matrix))
