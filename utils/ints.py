import math


def num_digits(n: int) -> int:
    if n == 0:
        return 1
    return int(math.log10(n)) + 1


def digits_to_int(digits: list) -> int:
    num = 0
    for d in digits:
        num = num * 10 + d
    return num


def reverse(n: int) -> int:
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


def is_palindromic(n) -> bool:
    if n <= 9:
        return True

    n_str = str(n)
    i, j = 0, len(n_str) - 1
    while i < j:
        if n_str[i] != n_str[j]:
            return False
        i += 1
        j -= 1
    return True
