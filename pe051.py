import itertools

from utils.primes import primes_up_to


def digits_to_int(digits: list):
    num = 0
    for d in digits:
        num = num * 10 + d
    return num


def main():
    primes = primes_up_to(10_000_000)
    primes_set = set(primes)

    for p in primes:
        digits = [int(n) for n in str(p)]
        indexes_to_replace = itertools.combinations(range(0, len(digits)), 3)
        for idx in indexes_to_replace:
            digits = [int(n) for n in str(p)]
            idx1, idx2, idx3 = idx
            count = 0
            ps = []
            for d in range(0, 10):
                if d == 0 and idx1 == 0:
                    continue
                digits[idx1] = d
                digits[idx2] = d
                digits[idx3] = d
                n = digits_to_int(digits)
                if n in primes_set:
                    ps.append(n)
                    count += 1
                if count == 8:
                    print(ps)
                    return


if __name__ == "__main__":
    main()
