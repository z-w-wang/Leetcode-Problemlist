from typing import List
from collections import deque

class Trie:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.maxlength = 0
        for word in words:
            node = self.trie
            self.maxlength = max(self.maxlength, len(word))
            for i in range(len(word) - 1, -1, -1):
                c = word[i]
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            node.is_end = True

        self.q = deque([])

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        if len(self.q) > self.maxlength:
            self.q.popleft()
        node = self.trie
        for i in range(len(self.q) - 1, -1, -1):
            
            if self.q[i] in node.children:
                node = node.children[self.q[i]]
            else:
                return node.is_end
            if node.is_end:
                return True
        return False

s = StreamChecker(["ab","ba","aaab","abab","baa"])
stream = [["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
res = [None] * len(stream)
for i, st in enumerate(stream):
    res[i] = s.query(st[0])

print(res)