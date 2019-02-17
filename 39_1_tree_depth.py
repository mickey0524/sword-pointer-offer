# coding: utf-8


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def tree_depth(root):
    if not root:
        return 0

    return max(tree_depth(root.left), tree_depth(root.right)) + 1
