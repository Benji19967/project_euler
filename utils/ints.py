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


def sum_digits(n: int) -> int:
    _sum = 0
    while n > 0:
        _sum += n % 10
        n //= 10
    return _sum


def is_palindromic(n) -> bool:
    return str(n) == str(n)[::-1]
