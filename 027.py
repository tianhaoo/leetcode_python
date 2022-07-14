# 27. 移除元素
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow



if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    n = s.removeElement(nums, val)
    print(nums)
    print(nums[:n])