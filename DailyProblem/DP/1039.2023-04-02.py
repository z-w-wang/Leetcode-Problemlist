from functools import cache
from typing import List
'''
1039. 多边形三角剖分的最低得分
https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/

DP问题
设memory_search(i, j)为values[i: j + 1]的点的结果，假设生成的三角形顶点为i, j, k，则问题可分成：
memory_search(i, j) = memory_search(i, k) + memory_search(k, j) + triangle(i, k, j)
自顶向下记忆化搜索即可。
注：@cache 等于 @lru_cache(maxsize=None, typed=False)，即一直保留。
'''
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def memory_search(i, j):
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            if i + 2 > j:
                return 0
            return min(values[i] * values[k] * values[j] + memory_search(i, k) + memory_search(k, j)\
                            for k in range(i + 1, j))
        
        return memory_search(0, len(values) - 1)

s = Solution()
print(s.minScoreTriangulation([3,7,4,5]))