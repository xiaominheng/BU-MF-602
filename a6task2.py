#
# a6task2.py - Assignment 6, Task 2
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Matrix Operations
#

from a6task1 import *

# Puzzle1: Add two matrices
def add_matrices(A, B):
    """
    :param A: Matrix A
    :param B: Matrix B
    :return: Matrix A + Matrix B
    """
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Not Same Size"
    return [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]


# Puzzle2: Subtract between A and B
def sub_matrices(A, B):
    """
    :param A: Matrix A
    :param B: Matrix B
    :return: Matrix A - Matrix B
    """
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Not Same Size"
    return [[A[i][j] - B[i][j] for j in range(len(A[i]))] for i in range(len(A))]


# Puzzle3: Zoom a matrix
def mult_scalar(M, s):
    """
    :param M: Target Matrix
    :param s: scalar
    :return: Zoomed matrix
    """
    return [[M[i][j]*s for j in range(len(M[i]))] for i in range(len(M))]


# Puzzle4: Dot product of two matrices
def dot_product(M, N):
    """
    :param M: Matrix M
    :param N: Matrix N
    :return: Dot product of M and N
    """
    assert len(M[0]) == len(N), "Cannot dot product"
    outcome = zeros(len(M), len(N[0]))
    for i in range(len(outcome)):
        for j in range(len(outcome[i])):
            outcome[i][j] = sum([x * y for x, y in zip(M[i], transpose(N)[j])])
    return outcome

# Puzzle5: Subset a Matrix
def create_sub_matrix(M, exclude_row, exclude_col):
    """
    :param M: Matrix M
    :param exclude_row: The row which is not wanted
    :param exclude_col: The column which is not wanted
    :return: The modified Matrix
    """
    exclude_row_matrix = [M[i] for i in range(len(M)) if i != exclude_row]
    transposed = transpose(exclude_row_matrix)
    exclude_col_matrix = [transposed[i] for i in range(len(transposed)) if i != exclude_col]
    return transpose(exclude_col_matrix)


# Puzzle6: Calculate the dererminant of Matrix M
def determinant(M):
    """
    :param M: A phalanx matrix
    :return: The determinant of matrix M
    """
    assert len(M) == len(transpose(M)), "Not a phalanx"
    if len(M) == 1:
        return M[0][0]
    elif len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    else:
        return sum([pow(-1, i)*M[0][i]*determinant(create_sub_matrix(M, 0, i)) for i in range(len(M))])


# Puzzle7: Calculate the minors matrix of a matrix
def matrix_of_minors(M):
    """
    :param M: phalanx matrix M
    :return: The minor matrix of M
    """
    minors = zeros(len(M))
    for i in range(len(M)):
        for j in range(len(M)):
            minors[i][j] = determinant(create_sub_matrix(M, i, j))
    return minors


# Puzzle8: Inverse matrix of a matrix
def inverse_matrix(M):
    """
    :param M: Matrix M
    :return: Inverse Matrix of M
    """
    assert len(M) == len(transpose(M)), "Not a phalanx"

    matrix_of_cofactors = [[pow(-1, i+j) for j in range(len(M))] for i in range(len(M))]

    minor_matrix = matrix_of_minors(M)

    for i in range(len(minor_matrix)):
        for j in range(len(minor_matrix)):
            minor_matrix[i][j] *= matrix_of_cofactors[i][j]

    adjugate = transpose(minor_matrix)

    determinant_of_m = determinant(M)
    for i in range(len(adjugate)):
        for j in range(len(adjugate)):
            adjugate[i][j] /= determinant_of_m

    return adjugate