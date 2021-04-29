##usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    if len(tuple_a) < 2:
        tuple_a += (0, 0) #assigns 0 to an empty space
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
#        tempa = list(tuple_a)
#        tempb = list(tuple_b)
# if len(tempa) == 1:
#           tempa.append(0)
#       if len(tempb) == 1:
#           tempb.append(0)
#        tup_sum1 = tuple(tempa)
#        tup_sum2 = tuple(tempb)
    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]
    return (sum1, sum2)
