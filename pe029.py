def main():
    distinct_nums = set()
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_nums.add(a**b)
    print(len(distinct_nums))


if __name__ == "__main__":
    main()
