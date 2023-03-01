from typing import List
'''
剑指 Offer II 104. 排列的数目 == 377

完全背包问题 + 排列，num需要重复计算，所以放在内循环。
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target     
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[-1]

s = Solution()
print(s.combinationSum4([1,2,3], 4))