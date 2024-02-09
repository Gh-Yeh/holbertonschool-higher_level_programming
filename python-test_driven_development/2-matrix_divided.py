#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of matrix by div.
    Args:
        matrix: List of lists containing int or float values
        div: must be a number
    Returns:
        list: new matrix representing divided matrix.
    Raises:
        TypeError: If matrix is not a matrix containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float or equal to zero.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        new_list.append([round(items/div, 2) for items in row])
    return new_list
