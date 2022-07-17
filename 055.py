# 55. 跳跃游戏
from typing import List


class Solution:
    def __init__(self):
        self.found = False

    def canJump(self, nums: List[int]) -> bool:
        def traverse(x):
            if x == len(nums)-1:
                self.found = True
            elif x >= len(nums):
                return
            else:
                step = nums[x]
                for y in range(x+1, x+1+step):
                    traverse(y)
        traverse(0)
        return self.found





if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    # nums = [0, 2, 3]
    nums = [0]
    print(s.canJump(nums))