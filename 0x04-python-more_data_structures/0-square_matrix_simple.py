#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_list = []
    for i in range(len(matrix)):
        num = []
        for j in range(len(matrix[0])):
            num.append(matrix[i][j] ** 2)
        sq_list.append(num)
    return sq_list
