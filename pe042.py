# Note: largest sum of words is 192


def generate_triangle_numbers(max_num: int):
    triangle_numbers = set([1])
    curr_num = 1
    for adder in range(2, 100):
        curr_num += adder
        triangle_numbers.add(curr_num)
        if curr_num > max_num:
            break
    return triangle_numbers


def read_words():
    with open("data/0042_words.txt") as f:
        words_str = f.read()
    words_str = words_str.translate(str.maketrans("", "", '"'))
    words = words_str.split(",")
    return words


def main():
    words = read_words()
    triangle_numbers = generate_triangle_numbers(192)

    count = 0
    for word in words:
        _sum_word = 0
        for c in word:
            position = ord(c) - ord("A") + 1
            _sum_word += position
        if _sum_word in triangle_numbers:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
