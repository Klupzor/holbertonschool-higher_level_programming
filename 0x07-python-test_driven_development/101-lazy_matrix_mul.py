#!/usr/bin/python3
"""Divide a matrix
This script divide a matrix by a number

"""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
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
    return npy.matmul(m_a, m_b)
