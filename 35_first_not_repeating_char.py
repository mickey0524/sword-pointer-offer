# coding: utf-8


from collections import OrderedDict


def first_not_not_repeating_number(s):
    hash_map = OrderedDict()
    for ch in s:
        cnt_num = hash_map.get(ch, 0)
        hash_map[ch] = cnt_num + 1

    for k, v in hash_map.iteritems():
        if v == 1:
            return k

    return None


if __name__ == '__main__':
    print first_not_not_repeating_number("abaccdeff")