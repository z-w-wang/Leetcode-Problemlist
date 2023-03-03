from typing import List
from collections import deque
'''
剑指 Offer II 108. 单词演变 == 127
最短 → DFS

2023.03.03
暴力枚举每位单词的26个字母，使用seen保证每种单词只被遍历了一次。时间复杂度为O(N * C * C * E)，其中N为单词表长度，C为单词长度，E = 26。
官解中先将单词表建成图，然后BFS图，时间复杂度会更低，为O(N * C * C)。
有空再回来看，先准备组会了。
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = {beginWord}
        n = len(beginWord)
        wordlist = {word for word in wordList}

        def get(word):
            for i in range(n):
                for j in range(ord('a'), ord('a') + 26):
                    if (curname:=word[: i] + chr(j) + word[i + 1: ]) not in seen and curname in wordlist:
                        yield curname
        
        q = deque([(beginWord, 0)])
        while q:
            word, time = q.popleft()
            if word == endWord:
                return time + 1
            time += 1
            for name in get(word):
                seen.add(name)
                q.append((name, time,))
        return 0
    
学个屁 = Solution()
print(学个屁.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))