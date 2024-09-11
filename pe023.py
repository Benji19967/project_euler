import math


def find_proper_divisors(num: int) -> list[int]:
    proper_divisors = [1]
    sqrt_n = math.floor(math.sqrt(num))
    for x in range(2, sqrt_n + 1):
        if num % x == 0:
            proper_divisors.extend(set([x, num // x]))
    return sorted(proper_divisors)


def is_abundant(num: int) -> bool:
    return sum(find_proper_divisors(num)) > num


def exists_two_sum(nums: list[int], target: int) -> list[int]:
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return sorted([num, complement])
        if 2 * num == target:
            return [num, num]
        seen.add(num)
    return []


def tests():
    assert find_proper_divisors(4) == [1, 2]
    assert find_proper_divisors(12) == [1, 2, 3, 4, 6]
    assert find_proper_divisors(28) == [1, 2, 4, 7, 14]

    assert is_abundant(12)
    assert not is_abundant(28)

    assert exists_two_sum([1, 2, 3], 5) == [2, 3]
    assert exists_two_sum([1, 2, 3], 6) == [3, 3]
    assert exists_two_sum([1, 2, 3], 1) == []
    assert exists_two_sum([1, 2, 3], 7) == []


def main():
    MAX_NUM = 28_123
    _sum = 0
    abundant_numbers = [num for num in range(1, MAX_NUM + 1) if is_abundant(num)]

    # print(abundant_numbers)

    for target in range(MAX_NUM + 1):
        two_sum = exists_two_sum(abundant_numbers, target)
        if not two_sum:
            _sum += target
        # else:
        #     print(target, two_sum)
    print(_sum)


if __name__ == "__main__":
    tests()

    main()
