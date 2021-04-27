#!/usr/bin/python3
for i in range(0, 90):
    fdigit = i / 10
    sdigit = i % 10
    if i != 89 and fdigit < sdigit:
        print('{:02d}, '.format(i).rstrip('\n'), end="")
    elif i == 89:
        print('{:2d}\n'.format(i), end="")
