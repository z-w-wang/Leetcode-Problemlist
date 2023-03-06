from typing import List
'''
剑指 Offer II 119. 最长连续序列 == 128

一般想法是排序再遍历，时间复杂度为O(nlogn)
连续的数会有一个起始数字num，num - 1不在nums数组中
所以找到num - 1 不在nums中的那个数，查询其连续长度
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = 0

        for num in s:
            if num - 1 not in s:
                templen = 0
                while num in s:
                    num += 1
                    templen += 1

                maxlen = max(templen, maxlen)

        return maxlen