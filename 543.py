# 543. 二叉树的直径


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import Utils


class Solution(object):

    def __init__(self):
        self.m = -1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(root):
            if root is None:
                return 0
            left_depth = traverse(root.left)
            right_depth = traverse(root.right)
            self.m = max(self.m, left_depth+right_depth+1)
            return max(left_depth, right_depth) + 1

        traverse(root)

        return self.m-1



if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    root = Utils.convert_array_to_tree(lst, 0, len(lst)-1)
    # Utils.traverse(root)
    s = Solution()
    print(s.diameterOfBinaryTree(root))