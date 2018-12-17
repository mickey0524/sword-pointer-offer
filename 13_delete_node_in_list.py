# coding: utf-8

from random import randint

class ListNode(object):
    def __init__(self, v):
        self.val = v
        self.next = None

def delete_node_in_list(target):
    if not target:
        return

    if not target.next:
        target = None
        print target
        return
    
    target.val = target.next.val
    target.next = target.next.next

def resursive_node_list(head):
    while head:
        print head.val,
        head = head.next
    
    return


if __name__ == '__main__':
    value_list = [1, 7, 3, 6, 5]
    rand_num = randint(1, 6)
    head = ListNode(0)
    tmp = head
    target = None

    for idx, v in enumerate(value_list):
        node = ListNode(v)
        if idx + 1 == rand_num:
            target = node
        tmp.next = node
        tmp = node
    
    print target.val if target else None
    delete_node_in_list(target)

    resursive_node_list(head.next)
