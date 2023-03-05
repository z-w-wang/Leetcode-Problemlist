from typing import List
from collections import defaultdict
'''
剑指 Offer II 114. 外星文字典 == 269

拓扑排序题
对比相邻两个单词，不一样的那一位为一个有向边，构造一个有向图。
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indeg = defaultdict(int)
        g = defaultdict(list)
        s = set()
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return ""
                if words[i][j] != words[i + 1][j]:
                    g[words[i][j]].append(words[i + 1][j])
                    indeg[words[i + 1][j]] += 1
                    break
        for word in words:
            for c in word:
                s.add(c)
        
        q = [c for c in s if indeg[c] == 0]
        start = end = 0
        while end < len(q):
            end = len(q)
            for i in range(start, end):
                for out in g[q[i]]:
                    indeg[out] -= 1
                    if indeg[out] == 0:
                        q.append(out)
            start = end
        if end < len(s):
            return ""

        return "".join(q)

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))