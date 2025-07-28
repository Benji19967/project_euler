import sympy

from utils.primes import generate_primes


def get_rotations(n):
    num_digits = len(str(n))
    num_rotations = num_digits - 1
    rotations = []
    for _ in range(num_rotations):
        d = n % 10
        n //= 10
        n = n + d * 10 ** (num_digits - 1)
        rotations.append(n)
    return rotations


def main():
    primes = generate_primes(1_000_001)

    count = 0
    for p in primes:
        rotations = get_rotations(p)
        if not rotations or all(sympy.isprime(r) for r in rotations):
            count += 1
            print(p, rotations)
    print(count)


if __name__ == "__main__":
    main()
