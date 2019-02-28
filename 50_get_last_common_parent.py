# coding: utf-8


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def get_last_common_parent(root, node_1, node_2):
    res = [None]

    def recursive(node):
        if not node or res[0]:
            return 0

        found_num = recursive(node.left) + recursive(node.right)

        if node == node_1:
            found_num += 1

        if node == node_2:
            found_num += 1

        if found_num == 2 and not res[0]:
            res[0] = node

        return found_num

    recursive(root)

    return res[0]


def gen_tree(arr, idx):
    if idx >= len(arr) or arr[idx] is None:
        return None

    node = TreeNode(arr[idx])
    node.left = gen_tree(arr, 2 * idx + 1)
    node.right = gen_tree(arr, 2 * idx + 2)

    return node


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    root = gen_tree(arr, 0)

    print get_last_common_parent(root, root.left, root.right).val
    print get_last_common_parent(root, root, root.left.left.left).val
    print get_last_common_parent(root, root.left.left, root.left.right).val
    print get_last_common_parent(root, root.left.left.left, root.left.left).val
