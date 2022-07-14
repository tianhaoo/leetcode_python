# 76. 最小覆盖子串

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = dict(), dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
        valid = 0  # 记录window里满足需要的字符个数，要满足valid == len(need)
        start, length = 0, float("inf")  # 记录字串的起始索引和长度
        left = right = 0  # 窗口的两端
        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            # 更新窗口数据
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            print(f"window {s[left:right]}")

            while valid == len(need):
                # 窗口此时已经满足了需要
                if right - left < length:
                    # 只要最小的
                    start = left
                    length = right - left

                # 收缩窗口
                c = s[left]
                left += 1
                # 更新窗口数据
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1

        if length == float("inf"):
            return ""
        else:
            return s[start:start+length]









if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "aa"
    print(solution.minWindow(s, t))
