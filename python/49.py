#!/bin/env python3
from itertools import permutations

from miscLibraries.python.prime_sieve import PrimeSieve

# Problem at:
# https://projecteuler.net/problem=49

primes = PrimeSieve(10000).primes_set

for i in set(range(1000, 10000)) & primes:
    perms = [
        int("".join(letters)) for letters in permutations(str(i))
        if int("".join(letters)) != i
    ]
    remaining_perms = set(perms) & primes
    for o in remaining_perms:
        diff = o - i
        if diff > 0:
            for p in remaining_perms:
                if p - o == diff:
                    whole = "".join(str(num) for num in (i, o, p))
                    if len(whole) == 12:
                        print(whole)
