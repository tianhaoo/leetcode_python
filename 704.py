# 704. 二分查找
import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = math.floor((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1



if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 5
    n = s.search(nums, target)
    if n != -1:
        print(nums[n], target)
    else:
        print("没找到")