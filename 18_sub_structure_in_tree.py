# coding: utf-8

class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def sub_structure_in_tree(A, B):
    if not A or not B:
        return False
    
    is_found = False

    if A.val == B.val:
        is_found = resursive(A, B)

    if not is_found:
        is_found = sub_structure_in_tree(A.left, B) or \
            sub_structure_in_tree(A.right, B)
    
    return is_found


def resursive(A, B):
    if not B:
        return True
    
    if not A:
        return False
    
    if A.val != B.val:
        return False
    
    return resursive(A.left, B.left) and \
        resursive(A.right, B.right)


def gen_tree(arr, idx):
    if idx >= len(arr) or arr[idx] is None:
        return None
    
    node = TreeNode(arr[idx])
    node.left = gen_tree(arr, 2 * idx + 1)
    node.right = gen_tree(arr, 2 * idx + 2)

    return node

def in_order_resursive(head):
    if head is None:
        return
    
    print head.val,

    in_order_resursive(head.left)
    in_order_resursive(head.right)

if __name__ == '__main__':
    A = gen_tree([8, 8, 7, 9, 2, None, None, None, None, 4, 7], 0)
    B = gen_tree([8, 9, 2], 0)
    C = gen_tree([8, 9, 3], 0)

    print 'A: ',
    in_order_resursive(A)
    
    print '\nB: ',
    in_order_resursive(B)

    print '\nC: ',
    in_order_resursive(C)
    
    print '\ncompare A and B: ', sub_structure_in_tree(A, B)
    print 'compare A and C: ', sub_structure_in_tree(A, C)
