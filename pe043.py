from utils.pandigitals import generate_pandigitals


def main():
    pandigitals = list(generate_pandigitals(0, 10, order_decreasing=True))

    _sum = 0
    for pandigital in pandigitals:
        has_property = True
        for d_i_start, divisor in zip(range(2, 9), [2, 3, 5, 7, 11, 13, 17]):
            num = int(str(pandigital)[d_i_start - 1 : d_i_start - 1 + 3])
            if num % divisor != 0:
                has_property = False
                break

        if has_property:
            print(pandigital)
            _sum += pandigital
    print(_sum)


if __name__ == "__main__":
    main()
