from typing import List
'''
剑指 Offer II 065. 最短的单词编码
https://leetcode.cn/problems/iSwD2y/

字典树
由于每次以#结尾，题目的要求可以理解为，尽可能将单词的后缀子串合并，求合并后的单词数量
可以用Trie树，将words里的单词倒序插入到树中，其中Trie.depth记录当前的树的深度，每次将深度加入到结果中

每次插入的时候判断一下途中是否包含之前的单词(是否遇到Trie.is_end = True)
如果有，该单词为现在插入单词的后缀串，删除该单词的is_end标识，并从结果中减去该单词长度

时间复杂度：O(nl)，其中n为words数组长度，l为words中单词最大长度
'''
class Trie:
    def __init__(self, depth):
        self.child = dict()
        self.is_end = False
        self.depth = depth


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        t = Trie(1)
        res = 0
        for word in words:
            tempt = t
            l = len(word)
            for i in range(l):
                if (c := word[l - 1 - i]) not in tempt.child:
                    tempt.child[c] = Trie(i + 1)
                tempt = tempt.child[c]
                if tempt.is_end:
                    res -= 1 + tempt.depth
                    tempt.is_end = False
            if len(tempt.child) == 0 and not tempt.is_end:
                res += 1 + tempt.depth
                tempt.is_end = True
        return res

# 贴一个题解的骚做法 狠狠用库
'''

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

'''

s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))