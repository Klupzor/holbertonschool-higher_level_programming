#!/usr/bin/python3
"""Print square
This script  prints a square
"""


def print_square(size):
    """Function that prints a square with the character #

    Parameters
    ----------
    size : int
        The size length of the square

    Raises
    ----------
    TypeError
        size must be a integer and > 0

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
