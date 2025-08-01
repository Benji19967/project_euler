import math


def generate_triangles(num: int):
    _nums = []
    for n in range(1, num):
        number = int((n / 2) * (n + 1))
        _nums.append(number)
    return _nums


def generate_pentagonals(num: int):
    _nums = []
    for n in range(1, num):
        number = int((n / 2) * (3 * n - 1))
        _nums.append(number)
    return _nums


def generate_hexagonals(num: int):
    _nums = []
    for n in range(1, num):
        number = int(n * (2 * n - 1))
        _nums.append(number)
    return _nums


def is_int(n):
    return n - int(n) == 0


def is_pentagonal(num):
    return is_int((1 + math.sqrt(1 + (24 * num))) / 6)


def main():
    # triangles = generate_triangles(100000)
    # triangles_set = set(triangles)
    # pentagonals = generate_pentagonals(100000)
    # pentagonals_set = set(pentagonals)
    hexagonals = generate_hexagonals(100000)
    # hexagonals_set = set(hexagonals)
    #
    # tp = triangles_set.intersection(pentagonals_set)
    # tph = tp.intersection(hexagonals_set)
    # print(tph)

    # faster solution: all hexagonals are also triangle numbers
    #
    # pentagonals: n/2 * (3n - 1) = p, thus 3n^2 - n - 2p = 0
    # then, by quadratic formula: n = (1 + sqrt(1 + 24p)) / 2 (only positives)
    # so if inserting p in formual gives an integer, then p is pentagonal

    for h in hexagonals:
        if is_pentagonal(h):
            print(h)


if __name__ == "__main__":
    main()
