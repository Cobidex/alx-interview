#!/usr/bin/python3
"""contains the rotate_2d_matrix method
"""


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
