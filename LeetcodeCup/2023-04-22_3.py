from typing import List
# 超时 O(n^3)
class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        xheap = []
        yheap = []
        maxres = 1
        for matrix in forceField:
            x1, y1, x2, y2 = matrix[0] - matrix[2]/2, matrix[1] - matrix[2]/2, matrix[0] + matrix[2]/2, matrix[1] + matrix[2]/2
            xheap.extend([x1, x2])
            yheap.extend([y1, y2])
        xheap = list(set(xheap))
        yheap = list(set(yheap))
        xheap.sort()
        yheap.sort()
        for x in xheap:
            for y in yheap:
                count = 0
                for matrix in forceField:
                    if x >= matrix[0] - matrix[2]/2 and x <= matrix[0] + matrix[2]/2 and y >= matrix[1] - matrix[2]/2 and y <= matrix[1] + matrix[2]/2:
                        count += 1
                maxres = max(maxres, count)
        return maxres