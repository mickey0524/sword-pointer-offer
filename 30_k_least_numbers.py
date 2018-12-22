# coding: utf-8


def k_least_numbers(arr, k):
    if k < 0:
        return None

    length = len(arr)

    if length <= k:
        return arr

    head, tail = 0, length - 1
    n = (arr[0] + arr[-1]) / 2
    idx = partition(arr, head, tail, n)

    while idx != k - 1:
        if idx > k - 1:
            tail = idx - 1
            idx = partition(arr, head, tail, n)
        else:
            head = idx + 1
            idx = partition(arr, head, tail, n)
    return arr[:idx + 1]

    
def partition(arr, head, tail, k):
    while head < tail:
        while head < tail and arr[head] <= k:
            head += 1
        while head < tail and arr[tail] > k:
            tail -= 1
        if head < tail:
            arr[head], arr[tail] = arr[tail], arr[head]
    
    return head


def k_least_numbers_V1(arr, k):
    if k < 0:
        return None

    length = len(arr)

    if length <= k:
        return arr
    
    heap = [0] * k
    for i in xrange(k):
        heap[i] = arr[i]
        up(heap, i)
        
    for n in arr[k:]:
        if n < heap[0]:
            heap[0] = n
            down(heap, 0, k)
    
    return heap


def up(heap, idx):
    while True:
        parent_idx = (idx - 1) / 2
        if idx == parent_idx or parent_idx < 0 or heap[idx] <= heap[parent_idx]:
            break
        heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        idx = parent_idx
    

def down(heap, i, j):
    while True:
        idx = 2 * i + 1
        if idx >= j:
            break

        if idx + 1 < j and heap[idx + 1] > heap[idx]:
            idx += 1
        
        if heap[i] >= heap[idx]:
            break

        heap[i], heap[idx] = heap[idx], heap[i]
        i = idx

 
if __name__ == "__main__":
    arr, k = [4, 5, 1, 6, 2, 7, 3, 8], 6
    print k_least_numbers_V1(arr, k)
    print k_least_numbers(arr, k)
