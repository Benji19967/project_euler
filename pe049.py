from typing import Counter

from utils.primes import generate_primes

COUNTERS = set()


def hash_counter(c):
    return hash(tuple(sorted(c.items())))


def is_permutation(c1, c2):
    if c1 == c2:
        COUNTERS.add(hash_counter(c1))
        return True
    return False


def main():
    primes = generate_primes(n=9999, start=1000)
    sequences = []
    for i, p1 in enumerate(primes):
        sequence = [p1]
        c1 = Counter(str(p1))
        if hash_counter(c1) in COUNTERS:
            continue
        for p2 in primes[i + 1 :]:
            c2 = Counter(str(p2))
            if is_permutation(c1, c2):
                sequence.append(p2)
        sequences.append(sequence)

    for s in sequences:
        for x, y, z in zip(s, s[1:], s[2:]):
            if y - x == z - y:
                print(x, y, z)


if __name__ == "__main__":
    main()
