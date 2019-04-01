# coding: utf-8


def decode_string(s):
    res = ''
    idx = 0
    length = len(s)

    while idx < length:
        ch = s[idx]
        if ch.isdigit():
            i = idx + 1
            while s[i].isdigit():
                i += 1
            num = int(s[idx:i])
            if s[-1] == ']':
                inner_s = decode_string(s[i+1:-1])
                res += (num * inner_s)
                break
            else:
                j = length - 1
                while s[j] != ']':
                    j -= 1
                inner_s = decode_string(s[i+1:j])
                res += (num * inner_s)
                idx = j

        elif ch.isalpha():
            res += ch

        idx += 1

    return res


if __name__ == '__main__':
    print decode_string('e3[2[abc]gh]')
    print decode_string('e9[xyz]')
