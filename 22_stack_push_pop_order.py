# coding: utf-8

from collections import deque

def stack_push_pop_order(push_order, pop_order):
    push_order_len, pop_order_len = len(push_order), len(pop_order)
    if push_order_len != pop_order_len:
        return False

    stack = deque()
    push_idx = 0
    for i in xrange(pop_order_len):
        if len(stack) > 0 and stack[-1] == pop_order[i]:
            stack.pop()
        elif push_idx < push_order_len:
            while push_idx < push_order_len and pop_order[i] != push_order[push_idx]:
                stack.append(push_order[push_idx])
                push_idx += 1
            if push_idx == push_order_len:
                return False
            push_idx += 1
        else:
            return False

    return True


if __name__ == "__main__":
    push_order = [1, 2, 3, 4, 5]
    pop_order = [4, 5, 3, 2, 1]
    print stack_push_pop_order(push_order, pop_order)
    
    pop_order = [4, 3, 5, 1, 2]
    print stack_push_pop_order(push_order, pop_order)

    push_order = []
    pop_order = []
    print stack_push_pop_order(push_order, pop_order)
