#!/bin/env python3
from math import sqrt

# Problem at:
# https://projecteuler.net/problem=39

# Horribly dirty brute force solution

solution_counts = [0] * 1001
for perimeter in range(1, 1001):
    for side1 in range(1, perimeter // 2):
        for side2 in range(1, perimeter // 2):
            if sqrt(side1**2 + side2**2) == float(perimeter - side1 - side2):
                solution_counts[perimeter] += 1

print(solution_counts.index(max(solution_counts)))
