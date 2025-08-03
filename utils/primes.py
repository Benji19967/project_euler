import math

import numpy as np


def primes_up_to(n):
    """Efficiently generate all primes <= n using NumPy and odd-only optimization."""
    if n < 2:
        return []

    # Only consider odd numbers (2 is the only even prime)
    sieve = np.ones((n // 2,), dtype=bool)
    sieve[0] = False  # 1 is not prime

    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = False

    # Convert sieve index to actual prime numbers
    primes = np.nonzero(sieve)[0] * 2 + 1
    return np.insert(primes, 0, 2)  # Insert 2, the only even prime


def generate_primes(n, start: int = 2):
    """
    Generate primes up to and including n

    Sieve of Eratosthenes
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for divisor in range(2, int(math.sqrt(n))):
        if is_prime[divisor]:
            for multiplier in range(2, n // divisor + 1):
                is_prime[divisor * multiplier] = False

    primes = []
    for num in range(len(is_prime)):
        if is_prime[num] and num >= start:
            primes.append(num)

    return primes
