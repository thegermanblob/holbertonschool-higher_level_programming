#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print matrix"""
    if (matrix is None):
        return(None)
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            print ('{:d}'.format(matrix[row][val]), end="")
            if val != (len(matrix[row]) - 1):
                print("", end=" ")

        print("")
