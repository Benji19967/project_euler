from itertools import permutations


def to_int(t: tuple):
    return int("".join(map(str, t)))


def main():
    products = set()
    perms = list(permutations(range(1, 10)))
    for perm in perms:
        for len_m1 in [1, 2]:
            m1 = to_int(perm[:len_m1])
            m2 = to_int(perm[len_m1:5])
            prod = to_int(perm[5:])
            if m1 * m2 == prod:
                products.add(prod)
    print(sum(products))


if __name__ == "__main__":
    main()
