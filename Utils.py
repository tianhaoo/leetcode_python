
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


def traverse(root):
    if root is not None:
        print(root.val)
        traverse(root.left)
        traverse(root.right)


if __name__ == '__main__':
    lst = [3,9,20,None,None,15,7]

    tree = convert_array_to_tree(lst, 0, len(lst)-1)
    print(tree)
    traverse(tree)


