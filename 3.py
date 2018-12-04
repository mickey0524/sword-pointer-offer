# coding: utf-8
# 这道题的关键点是矩形的左上角是矩形中最小的数

def search_in_two_dim_arr(arr, target):
    row = len(arr)
    if row == 0:
        return False
    col = len(arr[0])

    row_idx, col_idx = 0, col - 1

    while True:
        while col_idx >= 0 and arr[row_idx][col_idx] > target:
            col_idx -= 1
        if col_idx < 0:
            return False
        while row_idx < row and arr[row_idx][col_idx] < target:
            row_idx += 1
        if row_idx == row:
            return False
        if arr[row_idx][col_idx] == target:
            return True

    return False

if __name__ == "__main__":
    arr = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15],
    ]
    for row in arr:
        for i in row:
            print i, search_in_two_dim_arr(arr, i)

    for i in [5, 16, 0]:
        print i, search_in_two_dim_arr(arr, i) 