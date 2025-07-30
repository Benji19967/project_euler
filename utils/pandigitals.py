import itertools


def generate_pandigitals(
    lowest_digit: int, num_digits: int, order_decreasing: bool = False
):
    """
    if order_decreasing, starts with largest number.
    Ex. (lowest_digit=2, num_digits=4): "5432", instead of "2345", ...
    """
    if order_decreasing:
        digits = int(
            "".join(
                [
                    str(d)
                    for d in range(lowest_digit + num_digits - 1, lowest_digit - 1, -1)
                ]
            )
        )
    else:
        digits = int(
            "".join([str(d) for d in range(lowest_digit, lowest_digit + num_digits, 1)])
        )

    for n_str in itertools.permutations(str(digits), num_digits):
        n = int("".join(n_str))
        yield n
