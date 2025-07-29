import math


def main():
    sol = [0] * 1001
    for a in range(1, 300):
        for b in range(a, 400):
            c = math.sqrt((a**2) + (b**2))
            if c.is_integer():
                p = a + b + int(c)
                if p <= 1000:
                    sol[p] += 1
    print(sol.index(max(sol)))


if __name__ == "__main__":
    main()
