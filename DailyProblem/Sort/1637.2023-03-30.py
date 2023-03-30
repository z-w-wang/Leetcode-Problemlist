from typing import List
'''
1637. 两点之间不包含任何点的最宽垂直区域
https://leetcode.cn/problems/widest-vertical-area-between-two-points-containing-no-points/

与y坐标无关，取x坐标去重排序，遍历即可。
'''
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_list = sorted(list(set([point[0] for point in points])))
        return max([x_list[i + 1] - x_list[i] for i in range(len(x_list) - 1)], default = 0)

s = Solution()
print(s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))