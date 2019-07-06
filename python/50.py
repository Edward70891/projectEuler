#!/bin/env python3
from miscLibraries.python.prime_sieve import PrimeSieve

# Problem at:
# https://projecteuler.net/problem=50

MAX_VAL = 1000000
sieve = PrimeSieve(MAX_VAL)
primes = sieve.primes

current_best = list()
for i in range(len(primes)):
    for o in range(i + 1, len(primes)):
        current_seq = primes[i:o]
        current_sum = sum(current_seq)
        if current_sum > MAX_VAL:
            break
        if sieve.get(current_sum) and len(current_seq) > len(current_best):
            current_best = current_seq

print(sum(current_best))
