from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper




def convert_array_to_tree(lst, i, n):
    root = None
    if i > n:
        return root
    if lst[i] is not None:
        root = TreeNode()
        root.left = convert_array_to_tree(lst, 2*i+1, n)
        root.right = convert_array_to_tree(lst, 2*i+2, n)
        root.val = lst[i]
    return root


def pre_order(root):
    if root is not None:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

def post_order(root):
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

def level_order(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)





if __name__ == '__main__':
    lst = [3,9,20,None,None,15,7]

    tree = convert_array_to_tree(lst, 0, len(lst)-1)
    print(tree)
    level_order(tree)


