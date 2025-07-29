import itertools

import sympy

from utils.primes import generate_primes

"""
Optimization: n can only contain 7 digits.
Explanation: any number is congruent mod 9 with the sum of its digits,
(n - sum_digits(n) mod 9 = 0). Therefore, if sum_digits(n) mod 9 = 0, 3 or 6 then 
sum_digits(n) is divisible by 3, and thus, so is n. In that case, n is not prime. 

1+2+3+4+5+6+7+8+9=45 (any 9-digit pandigital cannot be prime)
1+2+3+4+5+6+7+8=36 (any 8-digit pandigital cannot be prime)
"""


def main():
    for num_digits in range(7, 0, -1):
        digits = int("".join([str(d) for d in range(num_digits, 0, -1)]))
        for n_str in itertools.permutations(str(digits), num_digits):
            n = int("".join(n_str))
            if sympy.isprime(n):
                print(n)
                break


if __name__ == "__main__":
    main()
