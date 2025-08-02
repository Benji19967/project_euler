import sympy

from utils.primes import generate_primes


def main():
    primes = generate_primes(1_000_000)

    max_num_primes = 0
    sequence = []
    max_sum = 0
    for num_primes in range(
        550, 21, -1
    ):  ## 550 is a rough upper bound, 550 first primes summed up are larger than 1 mio.
        i = 0
        _sum = 0
        while _sum < 1_000_000:
            _sum = sum(primes[i : i + num_primes])
            if _sum >= 1_000_000:
                continue
            if sympy.isprime(_sum):
                if num_primes > max_num_primes:
                    max_num_primes = num_primes
                    sequence = primes[i : i + num_primes]
                    max_sum = _sum
            if max_num_primes > num_primes:
                print(max_sum)
                print(max_num_primes)
                print(sequence)
                return
            i += 1


if __name__ == "__main__":
    main()
