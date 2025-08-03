def digits_to_int(digits: list):
    num = 0
    for d in digits:
        num = num * 10 + d
    return num
