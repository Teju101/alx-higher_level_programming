#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)
    if len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)
    if len(tuple_a) == 0:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) == 0:
        tuple_b = tuple_b + (0, 0)

    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]

    new_tuple = new_tuple + (sum1, sum2)
    return (new_tuple)
