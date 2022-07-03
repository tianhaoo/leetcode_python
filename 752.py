# 752. 打开转盘锁
from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.deadends = None
        self.visited = None

    def up(self, s, i):
        if s[i] == '9':
            return s[:i] + '0' + s[i+1:]
        else:
            return s[:i] + str(int(s[i])+1) + s[i+1:]

    def down(self, s, i):
        if s[i] == '0':
            return s[:i] + '9' + s[i+1:]
        else:
            return s[:i] + str(int(s[i])-1) + s[i+1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        self.visited = set()
        self.deadends = set(deadends)
        q = deque()
        q.append('0000')

        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                s = q.popleft()
                if s == target:
                    return depth
                if s in self.visited or s in self.deadends:
                    continue
                self.visited.add(s)

                for j in range(4):
                    s_up = self.up(s, j)
                    s_down = self.down(s, j)
                    q.append(s_up)
                    q.append(s_down)

            depth += 1
        # 遍历完了还没有那就是无解
        return -1


if __name__ == '__main__':
    s = Solution()
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # target = "0202"
    # deadends = ["8888"]
    # target = "0009"
    # deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    # target = "8888"

    deadends = []
    target = '0000'


    print(s.openLock(deadends, target))