from typing import List
'''
452. 用最少数量的箭引爆气球
https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

每一箭射穿的气球满足：最左边的气球右端在最右边气球左端的右面。
可以贪心，按照气球右端排序
记录新开的一箭的气球的右端点end，一旦有一个气球的左端点在end右面，则这一箭已经射不到这个气球了，需要新的一箭。
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 1
        end = points[0][1]
        for st, en in points:
            if st > end:
                res += 1
                end = en
        return res
    
s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))