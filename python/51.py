#!/bin/env python3
from itertools import chain, combinations

from miscLibraries.python.prime_sieve import PrimeSieve

# Problem at:
# https://projecteuler.net/problem=51


def replace_indexes(string, indexes, replacement):
    to_return = string
    for index in indexes:
        to_return = to_return[:index] + str(replacement) + to_return[index +
                                                                     1:]
    return to_return


sieve = PrimeSieve(1000000)
primes_list = sieve.primes
primes_set = set(primes_list)
primes = iter(primes_list)

replacement_indexes = list(
    chain.from_iterable(combinations(range(6), o) for o in range(1, 8)))

current_family = [set(), 0]
while not (current_family[1] in current_family[0]
           and len(current_family[0]) == 8):
    current = next(primes)
    current_str = str(current)
    variations = [
        ({int(replace_indexes(current_str, indexes, i))
          for i in range(10)} & primes_set, current)
        for indexes in replacement_indexes
    ]
    current_family = sorted(variations, key=lambda elem: len(elem[0]))[-1]

print(current_family)
