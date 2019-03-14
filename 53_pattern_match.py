# coding: utf-8


def pattern_match(s, pattern):
    len_p, len_s = len(pattern), len(s)
    idx_p, idx_s = 0, 0

    while idx_p < len_p and idx_s < len_s:
        if idx_p == len_p - 1 or pattern[idx_p + 1] != '*':
            if pattern[idx_p] == '.':
                idx_p += 1
                idx_s += 1
            elif pattern[idx_p] == s[idx_s]:
                idx_p += 1
                idx_s += 1
            else:
                return False
        else:
            if pattern[idx_p] != s[idx_s] and pattern[idx_p] != '.':
                idx_p += 2
            elif idx_p == len_p - 2 or pattern[idx_p + 2] != pattern[idx_p]:
                if pattern[idx_p] == '.':
                    return True
                while idx_s < len_s and s[idx_s] == pattern[idx_p]:
                    idx_s += 1
                idx_p += 2
            else:
                if pattern[idx_p] == '.':
                    for i in xrange(len_s - idx_s):
                        if pattern_match(pattern[idx_p+2:], s[idx_s+i:]):
                            return True
                    return False
                else:
                    if pattern_match(pattern[idx_p+2:], s[idx_s:]):
                        return True
                    for i in xrange(1, len_s - idx_s):
                        if s[idx_s+i] != pattern[idx_p]:
                            break
                        if pattern_match(pattern[idx_p+2:], s[idx_s+i:]):
                            return True
                    return False

    if idx_p == len_p and idx_s == len_s:
        return True

    return False


if __name__ == '__main__':
    print pattern_match('aaa', 'a.a')
    print pattern_match('aaa', 'ab*ac*a')
    print pattern_match('aaa', 'ab*acc*a')
    print pattern_match('aaa', 'aa.a')
    print pattern_match('aaa', 'ab*a')
    print pattern_match('aaa', 'a.*a')