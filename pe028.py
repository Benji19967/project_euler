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


def main():
    print(sum_diag_1() + sum_diag_2())


if __name__ == "__main__":
    main()
