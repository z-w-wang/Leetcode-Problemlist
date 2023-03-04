from typing import List
from collections import defaultdict
'''
剑指 Offer II 113. 课程顺序 == 210

将课程先后顺序理解为有向边，题目可以理解为用拓扑排序检测有向图中是否有环。
indeg数组记录每个点的前驱结点，in2out数组记录每个点的后继结点，s记录q中加入了哪些结点。

'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = []
        in2out = defaultdict(set)
        s = set()

        for i in range(numCourses):
            indeg.append(set())
            s.add(i)

        for cur, pre in prerequisites:
            indeg[cur].add(pre)
            in2out[pre].add(cur)

        q = []
        for n in range(numCourses):
            if len(indeg[n]) == 0:
                q.append(n)
                s.remove(n)

        start, end = 0, 0
        while len(q) > end:
            end = len(q)
            for i in range(start, end):
                for cur in in2out[q[i]]:
                    indeg[cur].remove(q[i])
                    if len(indeg[cur]) == 0:
                        q.append(cur)
                        s.remove(cur)
            start = end

        if len(s) > 0:
            return []
        return q
    
s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))