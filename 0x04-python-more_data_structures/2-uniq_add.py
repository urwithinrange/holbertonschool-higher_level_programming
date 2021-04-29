#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    list_sum = 0
    for n in new_list:
        list_sum += n
    return list_sum
