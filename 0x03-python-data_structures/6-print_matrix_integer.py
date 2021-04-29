#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    arrlen = len(matrix[0])
    if arrlen == 0:
        print()
    else:
        for col in matrix:
            count = 0
            for i in col:
                count += 1
                if count == arrlen:
                    print('{}'.format(i), end="\n")
                else:
                    print('{} '.format(i), end="")
