# coding: utf-8

def more_than_half_number(arr):
    hash_map = {}
    threshold = len(arr) / 2

    for n in arr:
        hash_map[n] = hash_map.get(n, 0) + 1
        if hash_map[n] > threshold:
            return n
    
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print more_than_half_number(arr)