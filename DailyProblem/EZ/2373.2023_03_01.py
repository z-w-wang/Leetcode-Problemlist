from typing import List
'''
2373. 矩阵中的局部最大值

模拟就完事儿了
'''

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2],\
                                    grid[i + 1][j],grid[i + 1][j + 1],grid[i + 1][j + 2],\
                                    grid[i + 2][j],grid[i + 2][j + 1],grid[i + 2][j + 2])
        return res

s = Solution()
print(s.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))