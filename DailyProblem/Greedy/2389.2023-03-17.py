from typing import List
from bisect import bisect_right
'''
2389. 和有限的最长子序列
https://leetcode.cn/problems/longest-subsequence-with-limited-sum/

贪心+二分
因为子序列可以不连续，所以这个条件啥用没有。
贪心地每次从最小的数开始取，得到的序列长度最长。
为了缩小查询复杂度，可以用前缀和数组存储，每次查询二分查找小于等于query的最大前缀和。
时间复杂度：排序O(nlogn)，前缀和O(q)，查询O(qlogn)，总体复杂度为O((n + q)logn)，其中n为nums长度，q为queries长度。
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
        res = [0] * len(queries)
        for i, query in enumerate(queries):
            res[i] = bisect_right(prefix, query) - 1
        return res

s = Solution()
print(s.answerQueries([4,5,2,1], [3,10,21]))