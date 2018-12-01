import math


primesDict = {0: False, 1: False}


def isPrime(n):
    # Type check for integers
    if not isinstance(n, int):
        raise TypeError("n must be an integer!")

    try:
        return primesDict[n]
    except Exception:
        pass

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            primesDict[n] = False
            return False
    primesDict[n] = True
    return True
