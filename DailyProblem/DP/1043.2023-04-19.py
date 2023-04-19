from typing import List
'''
1043. 分隔数组以得到最大和
https://leetcode.cn/problems/partition-array-for-maximum-sum/

DP
列出递推关系
dp[i] = max(dp[i], dp[i - j] + j * max(arr[i - j]))
把求max的预先处理，时间复杂度从O(nk^2)降为O(nk)。
'''
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(dp)):
            maxnum = 0
            for j in range(1, k + 1):
                maxnum = max(maxnum, arr[i - j])
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + maxnum * j)
        return dp[-1]
s = Solution()
print(s.maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4))