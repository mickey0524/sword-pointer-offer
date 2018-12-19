# coding: utf-8


def print_matrix(arr):
    row = len(arr)
    if row == 0:
        return
    col = len(arr[0])

    left, right = 0, col - 1
    top, bottom = 0, row - 1

    while left <= right and top <= bottom:
        for i in xrange(left, right + 1):
            print arr[top][i],
        
        for i in xrange(top + 1, bottom + 1):
            print arr[i][right],
        
        if right > left and bottom > top:
            for i in xrange(right - 1, left - 1, -1):
                print arr[bottom][i],

            for i in xrange(bottom - 1, top, -1):
                print arr[i][left],
        
        left += 1
        top += 1
        right -= 1
        bottom -= 1

if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    print_matrix(arr)
    print '\n'

    arr = [[1, 2, 3, 4]]
    print_matrix(arr)
    print '\n'

    arr = [
        [1],
        [2],
        [3],
        [4],
    ]
    print_matrix(arr)
    print '\n'

    arr = [[1]]
    print_matrix(arr)
    print '\n'
