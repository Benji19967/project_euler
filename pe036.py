def is_palindromic(s):
    i = 0
    j = len(s) - 1
    while j > i:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    _sum = 0
    for n in range(1, 1_000_000):
        binary = "{0:b}".format(n)
        decimal = str(n)
        if is_palindromic(binary) and is_palindromic(decimal):
            print(decimal, binary)
            _sum += n
    print(_sum)


if __name__ == "__main__":
    main()
