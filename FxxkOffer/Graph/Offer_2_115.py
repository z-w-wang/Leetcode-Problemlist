from typing import List
from collections import deque
'''
剑指 Offer II 115. 重建序列 == 444
检测是否是唯一拓扑排序，每次操作完判断是否只存在一个入度为0的结点。

'''
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indeg = [0] * n
        edges = [[] for _ in range(n)]

        for sequence in sequences:
            for i in range(1, len(sequence)):
                indeg[sequence[i] - 1] += 1
                edges[sequence[i - 1] - 1].append(sequence[i] - 1)

        q = deque([i for i in range(n) if indeg[i] == 0])


        while q:
            if len(q) > 1:
                return False
            
            for i in edges[q[0]]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)

            q.popleft()

        return True
    
s = Solution()
print(s.sequenceReconstruction([1,2,3], [[1,2],[1,2,3]]))