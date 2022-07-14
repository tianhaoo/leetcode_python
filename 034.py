# 34. 在排序数组中查找元素的第一个和最后一个位置
import math
from typing import List


class Solution:
    def leftBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = math.floor((left+right)/2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def rightBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = math.floor((left+right)/2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            a = self.leftBound(nums, target)
            b = self.rightBound(nums, target)
            return [a, b]
        else:
            return [-1, -1]



if __name__ == '__main__':
    s = Solution()
    nums = [2, 2]
    target = 3
    lst = s.searchRange(nums, target)
    if lst[0] != -1:
        print(nums[lst[0]: lst[1]+1])
    else:
        print("没找到")