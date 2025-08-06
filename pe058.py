import sympy


def main():
    prime_count = 0
    l = 3  # spiral length
    nums_on_diagonals = 5

    while True:
        bottom_right = l**2
        bottom_left = l**2 - l + 1
        top_left = l**2 - 2 * l + 2
        top_right = l**2 - 3 * l + 3

        for n in [bottom_right, bottom_left, top_left, top_right]:
            if sympy.isprime(n):
                prime_count += 1

        ratio = prime_count / nums_on_diagonals
        if ratio * 100 < 10:
            print(l)
            break

        nums_on_diagonals += 4
        l += 2


if __name__ == "__main__":
    main()
