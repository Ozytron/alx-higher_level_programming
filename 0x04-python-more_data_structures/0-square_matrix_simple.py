#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for row in range(len(matrix)):
        new_matrix = list(map(lambda x: x**2, matrix[row]))

    return (new_matrix)
