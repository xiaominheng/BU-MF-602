#
# a6task1.py - Assignment 6, Task 1
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Implementing a Matrix as a 2-D List
#


# Puzzle1: Implementing a Matrix as a 2-D List
def print_helper(m):
    """
    :param m: A matrix to be printed
    :return: print the matrix in a proper format
    """
    for i in range(len(m)):
        for j in range(len(m[i])):
            # The first line
            if i == 0:
                if j == 0:
                    # Consider a one row/column matrix
                    if len(m[i]) != 1:
                        print("[[%.2f" % m[i][j], end=', ')
                    else:
                        print("[[%.2f]" % m[i][j], end='\n')
                elif j == len(m[i])-1:
                    print("%.2f]" % m[i][j], end='\n')
                else:
                    print("%.2f" % m[i][j], end=', ')

            # The last line
            elif i == len(m)-1:
                if j == 0:
                    if len(m[i]) != 1:
                        print(" [%.2f" % m[i][j], end=', ')
                    else:
                        print(" [%.2f]]" % m[i][j], end='\n')
                elif j == len(m[i])-1:
                    print("%.2f]]" % m[i][j], end='\n')
                else:
                    print("%.2f" % m[i][j], end=', ')

            # Other lines
            else:
                if j == 0:
                    if len(m[i]) != 1:
                        print(" [%.2f" % m[i][j], end=', ')
                    else:
                        print(" [%.2f]" % m[i][j], end='\n')
                elif j == len(m[i])-1:
                    print("%.2f]" % m[i][j], end='\n')
                else:
                    print("%.2f" % m[i][j], end=', ')

def print_matrix(m, label=''):
    """
    :param m: A matrix to be printed
    :param label: The label of the matrix(can be omitted)
    :return: Print the matrix in a proper way
    """
    if label == '':
        print_helper(m)
    else:
        print(label + ' =')
        print_helper(m)


# Puzzle2: Create and return an n * m matrix containing all zeros.
def zeros_helper(n, m):
    """
    :param n: n rows
    :param m: m cols
    :return: n*m zero matrix
    """
    org = []
    return [[0 for _ in range(m)] for i in range(n)]

def zeros(n, m=0):
    """
    :param n: n rows
    :param m: m cols(if omitted, equal to n)
    :return: n*m zero matrix
    """
    if m == 0:
        m = n
    return zeros_helper(n, m)


# Puzzle3: Creates and return an n * n identity matrix containing the value of 1 along the diagonal.
def identity_matrix(n):
    """
    :param n: dimension
    :return: n*n diagonal matrix
    """
    diag = zeros(n)
    for i in range(n):
        diag[i][i] = 1
    return diag


# Puzzle4: Create and return the transpose of a matrix.
def transpose(M):
    """
    :param M: The original matrix
    :return: Transposed matrix
    """
    transposed_M = zeros(len(M[0]), len(M))
    for i in range(len(transposed_M)):
        for j in range(len(transposed_M[i])):
            transposed_M[i][j] = M[j][i]
    return transposed_M


# Puzzle5: Modify the matrix with a specific row order
def swap_rows(M, src, dest):
    """
    :param M: The original matrix
    :param src: row 1
    :param dest: row 2
    :return: None
    """
    assert src < len(M) and dest < len(M), "out of index"
    M[src], M[dest] = M[dest], M[src]


# Puzzle6: Multiplie all values in the row
def mult_row_scalar(M, row, scalar):
    """
    :param M: Original matrix
    :param row: target row
    :param scalar: a scalar number
    :return: None
    """
    M[row] = [M[row][i] * scalar for i in range(len(M[row]))]


# Puzzle7: Perform the elementary-row operation to add the src row into the dest row
def add_row_into(M, src, dest):
    """ Add src on dest row
    :param M: The original matrix
    :param src: The row used to add
    :param dest: target row
    :return: None
    """
    M[dest] = [M[src][i] + M[dest][i] for i in range(len(M[dest]))]
