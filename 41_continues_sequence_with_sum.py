# coding: utf-8


def continues_sequence_with_sum(n):
    if n < 3:
        return [[]]

    s = 0
    path = []

    for i in xrange(1, 3):
        s += i
        path += i,
        if s >= n:
            break

    if s == n:
        return [path]

    num = path[-1]
    res = []

    while True:
        while s > n:
            s -= path[0]
            path.pop(0)
        if s == n:
            res += path[:],
        if len(path) == 1:
            break
        num += 1
        s += num
        path += num,

    return res


if __name__ == '__main__':
    for i in xrange(3, 20):
        print i, continues_sequence_with_sum(i)
