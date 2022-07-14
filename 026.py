# 26. 删除有序数组中的重复项
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    n = s.removeDuplicates(nums)
    print(nums)
    print(nums[:n])