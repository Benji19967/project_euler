def generate_pentagonals(num: int):
    _nums = []
    for n in range(1, num):
        number = int((n / 2) * (3 * n - 1))
        _nums.append(number)
    return _nums


def main():
    pentagonals = generate_pentagonals(10000)
    pentagonals_set = set(pentagonals)

    for i in range(len(pentagonals)):
        for j in range(i, len(pentagonals)):
            _sum = pentagonals[i] + pentagonals[j]
            _diff = pentagonals[j] - pentagonals[i]
            if _sum in pentagonals_set and _diff in pentagonals_set:
                print(abs(pentagonals[i] - pentagonals[j]))
                print(pentagonals[i], pentagonals[j])


if __name__ == "__main__":
    main()
