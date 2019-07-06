#!/bin/env python3
from miscLibraries.python.pandigital import PanChecker

# Problem at:
# https://projecteuler.net/problem=38

valid_nums = list()
checker = PanChecker()
for base in range(1, 33334):
    for mult_max in range(2, 10):
        pan_test = "".join([str(base * i) for i in range(1, mult_max)])
        if PanChecker.is_pandigital(pan_test):
            valid_nums.append(pan_test)

print(max(valid_nums))
