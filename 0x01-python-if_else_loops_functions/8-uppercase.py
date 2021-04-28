#!/usr/bin/python3
def uppercase(str):
    strcat = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            strcat += chr(ord(i) - 32)
        else:
            strcat += i
    print('{}'.format(strcat))
