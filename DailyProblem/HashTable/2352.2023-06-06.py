from typing import List
from collections import defaultdict
'''
2352. 相等行列对
https://leetcode.cn/problems/equal-row-and-column-pairs/

for col in zip(*grid)取列 骚的。
'''
class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        for x in grid:
            dic[tuple(x)] += 1    
        return sum(dic[tuple(y)] for y in zip(*grid))

print(Solution.equalPairs(grid=[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))