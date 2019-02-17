# coding: utf-8


def number_of_k(arr, k):
    length = len(arr)

    head, tail, middle = 0, length - 1, -1

    while head < tail:
        middle = head + (tail - head) / 2
        if arr[middle] == k:
            left, right = middle, middle
            while left >= 0 and arr[left] == k:
                left -= 1
            while right < length and arr[right] == k:
                right += 1
            return right - 1 - left
        elif arr[middle] > k:
            tail = middle
        else:
            head = middle + 1

    return 1 if arr[head] == k else 0


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 3, 3, 4, 5]

    for k in set(arr):
        print number_of_k(arr, k)
    print number_of_k(arr, 6)
    print number_of_k(arr, 0)
