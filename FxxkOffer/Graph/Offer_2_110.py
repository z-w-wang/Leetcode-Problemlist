from typing import List
'''
剑指 Offer II 110. 所有路径 == 797

图DFS，因为有向无环，少了不少难度。
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res = []
        def dfs(index, pathlist):
            if index == n:
                res.append(pathlist)
                return
            for i in graph[index]:
                dfs(i, pathlist + [i])
        dfs(0, [0])
        return res
    
s = Solution()
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))