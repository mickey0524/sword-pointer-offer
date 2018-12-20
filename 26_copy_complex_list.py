# coding: utf-8

class ListNode(object):
    def __init__(self, v):
        self.val = v
        self.next = None
        self.sibling = None


def copy_complex_list(head):
    hash_map = {}
    tmp = head
    res = ListNode(0)
    res_copy = res

    while tmp:
        node = ListNode(tmp.val)
        res.next = node
        res = node
        hash_map[tmp] = node
        tmp = tmp.next

    tmp = head
    while tmp:
        if tmp.sibling:
            hash_map[tmp].sibling = hash_map[tmp.sibling]
        tmp = tmp.next
    
    return res_copy.next


def gen_list(list_len, siblings):
    hash_map = {}

    head = ListNode(-1)
    res = head
    for i in xrange(list_len):
        node = ListNode(i)
        head.next = node
        hash_map[i] = node
        head = node
    
    for (i, j) in siblings:
        hash_map[i].sibling = hash_map[j]

    return res.next


def traverse_list(head):
    siblings = []

    while head:
        print head.val,
        if head.sibling:
            siblings.append((head.val, head.sibling.val))
        head = head.next

    print siblings


if __name__ == "__main__":
    head = gen_list(5, [(0, 2), (1, 4), (3, 1)])
    traverse_list(head)

    head_copy = copy_complex_list(head)
    traverse_list(head_copy)
