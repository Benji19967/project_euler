import sympy

from utils.primes import generate_primes


def main():
    primes = set(generate_primes(10000))
    squares = [n**2 for n in range(1, 1000)]

    for n in range(35, 10_000, 2):
        if sympy.isprime(n):
            continue

        meets_criteria = False
        i = 0
        square = squares[i]
        while 2 * square < n:
            diff = n - (2 * square)
            if diff in primes:
                meets_criteria = True
                break
            i += 1
            square = squares[i]

        if not meets_criteria:
            print(n)
            break


if __name__ == "__main__":
    main()
