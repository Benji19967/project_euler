import sympy

from utils.primes import generate_primes


def is_truncatable_prime(n):
    m = n

    while m > 9:
        m //= 10
        if not sympy.isprime(m):
            return False

    num = 0
    power = 0
    while n > 9:
        num += (n % 10) * (10**power)
        if not sympy.isprime(num):
            return False
        power += 1
        n //= 10

    return True


def main():
    primes = generate_primes(1000000)
    _sum = 0
    for p in primes[4:]:
        if is_truncatable_prime(p):
            print(p)
            _sum += p
    print(_sum)


if __name__ == "__main__":
    main()
