import itertools
import math
from typing import Iterable

from utils.ints import digits_to_int
from utils.primes import generate_primes, primes_up_to


def concat_ints(n: int, m: int) -> int:
    return n * 10 ** (len(str(m))) + m


def find_primes_in_digits(digits: list, PRIMES):
    primes = []
    for prime_length in range(1, 5):
        for start in range(len(digits)):
            num = digits_to_int(digits[start : start + prime_length])
            if num in PRIMES:
                primes.append(num)
    if len(set(primes)) >= 5:
        return set(primes)
    return []


def count_prime_pairs(primes: Iterable, PRIMES_SET):
    count = 0
    prime_pairs = set()
    for n, m in list(itertools.combinations(primes, 2)):
        if concat_ints(n, m) in PRIMES_SET and concat_ints(m, n) in PRIMES_SET:
            count += 1
            prime_pairs.add(n)
            prime_pairs.add(m)
    return count, prime_pairs


def main():
    PRIMES = generate_primes(start=1_000_000, n=5_000_000)
    PRIMES_SET = set(primes_up_to(10_000_0000))

    # print(math.comb(168, 5))
    # print(len(primes))

    # combs = itertools.combinations(primes, 5)
    for p in PRIMES:
        digits = [int(x) for x in str(p)]
        d1 = digits_to_int(digits[:4])
        d2 = digits_to_int(digits[4:])
        if (
            d1 in PRIMES_SET
            and d2 in PRIMES_SET
            and digits_to_int(digits[4:] + digits[:4]) in PRIMES_SET
        ):
            primes = find_primes_in_digits(digits, PRIMES)
            if primes:
                primes.remove(d1)
                primes.remove(d2)
                for m, n, o in itertools.combinations(primes, 3):
                    primes_to_test = [d1, d2, n, m, o]
                    count, prime_pairs = count_prime_pairs(primes_to_test, PRIMES_SET)
                    if count == math.comb(len(primes_to_test), 2):
                        print(digits_to_int(digits), prime_pairs, sum(prime_pairs))
        if len(digits) < 6:
            break
        continue


if __name__ == "__main__":
    main()
