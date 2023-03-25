from typing import List
from collections import deque
'''
1032. 字符流
https://leetcode.cn/problems/stream-of-characters/

Trie树
因为每次判断的是后缀 将words里的单词倒序放进字典树即可
为了缩减字符流的空间占用 记录words单词最大长度作为字符流缓存大小
每次query时倒序搜字典树就行了 遇到is_end说明找到后缀
时间复杂度O((q + n) * l)，q为查询次数，l为words中单词最大长度，n为words长度。
需要O(nl)建树，O(ql)查询。

官解在说什么吊东西 看不懂
'''

class Trie:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            node = self.trie
            for i in range(len(word) - 1, -1, -1):
                c = word[i]
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.is_end = True

        self.q = deque(maxlen=max(map(len, words)))

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        node = self.trie
        for i in range(len(self.q) - 1, -1, -1):

            if self.q[i] in node.children:
                node = node.children[self.q[i]]
            else:
                return node.is_end
            if node.is_end:
                return True
        return False


s = StreamChecker(["ab", "ba", "aaab", "abab", "baa"])
stream = [["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], [
    "a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"], ["a"], ["a"], ["a"]]
res = [None] * len(stream)
for i, st in enumerate(stream):
    res[i] = s.query(st[0])

print(res)
