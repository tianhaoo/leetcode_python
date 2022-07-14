# 3. 无重复字符的最长子串

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        res = 0
        left = right = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            # 经过left收缩之后，此时是没有重复项的
            res = max(res, right-left)
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0
        ma = float("-inf")

        left, right = 0, 0
        while right < len(s):
            right += 1

            # print(s[left:right])
            if len(set(s[left:right])) == right - left and right - left > ma:
                ma = right - left

            # 当有重复的时候，缩
            while len(set(s[left:right])) < right - left:
                left += 1

        return ma


if __name__ == '__main__':
    solution = Solution()
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))
