from typing import List
'''
剑指 Offer II 102. 加减的目标值 == 494

可转换成剑指 Offer II 101题做，从-sum1开始算（所有运算符为-），每将一个数的符号改成+，相当于增加了2*num。
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum1:=sum(nums)) < abs(target) or (sum1 + target) % 2:
            return 0
        dp = [1] + [0] * (target + sum1)
        for num in nums:
            for j in range(target + sum1, 2 * num - 1, -1):
                dp[j] += dp[j - 2 * num]
        return dp[-1]
    
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))