from typing import List
'''
剑指Offer Ⅱ 101.分割等和子集 == 416

0-1背包DP，注意边界条件和循环范围。
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if len(nums) < 2 or (sum1:=sum(nums)) % 2 or max(nums) > (sum1:=sum1 // 2):
            return False
        dp = [True] + [False] * sum1
        for num in nums:
            for j in range(sum1, num - 1, -1):    # 到num-1要结束，不然会遍历到负索引。
                dp[j] |= dp[j - num]
        return dp[-1]
    
s = Solution()
print(s.canPartition([1,5,11,5]))