# coding: utf-8

class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def left_2_right(root):
    if not root:
        return
    
    left_2_right(root.left)
    print root.val,
    left_2_right(root.right)


def right_2_left(root):
    if not root:
        return
    
    right_2_left(root.right)
    print root.val,
    right_2_left(root.left)


def gen_tree(arr, idx):
    if idx >= len(arr) or arr[idx] is None:
        return None

    node = TreeNode(arr[idx])
    node.left = gen_tree(arr, 2 * idx + 1)
    node.right = gen_tree(arr, 2 * idx + 2)

    return node


def mirror_of_binary_tree(root):
    if not root:
        return None
    
    node = TreeNode(root.val)
    node.left = mirror_of_binary_tree(root.right)
    node.right = mirror_of_binary_tree(root.left)

    return node


if __name__ == "__main__":
    arr = [8,6,10,5,7,9,11]    
    root = gen_tree(arr, 0)
    left_2_right(root)
    print '\n'
    right_2_left(root)
    print '\n'
    left_2_right(mirror_of_binary_tree(root))
