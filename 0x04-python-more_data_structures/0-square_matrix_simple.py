#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = matrix.copy()
    for j in range(len(matrix)):
        result_matrix[j] = list(map(lambda y: y**2, matrix[j]))
    return (result_matrix)

 
 
 
