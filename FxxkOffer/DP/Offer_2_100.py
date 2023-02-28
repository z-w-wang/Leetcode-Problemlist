from typing import List

'''
由三角形底向上DP，比题解省了不少边界条件。
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[-1][j] = min(triangle[-1][j], triangle[-1][j + 1]) + triangle[i][j]
        return triangle[-1][0]

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))