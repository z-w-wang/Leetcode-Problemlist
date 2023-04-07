from functools import cache
from typing import List
'''
剑指 Offer II 112. 最长递增路径
https://leetcode.cn/problems/fpTFWP/

搜索就完事了，记忆化来记录之前搜过的答案来减少时间复杂度。
可以拓扑排序，懒得写。
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pos = ((0, -1), (0, 1), (-1, 0), (1, 0))
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(x, y):
            res = 1
            for dx, dy in pos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
                    res = max(res, dfs(nx, ny) + 1)
            return res
        
        return max(dfs(i, j) for i in range(m) for j in range(n))

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))