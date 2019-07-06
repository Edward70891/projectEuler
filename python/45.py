#!/bin/env python3
from miscLibraries.python.number_funcs import (get_hexagonal, get_pentagonal,
                                               get_triangular)

# Problem at:
# https://projecteuler.net/problem=45
BIG_RANGE = range(2, 100000)
triangular = [get_triangular(num) for num in BIG_RANGE]
pentagonal = {get_pentagonal(num) for num in BIG_RANGE}
hexagonal = {get_hexagonal(num) for num in BIG_RANGE}

valid = [i for i in triangular if i in hexagonal and i in pentagonal]

print(f"{len(valid)} numbers found.")
print(valid[1])
