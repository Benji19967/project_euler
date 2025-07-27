from decimal import *

getcontext().prec = 100000


def has_recurring_cycle(n: int, num_decimals: int = 100):
    fraction = Decimal(1) / Decimal(n)
    print(fraction)


def find_recurring_cycle(n: int):
    decimals = str(Decimal(1) / Decimal(n))[4:]
    cycle = decimals[:48]
    found_at = decimals[48:].find(cycle)
    # print(n, found_at)
    return found_at


def test():
    assert not has_recurring_cycle(2)


def main():
    max_found = 0
    n_at_max_found = None
    for n in range(100, 1000):
        found_at = find_recurring_cycle(n)
        if found_at > max_found:
            max_found = found_at
            n_at_max_found = n
    print(n_at_max_found, max_found)


if __name__ == "__main__":
    # test()

    main()
