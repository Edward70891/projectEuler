#!/bin/env python3
from miscLibraries.python.prime_sieve import PrimeSieve

# Problem at:
# https://projecteuler.net/problem=46

MAX_VAL = 100000
primes = PrimeSieve(MAX_VAL).primes_set
to_check = iter(
    [i for i in range(9, MAX_VAL) if i % 2 == 1 and i not in primes])

current_valid = True
while current_valid:
    current = next(to_check)
    current_valid = False
    for i in range(1, current // 2):
        diff = current - ((i**2) * 2)
        if diff in primes:
            current_valid = True
            break

print(current)
