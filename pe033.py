def find_common_digit(n: int, m: int):
    n_digits = set((n % 10, n // 10))
    m_digits = set((m % 10, m // 10))
    common_digit = n_digits.intersection(m_digits)

    return int(common_digit.pop()) if common_digit else None


def remove_common_digit(n: int, m: int, digit: int):
    n_digits = set((n % 10, n // 10))
    m_digits = set((m % 10, m // 10))

    if len(n_digits) == 2:
        n_digits.discard(digit)
    if len(m_digits) == 2:
        m_digits.discard(digit)

    return int(n_digits.pop()), int(m_digits.pop())


def main():
    numerators = 1
    denominators = 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            common_digit = find_common_digit(numerator, denominator)
            if common_digit:
                n, m = remove_common_digit(numerator, denominator, common_digit)
                if m > 0 and numerator / denominator == n / m:
                    print(numerator, denominator, n, m)
                    numerators *= numerator
                    denominators *= denominator
    print(numerators / denominators)


if __name__ == "__main__":
    main()
