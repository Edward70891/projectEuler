#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=35


from helpful import isPrime


def circularPrime(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer!")

    if n == 2:
        return True

    # If there are any even digits left in the number, it's not a circular prime
    for char in str(n):
        if char in "02468":
            return False

    # -- Permute the Number --
    length = len(str(n))
    # List to store all permutations
    permutations = [str(n)]
    # Go through (length) times, shifting the digits along every time
    for i in range(1, length):
        permutations.append("")
        for o in range(length):
            permutations[i] += str(n)[(i + o) % length]
    permutations = [int(i) for i in permutations]

    for num in permutations:
        if not isPrime(num):
            return False
    return True

lowerBound = int(input("Enter the lowest number you would like to test to: "))
upperBound = int(input("Enter the highest number you would like to test to: "))
total = 0
for i in range(lowerBound, upperBound + 1):
    if circularPrime(i):
        total += 1
print("Under " + str(upperBound) + ": " + str(total))
