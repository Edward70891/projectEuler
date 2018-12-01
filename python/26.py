#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=26


def recurringLength(n):
    total = 0
    
    while True:
        
    return total


upperBound = int(input("Enter the highest number you want to test: "))
lowerBound = int(input("Enter the lowest number you want to test: "))
lengths = [recurringLength(i) for i in range(lowerBound, upperBound + 1)]
highest = max(lengths)
highestIndex = lengths.index(highest)
print("The highest recursion was given by 1/" + str(highestIndex) + " with a recursive length of " + str(highest))
