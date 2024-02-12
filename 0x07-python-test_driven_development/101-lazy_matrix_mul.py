#!/usr/bin/python3
"""A function that multiplies 2 matrices by using NumPy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Returns the multiplication of 2 matrices

    Arguments:
        m_a (list of ints/floats): the first matrix
        m_b (list of ints/floats): the second matrix
    """    

    return (np.matmul(m_a, m_b))
