from typing import List
'''
435. 无重叠区间
https://leetcode.cn/problems/non-overlapping-intervals/

由于确定前面的区间后，后面的区间选择主要和前面区间的右端点比较，所以按照右端点排序，每次尽可能选择右端点最小的区间。
嘎嘎贪心。
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda x: x[1])
        index = 0
        res = 0
        for check in range(1, len(intervals)):
            if intervals[index][1] > intervals[check][0]:
                res += 1
            else:
                index = check
        return res
s = Solution()
print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))