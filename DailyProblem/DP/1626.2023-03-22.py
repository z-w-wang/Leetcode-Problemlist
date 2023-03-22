from typing import List
'''
1626. 无矛盾的最佳球队
https://leetcode.cn/problems/best-team-with-no-conflicts/

DP
如图所示 懒得解释
偷伞的σ
'''
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * len(scores)
        res = 0
        scores_ages = sorted(zip(scores, ages))
        for i, (score, age) in enumerate(scores_ages):
            for j in range(i):
                if age >= scores_ages[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += score
            res = max(res, dp[i])
        return res

s = Solution()
print(s.bestTeamScore([4,5,6,5], [2,1,2,1]))