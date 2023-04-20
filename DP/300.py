from typing import List
from bisect import bisect_left
'''
300. 最长递增子序列
https://leetcode.cn/problems/longest-increasing-subsequence/.

DP or Greedy+BiSearch

DP
dp[i]为nums[: i + 1]中，末尾为nums[i]的最长递增子序列。
初始时dp[i] = 1，即至少有其本身的元素组成子序列。
对于0 <= j < i，如果有nums[j] < nums[i]，那么末尾为nums[i]的递增子序列可由末尾为nums[j]的最长子序列加上nums[i]构成。
有转移方程dp[i] = max(dp[i], dp[j] + 1) if nums[j] < nums[i]
时间复杂度O(n^2)

Greedy+BiSearch
见题解，优胜劣汰。
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)
        q = []
        for num in nums:
            idx = bisect_left(q, num)
            if idx == len(q):
                q.append(num)
            else:
                q[idx] = num
        return len(q)