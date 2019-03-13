# coding: utf-8


from collections import deque


def max_in_sliding_window(arr, k):
    q = deque()

    for i in xrange(k):
        while len(q) > 0:
            if arr[i] >= arr[q[-1]]:
                q.pop()
            else:
                break
        q.append(i)

    res = []

    for i in xrange(k, len(arr)):
        res += arr[q[0]],
        if i - q[0] >= k:
            q.popleft()

        while len(q) > 0:
            if arr[i] >= arr[q[-1]]:
                q.pop()
            else:
                break
        q.append(i)

    res += arr[q[0]],

    return res


if __name__ == '__main__':
    print max_in_sliding_window([2, 3, 4, 2, 6, 2, 5, 1], 3)
