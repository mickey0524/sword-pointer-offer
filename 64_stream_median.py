# coding: utf-8

import heapq
from random import randint


min_heap, max_heap = [], []


def stream_median(num):
    if len(min_heap) == 0:
        heapq.heappush(min_heap, -num)
        return num

    if num >= -min_heap[0]:
        heapq.heappush(max_heap, num)
    else:
        heapq.heappush(min_heap, -num)

    min_heap_len, max_heap_len = len(min_heap), len(max_heap)

    if min_heap_len - max_heap_len == 2:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        min_heap_len -= 1
        max_heap_len += 1

    elif max_heap_len - min_heap_len == 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if min_heap_len == max_heap_len:
        return (-min_heap[0] + max_heap[0]) / 2

    return -min_heap[0]


if __name__ == '__main__':
    nums = []
    for _ in xrange(10):
        n = randint(1, 100)
        nums += n,
        nums.sort()
        print nums,
        print stream_median(n)
