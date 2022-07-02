# 322. 零钱兑换


class Solution:
    def __init__(self):
        self.memo = dict()

    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount in self.memo.keys():
            return self.memo[amount]
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            minimum = float('inf')
            for coin in coins:
                sub_problem = self.coinChange(coins, amount-coin)
                if sub_problem != -1:
                    minimum = min(minimum, sub_problem + 1)
            res = minimum if minimum != float('inf') else -1
            self.memo[amount] = res
            print(self.memo)
            return res

    def coinChange2(self, coins: list[int], amount: int) -> int:
        lst = [float('inf') for i in range(amount + 1)]
        lst[0] = 0
        for a in range(1, len(lst)):
            for coin in coins:
                if a-coin < 0:
                    continue
                else:
                    print(a, lst)
                    lst[a] = min(lst[a], lst[a-coin] + 1)
        return lst[amount] if lst[amount] != float('inf') else -1





if __name__ == '__main__':
    s = Solution()
    print(s.coinChange2([2, 5, 10, 1], 27))