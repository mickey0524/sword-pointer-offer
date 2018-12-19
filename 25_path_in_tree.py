# coding: utf-8


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def path_in_tree(root, target):
    def resursive(node, cnt_sum, path):
        if not node:
            return

        if not node.left and not node.right:
            if cnt_sum + node.val == target:
                print path + [node.val]
            return

        if node.left:
            resursive(node.left, cnt_sum + node.val, path + [node.val])
        if node.right:
            resursive(node.right, cnt_sum + node.val, path + [node.val])

    resursive(root, 0, [])

def gen_tree(arr, idx):
    if idx >= len(arr) or arr[idx] is None:
        return None

    node = TreeNode(arr[idx])
    node.left = gen_tree(arr, 2 * idx + 1)
    node.right = gen_tree(arr, 2 * idx + 2)

    return node

if __name__ == "__main__":
    arr = [10, 5, 12, 4, 7]
    tree = gen_tree(arr, 0)
    path_in_tree(tree, 22)
