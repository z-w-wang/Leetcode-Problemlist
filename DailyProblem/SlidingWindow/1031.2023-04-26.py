from typing import List
'''
1031. 两个非重叠子数组的最大和
https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/

滑动窗口
对于区间nums[i: i + Len]，i + Len之前的最大不重叠数组和为 sum(nums[i: i + Len]) 加上 nums[: i ]中的另一个数组的最大区间和。
可以分别计算first数组在前的情况和second数组在前的情况
对于数组和 和 数组和的最大值，可以用前缀和数组来存储以减少时间复杂度
总时间复杂度O(n)
'''
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        firstsum = sum(nums[: firstLen - 1])
        firstlist = [0] * (len(nums) - firstLen + 1)
        prefirst = [0] * (len(nums) - firstLen + 1)
        maxnum = 0
        for i in range(len(firstlist)):            
            firstsum += nums[i + firstLen - 1]
            firstlist[i] = firstsum
            maxnum = max(maxnum, firstsum)
            prefirst[i] = maxnum
            firstsum -= nums[i]

        secondsum = sum(nums[: secondLen - 1])
        secondlist = [0] * (len(nums) - secondLen + 1)
        maxnum = 0
        maxres = 0
        presecond = [0] * (len(nums) - secondLen + 1)
        for i in range(len(secondlist)):            
            secondsum += nums[i + secondLen - 1]
            secondlist[i] = secondsum
            maxnum = max(maxnum, secondsum)
            presecond[i] = maxnum
            if i - firstLen >= 0:
                maxres = max(maxres, prefirst[i - firstLen] + secondsum)
            secondsum -= nums[i]

        for i in range(secondLen, len(firstlist)):
            maxres = max(maxres, presecond[i - secondLen] + firstlist[i])
        
        return maxres