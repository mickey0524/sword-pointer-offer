# coding: utf-8


def number_of_1(n):
    if n < 1:
        return 0
    if n < 10:
        return 1

    s = str(n)
    length = len(s)

    first_bit_sum = pow(10, length - 1) if s[0] > '1' else int(s[1:]) + 1

    other_bit_sum = pow(10, length - 2) * int(s[0]) * (length - 1)

    return first_bit_sum + other_bit_sum + number_of_1(int(s[1:]))


def number_of_1_V1(n):
    res = 0
    for i in xrange(1, n + 1):
        tmp = 0
        while i:
            if i % 10 == 1:
                tmp += 1
            i /= 10
        res += tmp
    return res


if __name__ == "__main__":
    arr = [12, 996, 999, 13451, 24125]
    for n in arr:
        print n, number_of_1(n), number_of_1_V1(n)
