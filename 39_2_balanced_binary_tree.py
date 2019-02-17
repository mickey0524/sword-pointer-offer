# coding: utf-8


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def balanced_binary_tree(root):
    res = [None]

    def recursive(node):
        if not node:
            return 0

        left = recursive(node.left)
        right = recursive(node.right)
        if abs(left - right) > 1:
            res[0] = False

        return max(left, right) + 1

    recursive(root)

    return True if res[0] is None else False


if __name__ == '__main__':
    print balanced_binary_tree(None)
    root = TreeNode(1)
    print balanced_binary_tree(root)
    left = TreeNode(2)
    root.left = left
    print balanced_binary_tree(root)
    left_left = TreeNode(4)
    left.left = left_left
    print balanced_binary_tree(root)
    right = TreeNode(3)
    root.right = right
    print balanced_binary_tree(root)
