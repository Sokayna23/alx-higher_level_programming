#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square = list(map(lambda x: x ** 2, row))
        square_matrix.append(square)
    return square_matrix
