# coding: utf-8


def greatest_sum_of_subarray(arr):
    res, tmp = float('-inf'), float('-inf')    
    for n in arr:
        if tmp < 0:
            tmp = n
        else:
            tmp += n
        if tmp > res:
            res = tmp
    
    return res

if __name__ == "__main__":
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print greatest_sum_of_subarray(arr)