from typing import List
'''
面试题 17.05.  字母与数字

前缀和
直接暴力统计复杂度为O(n^2)，对于题目中10^6的数据量会RE。
字母为1，数字为-1，原问题转换成求连续子数组，使区间和为0。
用前缀和做即可。
'''
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic = {0: 0}
        flag = 0
        res = 0
        start, end = -1, -1
        for i, c in enumerate(array):
            flag = flag + 1 if c.isalpha() else flag - 1
            if flag not in dic:
                dic[flag] = i + 1
            else:
                if res < i + 1 - dic[flag]:
                    res = i + 1 - dic[flag]
                    start, end = dic[flag], i + 1
        return array[start: end] if end != -1 else []
s = Solution()
print(s.findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]))