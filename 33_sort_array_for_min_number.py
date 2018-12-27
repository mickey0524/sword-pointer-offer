# coding: utf-8


def sort_array_for_min_number(arr):
    """
    :param arr: 数组
    :return: int
    """
    length = len(arr)
    if length == 1:
        return arr[0]

    arr = [str(n) for n in arr]
    arr.sort(key=lambda x: x[0])

    head = arr[0]
    head_idx = 0

    for idx, n in enumerate(arr):
        if n[0] != head[0]:
            partition(arr, head_idx, idx - 1, 0)
            head = n
            head_idx = idx

    partition(arr, head_idx, length - 1, 0)

    return int(''.join(arr))


def quick_sort(arr, head, tail, bit_idx):
    while head < tail:
        while head < tail and len(arr[head]) != bit_idx + 1 and arr[head][bit_idx + 1] < arr[head][bit_idx]:
            head += 1
        while head < tail and len(arr[tail]) != bit_idx + 1 and arr[tail][bit_idx + 1] >= arr[tail][bit_idx]:
            tail -= 1
        if head == tail:
            break
        arr[head], arr[tail] = arr[tail], arr[head]

    return head


def partition(arr, head, tail, bit_idx):
    if head >= tail:
        return

    idx = quick_sort(arr, head, tail, bit_idx)
    partition(arr, head, idx - 1, bit_idx + 1)
    partition(arr, idx + 1, tail, bit_idx + 1)

    return


if __name__ == '__main__':
    arr = [3, 32, 321, 432, 434, 43, 4]
    print sort_array_for_min_number(arr)
