# 297. 二叉树的序列化与反序列化


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

import Utils
from Utils import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
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


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
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




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == '__main__':

    s = "[2,null,3,null,4,null,5,null,6]"
    # lst = [1, 2, 3, None, None, 4, 5]
    # lst = []
    print(s)
    root = Utils.deserialize_binary_tree(s)
    Utils.print_binary_tree(root)

    b = Utils.serialize(root)
    print(b)