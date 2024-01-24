#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    total_matrix = []

    for row in matrix:
        squared_row = [x**2 if isinstance(x, int) else x for x in row]
        total_matrix.append(squared_row)

    return total_matrix
