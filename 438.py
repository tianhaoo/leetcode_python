# 438. 找到字符串中所有字母异位词
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, need = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        res = []
        valid = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res



if __name__ == '__main__':
    solution = Solution()
    s = "abab"
    p = "ab"
    print(solution.findAnagrams(s, p))
