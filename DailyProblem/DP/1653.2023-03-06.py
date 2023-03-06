'''
1653. 使字符串平衡的最少删除次数

DP问题。
平衡字符串存在一个位置，该位置之前全为a，后面全为b。
dpa表示前i个是a的时候需要删除的次数，dpb表示第i个为b时，前i个字母的删除数。
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dpa, dpb = 0, 0
        for c in s:
            if c == 'a':
                dpb += 1
            else:
                dpa += 1
            dpb = min(dpa, dpb)
        return dpb
    
s = Solution()
print(s.minimumDeletions("bbaaaaabb"))