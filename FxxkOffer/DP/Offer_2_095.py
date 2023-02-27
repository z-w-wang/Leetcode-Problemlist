import tools
'''
剑指 Offer II 095. 最长公共子序列 == 1143. 最长公共子序列

经典二维DP问题
定义dp[i][j]为text1[0: i]和text2[0: j]的最长公共子序列
按照text1[i]与text2[j]是否相等，定义两个子问题
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]

s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))