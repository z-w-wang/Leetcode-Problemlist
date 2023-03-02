from typing import List
'''
剑指 Offer II 105. 岛屿的最大面积 == 695

普通的DFS
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(x, y):
            if x >= m or x < 0 or y >= n or y < 0 or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            res = 1
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):               
                res += dfs(i, j)
            return res

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
    
s = Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],\
                         [0,0,0,0,0,0,0,1,1,1,0,0,0],\
                         [0,1,1,0,1,0,0,0,0,0,0,0,0],\
                         [0,1,0,0,1,1,0,0,1,0,1,0,0],\
                         [0,1,0,0,1,1,0,0,1,1,1,0,0],\
                         [0,0,0,0,0,0,0,0,0,0,1,0,0],\
                         [0,0,0,0,0,0,0,1,1,1,0,0,0],\
                         [0,0,0,0,0,0,0,1,1,0,0,0,0]]))