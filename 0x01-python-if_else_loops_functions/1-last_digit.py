#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if number < 0:
    temp = number * -1
    num = temp % 10
    if num != 0:
        num = -num
else:
    num = number % 10
if num > 5:
    print('Last digit of {} is {} and is greater\
than 5'.format(number, num))
elif num == 0:
    print('Last digit of {} is {} and is 0'.format(number, num))
elif num < 6 and num != 0:
    print('Last digit of {} is {} and is less \
than 6 and not 0'.format(number, num))
