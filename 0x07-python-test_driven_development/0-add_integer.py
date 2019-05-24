#!/usr/bin/python3
"""Add Integer

This script add two int numbers

"""


def add_integer(a, b=98):

    """ Function that adds 2 integers.

    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number

    Raises
    ----------
    TypeError
        a and b must be int or float

    Returns
    ----------
    Integer
        a + b
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
