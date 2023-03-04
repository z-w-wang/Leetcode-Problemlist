from typing import List
'''
982. 按位与为零的三元组

直接三重循环会超时，可以预先处理两个数的与结果，然后遍历第三个数，找和它与为0的结果。
'''
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        dic = dict()
        for x in nums:
            for y in nums:
                if (num := x & y) in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
        res = 0
        for x in nums:
            for k, v in dic.items():
                if x & k == 0:
                    res += v
        return res
s = Solution()
print(s.countTriplets([2,1,3]))