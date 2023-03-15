from typing import List
'''
1615. 最大网络秩
https://leetcode.cn/problems/maximal-network-rank/

记录每个点的连接情况，遍历点对的连接数量加起来
如果点对之间相连，减一

贪心直接统计前二的连接数量的点去做也可以，懒得写了。
'''
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = [set() for _ in range(n)]
        for (a, b) in roads:
            g[a].add(b)
            g[b].add(a)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                rank = len(g[i]) + len(g[j])
                if j in g[i] or i in g[j]:
                    rank -= 1
                res = max(res, rank)
        return res
    
s = Solution()
print(s.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))