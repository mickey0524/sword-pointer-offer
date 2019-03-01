# coding: utf-8


class ListNode(object):

    def __init__(self, v):
        self.val = v
        self.next = None


def delete_duplication_v1(head):
    """
    允许修改链表节点的 val
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    r, pre_val = head, '#'
    l = ListNode('#')
    l.next = head

    while r:
        if r.val != pre_val:
            l = l.next
            l.val = r.val

        pre_val = r.val
        r = r.next

    l.next = None

    return head


def delete_duplication_v2(head):
    """
    只能修改链表节点的 next
    :param head:
    :return:
    """
    if not head or not head.next:
        return head

    l, r = head, head.next

    while r:
        if r.val == l.val:
            while r and r.val == l.val:
                r = r.next
            l.next = r
        else:
            l = r
            r = r.next

    return head


def print_list(head):
    while head:
        print head.val
        head = head.next


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 4, 4, 5]
    # arr = [1, 2, 3]
    # arr = [1, 1, 1, 1, 1, 1]
    # arr = [1]
    for idx, n in enumerate(arr):
        arr[idx] = ListNode(n)

    for i in xrange(len(arr) - 1):
        arr[i].next = arr[i + 1]

    print_list(delete_duplication_v1(arr[0]))
    print '\n'
    print_list(delete_duplication_v2(arr[0]))