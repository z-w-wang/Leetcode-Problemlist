from typing import List
'''
剑指 Offer II 118. 多余的边 == 684

并查集
遍历edges，判断遍历到的边的两点是否已经在同一个连通分量中，若在则为多余的边
'''
class Union:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, a, b):
        self.parents[self.find(a)] = self.find(b)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        u = Union(n)

        for a, b in edges:
            if u.find(a - 1) == u.find(b - 1):
                return [a, b]
            
            u.union(a - 1, b - 1)


        return []