# 278. 第一个错误的版本


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math

bad = 1

def isBadVersion(v):
    if v >= bad:
        return True
    return False




class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        left, right = 1, n
        while left <= right:
            mid = math.floor((left+right)/2)
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    n = 1
    print(s.firstBadVersion(n))
