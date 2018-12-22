# coding: utf-8

class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def convert_binary_search_tree(root):
    tmp = [None, None]
    def resursive(root):
        if not root:
            return
        
        resursive(root.left)
        if tmp[0] is not None:
            tmp[0].next = root
            root.pre = tmp[0]
        else:
            tmp[1] = root
        tmp[0] = root
        resursive(root.right)

    resursive(root)

    return tmp[1]

def gen_tree(arr, idx):
    if idx >= len(arr) or arr[idx] is None:
        return None

    node = TreeNode(arr[idx])
    node.left = gen_tree(arr, 2 * idx + 1)
    node.right = gen_tree(arr, 2 * idx + 2)

    return node


def inorder_traverse(root):
    if not root:
        return
    
    inorder_traverse(root.left)
    print root.val,
    inorder_traverse(root.right)


def traverse_double_link_list(head):
    while head:
        print head.val,
        if not hasattr(head, 'next'):
            break
        head = head.next
    
    while head:
        print head.val,
        if not hasattr(head, 'pre'):
            break
        head = head.pre


if __name__ == "__main__":
    tree = [10, 6, 14, 4, 8, 12, 16]
    tree = gen_tree(tree, 0)
    inorder_traverse(tree)
    print '\n'
    head = convert_binary_search_tree(tree)
    traverse_double_link_list(head)
