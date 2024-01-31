#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for one_d in matrix:
        new_list.append([sqaure_it * sqaure_it for sqaure_it in one_d])
    return new_list
