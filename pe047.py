import sympy

NUMS = range(2, 1000000)


def get_prime_factors(n):
    prime_factors = set()
    limit = n / 2
    i = 0
    p = NUMS[i]
    while p < limit:
        if n % p == 0:
            if sympy.isprime(p):
                prime_factors.add(p)
            if sympy.isprime(n // p):
                prime_factors.add(n // p)
        limit = n / p
        i += 1
        p = NUMS[i]
    return prime_factors


def main():
    consecutive = 0
    for n in range(647, 1000000):
        prime_factors = get_prime_factors(n)
        if len(prime_factors) == 4:
            consecutive += 1
            if consecutive == 4:
                print(n - 3)
                break
        else:
            consecutive = 0


if __name__ == "__main__":
    main()
