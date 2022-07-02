# 111. 二叉树的最小深度
from collections import deque

from Utils import TreeNode, convert_array_to_tree, level_order, print_binary_tree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """广度优先搜索，找到一个叶子节点后就返回"""
        depth = 0
        q = deque()
        q.append(root)
        while q:
            sz = len(q)
            for i in range(sz):
                depth += 1
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return depth



if __name__ == '__main__':
    # lst = [3,9,20,None,None,15,7]
    lst = [2, None, 3, None, 4, None, 5, None, 6]

    root = convert_array_to_tree(lst, 0)
    print_binary_tree(root)

    s = Solution()
    print(s.minDepth(root))



