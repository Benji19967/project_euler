import sympy.ntheory as nt


def is_prime(n):
    return nt.isprime(n)


def main():
    max_prime_count = 0
    a_max_prime_count = None
    b_max_prime_count = None
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            prime_count = 0
            for n in range(100):
                if is_prime((n * n) + (a * n) + b):
                    print(a, b, n, (n * n) + (a * n) + b)
                    prime_count += 1
                    if prime_count > max_prime_count:
                        max_prime_count = prime_count
                        a_max_prime_count = a
                        b_max_prime_count = b
                        print(a, b, prime_count)
                else:
                    prime_count = 0
                    break
    print(a_max_prime_count, b_max_prime_count, max_prime_count)


if __name__ == "__main__":
    main()
