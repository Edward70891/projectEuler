#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=27


from helpful import isPrime


def quadraticPrimeLength(a, b):
    if not isPrime(b):
        return 0
    current = 0
    result = (current ** 2) + (a * current) + b
    while isPrime(result):
        result = (current ** 2) + (a * current) + b
        current += 1
    print(current)
    return current


aMax = int(input("Enter the maximum absolute value for a: "))
bMax = int(input("Enter the maximum absolute value for b: "))

runs = []
products = []
for a in range(aMax * -1, aMax + 1):
    for b in range(bMax * -1, bMax + 1):
        runs.append(quadraticPrimeLength(a, b))
        products.append((a * b))
maxRunIndex = runs.index(max(runs))
print("The largest run was up to " + str(runs[maxRunIndex]) + " with a product of " + str(products[maxRunIndex]))
