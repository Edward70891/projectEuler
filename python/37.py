from prime_sieve import PrimeSieve

trunc_primes = set()
all_primes = PrimeSieve(1000000).primes_set
primes_iter = iter(all_primes)

while len(trunc_primes) < 11:
    current = next(primes_iter)
    current_str = str(current)
    current_str_len = len(current_str)
    if current_str_len == 1:
        continue
    left_truncations = {
        int(current_str[i:])
        for i in range(1, current_str_len)
    }
    left_truncations.add(current)
    right_truncations = {
        int(current_str[:i])
        for i in range(1, current_str_len)
    }
    if left_truncations | right_truncations < all_primes:
        trunc_primes.add(current)

print(sum(trunc_primes))
