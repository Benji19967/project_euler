def main():
    _sum = 0
    for n in range(1, 1001):
        _sum += n**n
    print(_sum % 10000000000)


if __name__ == "__main__":
    main()
