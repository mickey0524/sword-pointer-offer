# coding: utf-8


def numbers_appear_once(arr):
    xor = 0
    for n in arr:
        xor ^= n

    base = 1
    while True:
        if base & xor == base:
            break
        base <<= 1

    bit_one, bit_zero = 0, 0
    for n in arr:
        if base & n == base:
            bit_one ^= n
        else:
            bit_zero ^= n

    return bit_one, bit_zero


if __name__ == '__main__':
    arr = [2, 4, 3, 6, 3, 2, 5, 5]
    print numbers_appear_once(arr)
