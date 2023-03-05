from typing import List
'''
剑指 Offer II 116. 省份数量 == 547

DFS、BFS都可以做，用一个数组记录是否被遍历到。
如果需要快速查询两个城市属不属于一个省份，可以用并查集做，这里不需要。
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        is_arrived = [False] * len(isConnected)
        res = 0
        def dfs(city: int) -> None:
            for i, is_connected in enumerate(isConnected[city]):
                if is_connected and not is_arrived[i]:
                    is_arrived[i] = True
                    dfs(i)
        for i in range(len(isConnected)):
            if is_arrived[i]:
                continue
            is_arrived[i] = True
            dfs(i)
            res += 1
        return res
    
s = Solution()
print(s.findCircleNum([[1,1,0],\
                       [1,1,0],\
                       [0,0,1]]))