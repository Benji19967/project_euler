N = 1001


def sum_diag_1():
    i = 3
    _sum = i
    _adder = 4
    while i <= N * N:
        i += _adder
        if i > N * N:
            break
        _sum += i
        _adder += 2
    return _sum


def sum_diag_2():
    i = 1
    _sum = i
    _adder = 4
    while i <= N * N:
        for _ in range(2):
            i += _adder
            if i > N * N:
                break
            _sum += i
        _adder += 4
    return _sum


def sol_2():
    _sum = 1
    for n in range(3, 1002, 2):
        """
        The 4 corners are given by
        n^2
        n^2 - n + 1
        n^2 - 2n + 2
        n^2 - 3n + 3
        --> 4n^2 - 6n + 6
        """
        _sum += (4 * n * n) - (6 * n) + 6
    return _sum


def main():
    print(sum_diag_1() + sum_diag_2())
    print(sol_2())


if __name__ == "__main__":
    main()
