#!/bin/env python3
from miscLibraries.python.prime_sieve import PrimeSieve

# Problem at:
# https://projecteuler.net/problem=47

sieve = PrimeSieve(1000000)

valid = list()
current = 2
while len(valid) < 4:
    if len(set(sieve.prime_factors(current))) == 4:
        valid.append(current)
    else:
        valid.clear()
    current += 1

print(valid[0])
