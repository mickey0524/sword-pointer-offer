# coding: utf-8


def transform_10_base_to_2_base(N):
    if N == 0:
        return '0'

    symbol = 1
    if N < 0:
        N = -N
        symbol = -1

    res = ''

    while N != 0:
        if N % 2 == 1:
            res = '1' + res
            N -= 1
        else:
            res = '0' + res
        N /= 2

    if symbol == -1:
        res = res.zfill(32)
        l = ['1' if ch == '0' else '0' for ch in res]
        res = int(''.join(l)) + 1
        return str(res)

    return res


def equal(a, b):
    return a == b


if __name__ == '__main__':
    print equal(transform_10_base_to_2_base(9), bin(9)[2:])
    print equal(transform_10_base_to_2_base(32), bin(32)[2:])
    print equal(transform_10_base_to_2_base(142), bin(142)[2:])
    print equal(transform_10_base_to_2_base(15352), bin(15352)[2:])
    print transform_10_base_to_2_base(-4123)


