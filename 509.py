# 509. 斐波那契数

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            p1, p2 = 0, 1
            for i in range(2, n+1):
                p1, p2 = p2, p1+p2
        return p2


if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))