#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mtrx in matrix:
        for row in mtrx:
            print("{:d}".format(row), end=" " if row != mtrx[-1] else "\n")
