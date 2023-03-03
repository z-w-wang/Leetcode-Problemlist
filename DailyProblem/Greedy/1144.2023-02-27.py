from typing import *

'''
1144. 递减元素使数组呈锯齿状
只能减少元素大小
用贪心思想，分类成奇数和偶数两种情况，分别计算
'''
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res0, res1 = 0, 0
        for i in range(0, len(nums), 2):
            temp = 0
            if i + 1 < len(nums):
                temp = max(temp, nums[i] - nums[i + 1] + 1)
            if i > 0:
                temp = max(temp, nums[i] - nums[i - 1] + 1)
            res0 += temp
        for i in range(1, len(nums), 2):
            temp = 0
            if i + 1 < len(nums):
                temp = max(temp, nums[i] - nums[i + 1] + 1)
            if i > 0:
                temp = max(temp, nums[i] - nums[i - 1] + 1)
            res1 += temp
        return min(res0, res1)
    
s = Solution()
print(s.movesToMakeZigzag([9,6,1,6,2]))