from miscLibraries.python.prime_sieve import PrimeSieve


def get_rotations(num):
    doubled_string = str(num) * 2
    string_len = len(str(num))
    return [int(doubled_string[i:i + string_len]) for i in range(string_len)]


generator = PrimeSieve(1000000)
generator.generate()
circular_primes = set()

for prime in generator.primes_set:
    if prime in circular_primes:
        continue
    rotations = get_rotations(prime)
    if all(generator[rotation] for rotation in rotations):
        circular_primes |= set(rotations)

print(len(circular_primes))
