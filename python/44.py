#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=44


def get_pentagonal(num):
    return int(num * (3 * num - 1) * 0.5)


diffs = list()
pentagonals = [get_pentagonal(i) for i in range(1, 10000)]
pentagonal_set = set(pentagonals)
for i in pentagonals:
    for o in pentagonals:
        diff = abs(i - o)
        if (i + o in pentagonal_set) and (diff in pentagonal_set):
            diffs.append(diff)

print(min(diffs))
