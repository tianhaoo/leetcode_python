# 104. 二叉树的最大深度
from Utils import convert_array_to_tree


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root, depth, depths):
            if root is not None:
                # 在前序位置 +1
                depth += 1
                # 如果是叶子节点，记录当前的高度
                if root.left is None and root.right is None:
                    depths.append(depth)
                traverse(root.left, depth, depths)
                traverse(root.right, depth, depths)
                # 在后序位置 -1
                depth -= 1

        depths = []
        traverse(root, 0, depths)
        if depths:
            return max(depths)
        else:
            return 0

    def maxDepth2(self, root):
        def traverse(root):
            if root is None:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            return max(left, right) + 1
        return traverse(root)


if __name__ == '__main__':
    lst = [3,9,20,None,None,15,7]
    root = convert_array_to_tree(lst, 0, len(lst)-1)
    s = Solution()
    print(s.maxDepth2(root))