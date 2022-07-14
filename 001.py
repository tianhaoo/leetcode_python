# 1. 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = [(elem, i) for i, elem in enumerate(nums)]
        lst.sort(key=lambda x: x[0])
        left, right = 0, len(nums)-1
        while left < right:
            temp = lst[left][0] + lst[right][0]
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
            elif temp == target:
                return [lst[left][1], lst[right][1]]
        return []



if __name__ == '__main__':
    s = Solution()
    nums = [2, 11, 7, 15]
    target = 9
    print(s.twoSum(nums,target))

