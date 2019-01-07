# coding: utf-8


def sort_array_for_min_number(arr):
    """
    :param arr: 数组
    :return: int
    """
    length = len(arr)
    if length == 1:
        return arr[0]

    arr = map(str, arr)

    arr.sort(compare)

    return ''.join(arr)


def compare(a, b):
    len_a, len_b = len(a), len(b)

    if len_a < len_b:
        while len(a) < len_b:
            a += a[-1]
    elif len_a > len_b:
        while len(b) < len_a:
            b += b[-1]

    return -1 if a < b else 1


if __name__ == '__main__':
    arr = [3, 3, 32, 321, 432, 434, 43, 4, 5, 66, 67]
    print sort_array_for_min_number(arr)
