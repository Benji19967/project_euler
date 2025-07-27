def sum_of_digits_5th_power(n):
    _sum = 0
    while n > 0:
        digit = n % 10
        _sum += digit**5
        n //= 10
    return _sum


def main():
    _sum = 0
    for n in range(2, 310_000):  # rough estimate of upper bound
        if n == sum_of_digits_5th_power(n):
            print(n)
            _sum += n
    print(_sum)


if __name__ == "__main__":
    main()
