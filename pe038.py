def main():
    for n in range(9100, 10000):
        s = f"{n*1}{n*2}"
        s_set = set(s)
        if len(s_set) == 9:
            print(s)


if __name__ == "__main__":
    main()
