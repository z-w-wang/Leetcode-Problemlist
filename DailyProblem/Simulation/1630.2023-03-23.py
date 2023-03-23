from typing import List
'''
1630. 等差子数组
https://leetcode.cn/problems/arithmetic-subarrays/

模拟就行
m个查询，nums长度为n，每次将查询区间的数组排序，依次比较相邻两个数的差。时间复杂度为O(mnlogn)，题目中m和n均小于500，可行。
官解优化了单次查询复杂度，能达到O(mn)，懒得看了，忙。
'''
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True] * len(r)
        for i, (left, right) in enumerate(zip(l, r)):
            query = sorted(nums[left: right + 1])
            b = query[1] - query[0]
            for j in range(right - left):
                if query[j + 1] - query[j] != b:
                    res[i] = False
                    break
        return res
    
s = Solution()
print(s.checkArithmeticSubarrays([4,6,5,9,3,7], [0,0,2], [2,3,5]))