#!/usr/bin/python3
for i in range(0, 100):
    fdigit = i % 100
    sdigit = i % 10
    if i != 99:
        print('{:02d}, '.format(i).rstrip('\n'), end="")
    if i == 99:
        print('{:2d}'.format(i))
