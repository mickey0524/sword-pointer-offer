# coding: utf-8


def inverse_pairs(arr):
    length = len(arr)
    if length <= 1:
        return 0, arr

    middle = length / 2
    left_n, left_arr = inverse_pairs(arr[:middle])
    right_n, right_arr = inverse_pairs(arr[middle:])

    pairs = 0
    tmp = []
    left_idx, right_idx = 0, 0
    left_len, right_len = len(left_arr), len(right_arr)
    while left_idx < left_len and right_idx < right_len:
        if left_arr[left_idx] > right_arr[right_idx]:
            pairs += (right_len - right_idx)
            tmp += left_arr[left_idx],
            left_idx += 1
        else:
            tmp += right_arr[right_idx],
            right_idx += 1

    if left_idx < left_len:
        tmp += left_arr[left_idx:]

    elif right_idx < right_len:
        tmp += right_arr[right_idx:]

    return left_n + right_n + pairs, tmp


if __name__ == '__main__':
    print inverse_pairs([7, 5, 6, 4])
    print inverse_pairs([1, 2, 3, 4])
