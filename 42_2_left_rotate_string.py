# coding: utf-8


def left_rotate_string(s, n):
    if n < 0:
        return s

    length = len(s)
    n %= length

    if n == 0:
        return s

    return s[n:] + s[:n]


if __name__ == '__main__':
    s = "abcdefg"
    for i in xrange(1, 2 * len(s)):
        print i, left_rotate_string(s, i)
