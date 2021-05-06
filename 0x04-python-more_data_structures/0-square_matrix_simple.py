#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return([list(map(lambda val: val * val, row)) for row in matrix])
