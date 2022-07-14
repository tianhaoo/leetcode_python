# 15. 三数之和
from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for a_index, a in enumerate(nums):
            if a_index >= 1 and a == nums[a_index-1]:  # 如果跟上一个元素相同就continue
                continue
            res = self.twoSum(nums, 0-a)
            if res:
                for lst in res:
                    b_index, c_index = lst[0], lst[1]
                    b, c = nums[b_index], nums[c_index]
                    if a_index != b_index and a_index != c_index:
                        ans.add(tuple(sorted([a, b, c])))

        return [list(lst) for lst in ans]







    def twoSum(self, lst: List[int], target) -> List[List[int]]:
        """数组有序，元素可能有重复"""
        left, right = 0, len(lst) - 1
        res = []
        while left < right:
            temp = lst[left] + lst[right]
            if temp < target:
                left += 1
                # 一直加到没有重复了为止
                while left <= len(lst)-2 and lst[left-1] == lst[left]:
                    left += 1
            elif temp > target:
                right -= 1
                # 一直减到没有重复了为止
                while right >= 1 and lst[right] == lst[right+1]:
                    right -= 1
            elif temp == target:
                # left和right要往中间移动，直到没有重复元素了为止
                while left <= len(lst)-2 and lst[left] == lst[left+1]:
                    left += 1
                while right >= 1 and lst[right] == lst[right-1]:
                    right -= 1
                res.append([left, right])
                left += 1
                right -= 1
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [0,0,0]
    print(s.twoSum(nums, 0))
