#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix is None):
        return(None)
    for row in matrix:
        for val in row:
            print ('{:d}'.format(val), end="")
            if (val % 3 != 0):
                print("", end=" ")
                
        print("")
