# coding: utf-8

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_binary_tree(pre_order, in_order):
    length = len(pre_order)

    if length == 0:
        return None

    if length == 1:
        return TreeNode(pre_order[0])

    node = TreeNode(pre_order[0])
    index = None
    for idx, n in enumerate(in_order):
        if n == pre_order[0]:
            node.left = construct_binary_tree(pre_order[1:1+idx], in_order[0:idx])
            node.right = construct_binary_tree(pre_order[1+idx:], in_order[idx+1:])
            break

    return node


def in_resursive(root):
    if not root:
        return
    
    in_resursive(root.left)
    print root.val,
    in_resursive(root.right)


def pre_resursive(root):
    if not root:
        return

    print root.val,
    pre_resursive(root.left)
    pre_resursive(root.right)


if __name__ == "__main__":
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_binary_tree(pre_order, in_order)

    pre_resursive(root)
    print '\n'
    in_resursive(root)
