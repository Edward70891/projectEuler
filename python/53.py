#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=53

from math import factorial


def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


over_million = list()
for n in range(1, 101):
    for r in range(n + 1):
        if choose(n, r) > 1000000:
            over_million.append((n, r))

print(len(over_million))
