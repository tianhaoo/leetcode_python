from collections import deque



def trace(func):
    """作为递归函数的装饰器，打印每次调用的参数和返回值"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val} -> ({self.left},{self.right})"




def convert_array_to_tree(lst, i):
    """把数组表示的tree转成TreeNode"""
    root = None
    if i >= len(lst):
        return root
    if lst[i] is not None:
        root = TreeNode()
        root.val = lst[i]
        root.left = convert_array_to_tree(lst, 2*i+1)
        root.right = convert_array_to_tree(lst, 2*i+2)

    return root

def convert_tree_to_array(root):
    """把二叉树转为数组表示，满二叉树"""
    # 求最大深度
    def maxDepth(root):
        def traverse(root):
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            return max(left, right) + 1

        return traverse(root)
    depth = maxDepth(root)
    count = 2 ** depth - 1
    lst = [None for i in range(count)]  # 记录满二叉树的lst

    def traverse(root, lst, i):
        if root is not None:
            lst[i] = root.val
            traverse(root.left, lst, 2*i+1)
            traverse(root.right, lst, 2*i+2)
    traverse(root, lst, 0)

    return lst



def serialize_binary_tree(root):
    if root is None:
        return str([])
    lst = []
    q = deque()
    q.append(root)
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node:
                lst.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                lst.append(None)
    index = len(lst)
    for i in range(len(lst)-1, -1, -1):
        if lst[i] is not None:
            index = i
            break

    return str(lst[:index+1])


def deserialize_binary_tree(data):
    data = data.replace("null", "None")
    lst = eval(data)
    if not lst:
        return None
    root = TreeNode(lst[0])
    q = deque()
    q.append(root)

    i = 1
    while q:
        node = q.popleft()
        if i >= len(lst):
            break
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            q.append(node.left)
        i += 1
        if i >= len(lst):
            break
        if lst[i] is not None:
            node.right = TreeNode(lst[i])
            q.append(node.right)
        i += 1
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


def print_binary_tree(root):

    lst = convert_tree_to_array(root)
    print(lst)
    i = 0
    depth = 1
    lines = []
    while i < len(lst):
        line = []
        for j in range(2**(depth-1)):
            line.append(str(lst[i]))
            i += 1
        depth += 1
        lines.append(" ".join(line))

    for line in lines:
        print(f"| {line.center(100, ' ')} |")



class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def print_linked_list(lst):
    p = lst
    while p:
        print(p.val, end=" ")
        p = p.next
    print()


def serialize_linked_list(lst):
    res = []
    p = lst
    while p:
        res.append(p.val)
        p = p.next
    return res

def deserialize_linked_list(lst):
    if not lst:
        return None
    root = ListNode(lst[0])
    p = root
    for val in lst[1:]:
        p.next = ListNode(val)
        p = p.next
    return root





if __name__ == '__main__':
    # lst = [3,9,20,None,None,15,7, None,None,None,None,8]
    # lst = [2, None, 3, None, 4, None, 5, None, 6]
    lst = [3,9,20,None,None,15,7]
    tree = convert_array_to_tree(lst, 0)
    print(tree)
    print_binary_tree(tree)


