from fractions import Fraction

from utils import ints


def main():
    count = 0
    frac = Fraction(1, 2)
    for _ in range(999):
        frac = 1 / (2 + frac)
        _sum = 1 + frac
        if ints.num_digits(_sum.numerator) > ints.num_digits(_sum.denominator):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
