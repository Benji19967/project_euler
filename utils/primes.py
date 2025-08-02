import math


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
