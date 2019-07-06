#!/bin/env python3
from collections import Counter

# Problem at:
# https://projecteuler.net/problem=38

PAN_DIGITS = Counter("123456789")

valid_nums = list()
for base in range(1, 33334):
    for mult_max in range(2, 10):
        pan_test = "".join([str(base * i) for i in range(1, mult_max)])
        if Counter(pan_test) == PAN_DIGITS:
            valid_nums.append(pan_test)

print(max(valid_nums))
