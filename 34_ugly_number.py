# coding: utf-8


def ugly_number(n):
    if n <= 0:
        return None

    nums = [1]

    base_2, base_3, base_5 = 0, 0, 0

    for _ in xrange(1, n):
        min_base = min(nums[base_2] * 2, nums[base_3] * 3, nums[base_5] * 5)
        nums += min_base,
        while nums[base_2] * 2 <= min_base:
            base_2 += 1
        while nums[base_3] * 3 <= min_base:
            base_3 += 1
        while nums[base_5] * 5 <= min_base:
            base_5 += 1

    return nums[-1]


def ugly_number_v1(n):
    if n <= 0:
        return None

    cnt_s, i = 1, 2
    while cnt_s < n:
        if is_ugly_number(i):
            cnt_s += 1
        i += 1

    return i - 1


def is_ugly_number(n):
    if n == 0:
        return False

    while n % 2 == 0:
        n /= 2

    while n % 3 == 0:
        n /= 3

    while n % 5 == 0:
        n /= 5

    return n == 1


if __name__ == '__main__':
    print ugly_number(100), ugly_number_v1(100)
    print ugly_number(500), ugly_number_v1(500)
    print ugly_number(1000), ugly_number_v1(1000)
