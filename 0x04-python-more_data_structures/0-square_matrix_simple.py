#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(element ** 2)
        new_matrix.append(result_row)
    return new_matrix
