# coding: utf-8


class ListNode(object):

    def __init__(self, v):
        self.val = v
        self.next = None


def meeting_node(head):
    if head.next == head:
        return head

    one_pass, two_pass = head.next, head.next.next
    while one_pass != two_pass:
        one_pass = one_pass.next
        two_pass = two_pass.next.next

    ring_len = 1
    one_pass = one_pass.next
    while one_pass != two_pass:
        ring_len += 1
        one_pass = one_pass.next

    l, r = head, head

    for _ in xrange(ring_len):
        r = r.next

    while l != r:
        l = l.next
        r = r.next

    return l


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]

    for idx, n in enumerate(arr):
        arr[idx] = ListNode(n)

    for i in xrange(len(arr) - 1):
        arr[i].next = arr[i + 1]

    arr[-1].next = arr[2]

    print meeting_node(arr[0]).val
