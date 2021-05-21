#!/usr/bin/python3
""" Module that contains the matrix divider """


def matrix_divided(matrix, div):
    """ function that divides a matrix by a number

    Args:
        matrix (list): A list of lists of numbers
        div (int/float): divisor.
    Raises:
        TypeError: if the matrix is not list of list
        TypeError: if the rows are diff lenghts
        TypeError: if div is not a num
        TypeError: if matrix has non numbers
        ZeroDivisionError: if div is zero
    Returns:
        matix containinng the results
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(value, int) or isinstance(value, float))
                    for value in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return list(map(lambda x: list(map(lambda y: 
        round(y / div, 2), x)), matrix))
