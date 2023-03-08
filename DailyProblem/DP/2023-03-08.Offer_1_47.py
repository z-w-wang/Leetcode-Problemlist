from typing import List
'''
剑指 Offer 47. 礼物的最大价值

经典二维DP
dp[i][0] = dp[i - 1][0] + grids[i][0]
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grids[i][j]     j > 0

'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[j] = max(dp[j - 1] * (j > 0), dp[j]) + grid[i][j]
        return dp[-1]

s = Solution()
print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))