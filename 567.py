# 567. 字符串的排列

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, need = {}, {}
        valid = 0
        left, right = 0, 0
        for c in s1:
            need[c] = need.get(c, 0) + 1
        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            print(f"window {s2[left:right]}")

            # 左边收缩的条件
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                c = s2[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False





    def checkInclusion2(self, s1: str, s2: str) -> bool:
        window, need = {}, {}
        valid = 0  # 记录找到的个数，需要valid==len(need)
        start, length = 0, float("inf")
        left, right = 0, 0

        # 更新need
        for c in s1:
            need[c] = need.get(c, 0) + 1

        while right < len(s2):
            # 扩大窗口
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                # 这时就是找到了一个合法的窗口，记录其信息
                current_length = right - left
                if current_length < length:
                    start = left
                    length = current_length

                # 收缩窗口
                c = s2[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        if length == len(s1):
            return True
        else:
            return False




if __name__ == '__main__':
    s = Solution()
    s1 = "ab"
    s2 = "eidbdaaooo"
    print(s.checkInclusion(s1, s2))