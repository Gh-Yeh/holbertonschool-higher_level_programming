#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for mtrx in matrix:
            for row in mtrx:
                print("{:d}".format(row), end=" " if row != mtrx[-1] else "\n")
