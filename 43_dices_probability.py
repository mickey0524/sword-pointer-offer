# coding: utf-8


def dices_probability(n):
    if n < 1:
        return
    times = [1] * 6
    for i in xrange(1, n):
        tmp = [0] * ((i + 1) * 6)
        for j in xrange(i, (i + 1) * 6):
            for k in xrange(j - i, max(-1, j - i - 6), -1):
                if k < len(times):
                    tmp[j] += times[k]
        times = tmp[i:]

    s = sum(times)

    begin = n
    for n in times:
        print '%d: %d/%d' % (begin, n, s)
        begin += 1


if __name__ == '__main__':
    for i in xrange(3):
        dices_probability(i)
