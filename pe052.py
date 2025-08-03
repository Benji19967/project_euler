from collections import Counter


def main():
    for n in range(120_000, 100_000_000):
        digits_counter = Counter(str(n))
        count = 0
        for mult in [2, 3, 4, 5, 6]:
            digits_counter_mult = Counter(str(mult * n))
            if digits_counter_mult == digits_counter:
                count += 1
                if count == 5:
                    print(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)
                    return
            else:
                break


if __name__ == "__main__":
    main()
