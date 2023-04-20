from bisect import bisect_left
from typing import List
INF = 10 ** 9 + 1
'''
1187. 使数组严格递增
https://leetcode.cn/problems/make-array-strictly-increasing/

DP
首先对arr2排序，方便二分查找，以降低检索需要替换元素的时间复杂度。
设dp[i]表示使arr1[: i + 1]严格递增的最小操作数
对于arr1[i]来说
若arr1[i - 1]不需要更换，说明此时arr1[i - 1] < arr1[i]，那么dp[i] = dp[i - 1]
若arr1[i - 1]需要更换，首先通过二分查找找到arr2中不大于arr[i]的数
然后，为了保证arr1[i]之前的数有序，于是从arr1[i - 1]开始往之前替换，有
dp[i] = dp[i - j - 1] + j if arr1[i - j - 1] < arr2[idx - j]
为了防止最后一位不用替换而找不到所求的数，在最后一位加入INF来保证最后结果出现在INF这一位上。
时间复杂度O((m + n)logm + n * min(m, n))
'''
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))
        arr1 = [-1] + arr1 + [INF]
        n1 = len(arr1)
        dp = [INF] * n1
        dp[0] = 0
        for i in range(1, n1):
            idx = bisect_left(arr2, arr1[i])
            for j in range(1, min(idx, i - 1) + 1):
                if arr1[i - j - 1] < arr2[idx - j]:
                    dp[i] = min(dp[i], dp[i - j - 1] + j)
            if arr1[i] > arr1[i - 1]:
                dp[i] = min(dp[i], dp[i - 1])
        return -1 if dp[-1] == INF else dp[-1]
    
s = Solution()
print(s.makeArrayIncreasing([1,5,3,6,7], [4,3,1]))