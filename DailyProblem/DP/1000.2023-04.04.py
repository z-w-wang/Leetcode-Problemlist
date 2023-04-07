from typing import List
from itertools import accumulate
'''
1000. 合并石头的最低成本
https://leetcode.cn/problems/minimum-cost-to-merge-stones/

DP
暴力解法很垃圾，时间复杂度飞起。
三维dp、二维dp见题解。
'''
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        # # 回溯，超时
        n = len(stones)
        if n > 1 and n < k or k != 2 and not n % (k - 1) == 1:
            return -1
        prefix = list(accumulate(stones, initial=0))
        # # 三维DP
        # dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i][1] = 0
        #     prefix[i + 1] = prefix[i] + stones[i]
        # for length in range(2, n + 1):
        #     for left in range(n - length + 1):
        #         right = left + length - 1
        #         for t in range(2, k + 1):
        #             for p in range(left, right, k - 1):
        #                 dp[left][right][t] = min(dp[left][right][t], dp[left][p][1] + dp[p + 1][right][t - 1])              
        #         dp[left][right][1] = min(dp[left][right][1], dp[left][right][k] + prefix[right + 1] - prefix[left])
        # return dp[0][n - 1][1]
        
        #二维dp
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                dp[left][right] = min(dp[left][p] + dp[p + 1][right] for p in range(left, right, k - 1))
                if (right - left) % (k - 1) == 0:
                    dp[left][right] += prefix[right + 1] - prefix[left]
        return dp[0][n - 1]

s = Solution()
print(s.mergeStones([3,5,1,2,6], 3))