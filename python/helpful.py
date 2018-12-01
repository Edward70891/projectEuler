import math


primesDict = {0: False, 1: False}


def isPrime(n):
    # Type check for positive integers
    if not isinstance(n, int):
        raise TypeError("n must be an integer!")
    if n < 0:
        raise ValueError("n must be a positive integer!")

    # Check if we've already got something in the primes dictionary
    try:
        return primesDict[n]
    except KeyError:
        pass

    # If the last digit is even, reject it
    if str(n)[-1] in "02468":
        primesDict[n] = False
        return False

    # Try to run between 2 and the square root of the number, checking for divisibility and returning false if it ever is
    try:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                primesDict[n] = False
                return False
    # When testing large numbers, math.sqrt() will fail, so we use the more inefficient method of checking between 2 and n/2
    except ValueError:
        for i in range(2, math.ceil(n / 2) + 1):
            if n % i == 0:
                primesDict[n] = False
                return False
    # If all previous tests are passed, return true
    primesDict[n] = True
    return True
