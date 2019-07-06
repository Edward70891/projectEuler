#!/bin/env python3
from miscLibraries.python.pandigital import PanChecker

# Problem at:
# https://projecteuler.net/problem=43

divisors = (2, 3, 5, 7, 11, 13, 17)
base_set = PanChecker(9, True).pandigital_list

valid = [
    num for num in base_set if all(
        int(str(num)[i + 1:i + 4]) % divisors[i] == 0 for i in range(7))
]

print(sum(valid))
