from typing import List
'''
1574. 删除最短的子数组使剩余数组有序
https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

双指针
去掉的子数组是连续区间，假设去掉的区间为[i + 1: j]，搜寻出满足题意的[0: i]和[j: ]即可

'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        res = j
        for i, num in enumerate(arr):
            while j < n and arr[j] < arr[i]:
                j += 1
            res = min(res, j - i - 1)
            if i < n - 1 and num > arr[i + 1]:
                break
        return res
    
s = Solution()
print(s.findLengthOfShortestSubarray([16,10,0,3,22,1,14,7,1,12,15]))