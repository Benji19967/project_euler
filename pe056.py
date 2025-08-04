from utils import ints

"""
To be learned:
- on average a digit contributes 5 to the sum (assumes digits uniformly distributed)
- num_digits: int(b log_10 a) + 1
  - 90^99=194 digits (~sum: 970)
  - 90^90=176 digits (~sum: 880) significantly lower than 90^99. 
    - --> Safe/modest starting point
"""


def main():
    max_sum = 0
    for a in range(90, 100):
        for b in range(90, 100):
            sum_digits = ints.sum_digits(a**b)
            max_sum = max(max_sum, sum_digits)
    print(max_sum)


if __name__ == "__main__":
    main()
