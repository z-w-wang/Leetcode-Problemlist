'''
392. 判断子序列
https://leetcode.cn/problems/is-subsequence/

贪心就完事儿了
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (lens:=len(s)) == 0:
            return True

        if lens > len(t):
            return False
        index_s = 0
        c_s = s[0]
        for c in t:
            if c == c_s:
                index_s += 1
                if index_s == lens:
                    return True
                c_s = s[index_s]
        return False
    
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))