# coding: utf-8


def delete_number(s, n):

    for _ in xrange(n):
        cur_len = len(s)
        i = 0
        while i < cur_len - 1:
            if s[i + 1] < s[i]:
                break
            i += 1
        s = s[0:i] + s[i+1:]
        if s == '':
            return 0
        cur_len -= 1
        if s[0] == '0':
            i = 1
            while i < cur_len and s[i] == '0':
                i += 1
            s = s[i:]
            if s == '':
                return 0

    return int(s)


if __name__ == '__main__':
    print delete_number('987132', 4)
    print delete_number('1000230', 5)
