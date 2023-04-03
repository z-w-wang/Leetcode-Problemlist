from bisect import bisect_left
from typing import List
'''
1053. 交换一次的先前排列
https://leetcode.cn/problems/previous-permutation-with-one-swap/

贪心。
将arr分成两部分：arr[: i + 1] 和 arr[i + 1: ]
其中arr[i + 1: ]是arr数组最长的后缀非递减连续序列
数字的交换不会出现在arr[i + 1: ]中，因为已经是最小字典序，任何交换都会增大字典序。
符合题目的交换为：
arr[i + 1: ]中比arr[i]小的最大数，与arr[i]交换。
若有多个最大数，取下标最小的数与arr[i]交换，以保证最大序列。
时间复杂度：O(n)
'''
class Solution: 
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        dic = dict()
        for i in range(len(arr) - 2, -1, -1):
            dic[arr[i + 1]] = i + 1
            if arr[i + 1] < arr[i]:
                break
        if i == 0 and arr[0] <= arr[1]:
            return arr
        
        index = dic[arr[i + bisect_left(arr[i + 1: ], arr[i])]]
        arr[i], arr[index] = arr[index], arr[i]
        return arr

s = Solution()
arr = [3,1,1,3]
print(arr, "->", s.prevPermOpt1(arr))