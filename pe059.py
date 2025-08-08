import itertools
import string

"""
Brute force solution -- could be improved by looking for most common chars in ciphers
and matching to most common english characters, such as ' ' or 'e'
"""

CIPHERS_FILENAME = "./data/0059_cipher.txt"


def ascii_code_to_text(ascii_code: int) -> str:
    return chr(ascii_code)


def get_cipher():
    cipher = []
    with open(CIPHERS_FILENAME, "r") as f:
        s = f.read()
        for c in s.strip().split(","):
            cipher.append(int(c))

    return cipher


def possible_keys() -> list[tuple[str, str, str]]:
    keys = []
    for chars in itertools.combinations_with_replacement(string.ascii_lowercase, 3):
        for key in itertools.permutations(chars):
            keys.append(key)
    return keys


def main():
    ENGLISH_WORDS = set()
    with open("/usr/share/dict/words", "r") as f:
        for line in f:
            ENGLISH_WORDS.add(line.strip())

    cipher = get_cipher()

    for key in possible_keys():
        chars_list = []
        for c, key_letter in zip(cipher, itertools.cycle(key)):
            decrypted_char = c ^ ord(key_letter)
            char = ascii_code_to_text(decrypted_char)
            chars_list.append(char)
        chars = "".join(chars_list)
        words_split = chars.split(" ")
        if len(words_split) > 20:
            count = 0
            for word in words_split[:10]:
                if word in ENGLISH_WORDS:
                    count += 1
            if count > 5:
                print(words_split)
                print(len(words_split))
                print(sum((ord(c) for c in chars)))


if __name__ == "__main__":
    main()
