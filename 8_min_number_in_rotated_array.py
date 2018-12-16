# coding: utf-8


def get_min_number_in_rotated_array(arr):
    length = len(arr)
    if length == 0:
        raise IndexError("no element in arr")
    
    if length == 1 or arr[0] < arr[-1]:
        return arr[0]

    head, tail, middle = 0, length - 1, None

    while head < tail:
        middle = head + (tail - head) / 2
        if arr[middle] <= arr[-1]:
            tail = middle
        elif arr[middle] > arr[-1]:
            head = middle + 1

    return arr[tail]

if __name__ == "__main__":
    print get_min_number_in_rotated_array([1])
    print get_min_number_in_rotated_array([1, 1, 2, 3, 3, 4, 5])
    print get_min_number_in_rotated_array([2, 3, 4, 5, 1])
    print get_min_number_in_rotated_array([3, 4, 5, 5, 1, 2])
    print get_min_number_in_rotated_array([3, 4, 5, 1, 2, 3])
    print get_min_number_in_rotated_array([5, 1, 1, 2, 3, 4, 4])
    print get_min_number_in_rotated_array([3, 4, 5, 5, 6, 6, 1, 2, 2, 3])
