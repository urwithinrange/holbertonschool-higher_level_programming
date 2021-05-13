#!/usr/bin/python3
"""pascal_triangle creates a triangle"""


def pascal_triangle(n):
    """creates n rows"""
    row = 0
    p_list = []
    s_list = []
    if n <= 0:
        return [[]]
    else:
        for x in range(n):
            s_list = []
            if row == 0:
                s_list.append(1)
            else:
                for i in range(row + 1):
                    if i == 0 or i == (row):
                        s_list.append(1)
                    else:
                        s_list.append(int(p_list[x - 1][i - 1]) +
                                      int(p_list[x - 1][i]))
            row += 1
            p_list.append(s_list)
    return p_list
