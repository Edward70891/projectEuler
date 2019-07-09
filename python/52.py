#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=52
from collections import Counter

current = 1
multipliers = (2, 3, 4, 5, 6)
shares_digits = [False]
while not all(shares_digits):
    current += 1
    current_digits = Counter(str(current))
    multiplied_digits = [
        str(current * multiplier) for multiplier in multipliers
    ]
    shares_digits = [
        current_digits == Counter(multiplied)
        for multiplied in multiplied_digits
    ]

print(current)
