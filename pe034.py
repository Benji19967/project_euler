import math


def digits_of_int(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return reversed(digits)


def sum_of_digit_factorials(n):
    digits = digits_of_int(n)
    return sum(math.factorial(d) for d in digits)


def main():
    _sum = 0
    for n in range(3, 3_000_000):  # rough upper bound
        if n == sum_of_digit_factorials(n):
            _sum += n
            print(n)
    print(_sum)


if __name__ == "__main__":
    main()
