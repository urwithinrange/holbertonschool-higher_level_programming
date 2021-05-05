#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):  # whish list is longer
    try:
        quotient = []
        for i in range(0, list_length):
            try:
                quotient.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                quotient.append(0)
            except TypeError:
                print("wrong type")
                quotient.append(0)
            except IndexError:
                print("out of range")
                quotient.append(0)
    finally:
        return quotient
