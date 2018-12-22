# coding: utf-8

from itertools import permutations


def string_permutation(s):
    return [''.join(t) for t in permutations(s)]


def string_permutation_V1(s):
    length = len(s)
    tmp = [[], [False] * length]

    def resursive(idx, path):
        if idx == length:
            tmp[0] += path,
            return
        
        for i in xrange(length):
            if not tmp[1][i]:
                tmp[1][i] = True
                resursive(idx + 1, path + s[i])
                tmp[1][i] = False
        
    resursive(0, '')

    return tmp[0]


if __name__ == "__main__":
    s = 'abc'
    print string_permutation(s)
    print string_permutation_V1(s)
