from typing import List
'''
剑指 Offer II 106. 二分图 == 785

图着色问题，广度优先遍历将邻居染成不一样的颜色，如果染色冲突就说明不可二分。
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        flag = [0] * len(graph)
        for i in range(len(graph)):
            if flag[i]:
                continue
            flag[i] = 1
            f = -1
            s = [i]
            while s:
                temps = []
                for node in s:
                    for j in graph[node]:
                        if flag[j] == -f:
                            return False
                        if flag[j] == 0:
                            flag[j] = f
                            temps.append(j)
                f = -f
                s = temps[:]
        return True
    
s = Solution()
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))