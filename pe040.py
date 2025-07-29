def main():
    digits_placed = 0
    for n in range(1, 1_000_000):
        digit_len = len(str(n))
        if len(str(digits_placed + digit_len)) > len(str(digits_placed)):
            print(digits_placed, n)
        digits_placed += digit_len


if __name__ == "__main__":
    main()
