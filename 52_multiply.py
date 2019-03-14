# coding: utf-8


def multiply(arr):
    length = len(arr)
    left = [1] * length
    right = [1] * length

    pre_sum = arr[0]
    for i in xrange(1, length):
        left[i] = pre_sum
        pre_sum *= arr[i]

    pre_sum = arr[-1]
    for i in xrange(length - 2, -1, -1):
        right[i] = pre_sum
        pre_sum *= arr[i]

    res = [0] * length
    for i in xrange(length):
        res[i] = left[i] * right[i]

    return res


def multiply_contrast(arr):

    def mul(arr):
        res = 1

        for n in arr:
            res *= n

        return res

    length = len(arr)

    zero_num = arr.count(0)
    if zero_num > 1:
        return [0] * length

    if zero_num == 1:
        zero_idx = arr.index(0)
        s = mul(arr[:zero_idx]) * mul(arr[zero_idx+1:])
        return [s if i == zero_idx else 0 for i in xrange(length)]

    s = mul(arr)
    res = [0] * length
    for i in xrange(length):
        res[i] = s / arr[i]

    return res


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    print multiply(arr)
    print multiply_contrast(arr)
    arr = [1, 2, 0, 4, 5, 6]
    print multiply(arr)
    print multiply_contrast(arr)
    arr = [1, 2, 0, 4, 0, 6]
    print multiply(arr)
    print multiply_contrast(arr)
