# coding: utf-8


def add(a, b):
    sum = a ^ b
    carry = (a & b) << 1

    while carry != 0:
        sum_tmp = sum ^ carry
        carry_tmp = (sum & carry) << 1
        sum, carry = sum_tmp, carry_tmp

    return sum


if __name__ == '__main__':
    print add(5, 17)
    print add(142, 5312)