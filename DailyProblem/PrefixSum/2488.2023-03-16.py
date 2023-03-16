from typing import List
from collections import defaultdict
'''
2488. 统计中位数为 K 的子数组
https://leetcode.cn/problems/count-subarrays-with-median-k/

前缀和 + 哈希表
大于k的数记为1，小于k的数记为-1
原问题转换成求一个子数组，其区间和为0或1（1对应偶数长度的子数组）
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        res = 0
        k_index = -1
        dicleft = defaultdict(int)
        dicleft[0] = 1
        for i, num in enumerate(nums):
            if num == k:
                k_index = i
            elif num > k:
                prefix += 1
            else:
                prefix -= 1
            if k_index == -1:
                dicleft[prefix] += 1
            else:
                res += dicleft[prefix] + dicleft[prefix - 1]
        return res

s = Solution()
print(s.countSubarrays([3,2,1,4,5], 4))