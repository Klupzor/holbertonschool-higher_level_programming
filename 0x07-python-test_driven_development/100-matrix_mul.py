#!/usr/bin/python3
"""Divide a matrix
This script divide a matrix by a number

"""


def matrix_mul(m_a, m_b):
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
    ms = ["m_a should contain only integers or floats",
          "m_b should contain only integers or floats",
          "each row of m_a must should be of the same size",
          "each row of m_b must should be of the same size"]
    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")

    for ali in m_a:
        if type(ali) != list:
            raise TypeError("m_a must be a list of lists")
        if len(ali) == 0:
            raise TypeError("m_a can't be empty")
        for n in ali:
            if not type(n) == int or type(n) == float:
                raise TypeError(ms[0])
        if not len(ali) == len(m_a[0]):
            raise TypeError(ms[2])

    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    for bli in m_b:
        if type(bli) != list:
            raise TypeError("m_b must be a list of lists")
        if len(bli) == 0 or len(m_b) == 0:
            raise TypeError("m_b can't be empty")
        for n in bli:
            if not type(n) == int or type(n) == float:
                raise TypeError(ms[1])
        if not len(bli) == len(m_b[0]):
            raise TypeError(ms[3])

    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matx = []
    for arow in m_a:
        li = []
        i = 0
        while i < len(m_b[0]):
            value = 0
            c = 0
            for brow in m_b:
                value = value + (arow[c] * brow[i])
                c += 1
            li.append(value)
            i += 1
        matx.append(li)
    return matx
