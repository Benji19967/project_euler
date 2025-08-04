from utils import ints

MAX_ITERATIONS = 50


def is_lychrel_number(n):
    for _ in range(MAX_ITERATIONS):
        n_rev = ints.reverse(n)
        if ints.is_palindromic(n + n_rev):
            return False
        n = n + n_rev
    return True


def main():
    count = 0
    for n in range(1, 10_000):
        if is_lychrel_number(n):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
