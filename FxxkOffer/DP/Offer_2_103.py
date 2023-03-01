from typing import List
'''
剑指 Offer II 103. 最少的硬币数目 == 322

完全背包，拿就完事儿了。
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]

s = Solution()
print(s.coinChange([1, 2, 5], 11))