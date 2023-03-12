from typing import List
'''
455. 分发饼干
https://leetcode.cn/problems/assign-cookies/
排序，饼干由小到大尽量满足孩子要求。
嘎嘎贪心。
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        biscuit_index = 0
        res = 0
        for child in g:
            while biscuit_index < len(s) and child > s[biscuit_index]:
                biscuit_index += 1
            if biscuit_index == len(s):
                break
            res += 1
            biscuit_index += 1
        return res
    
s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))