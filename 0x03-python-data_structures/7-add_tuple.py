#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lr = [0, 0]
    for idx in range(0, 2):
        try:
            lr[idx] += tuple_a[idx]
        except:
            lr[idx] += 0
        try:
            lr[idx] += tuple_b[idx]
        except:
            lr[idx] += 0
    tr = tuple(lr)
    return tr
