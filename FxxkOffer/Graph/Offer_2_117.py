from typing import List
'''
剑指 Offer II 117. 相似的字符串 == 839

并查集
先比较两个字符串是否相似，如果相似执行union，不相似则为新的连通分量。
'''
class Union:

    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.str2int = dict()
        self.roots = set()
        self.count = 0


    def __len__(self) -> int:
        return len(self.roots)


    def find(self, node: int) -> int:
        if node != self.parents[node]:
            self.roots.discard(node)
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]


    def union(self, a: int, b: int) -> None:
        inta, intb = self.str2int[a], self.str2int[b]
        parenta, parentb = self.find(inta), self.find(intb)

        self.parents[parenta] = parentb
        self.roots.discard(parenta)
        self.roots.add(parentb)


    def add(self, s: str) -> None:
        if s not in self.str2int:
            self.str2int[s] = self.count
            self.roots.add(self.count)
        else:
            self.parents[self.count] = self.find(self.str2int[s])
            self.count += 1
            return
        
        self.count += 1
        
        for s1 in self.str2int:
            if self.is_similar(s, s1):
                self.union(s, s1)


    def is_similar(self, s1: str, s2: str) -> bool:
        count = 0
        for i, c in enumerate(s1):
            if c != s2[i]:
                count += 1

        return count == 2



class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        u = Union(len(strs))
        for s in strs:
            u.add(s)

        return len(u)
    


s = Solution()
print(s.numSimilarGroups(["tars","rats","arts","star"]))