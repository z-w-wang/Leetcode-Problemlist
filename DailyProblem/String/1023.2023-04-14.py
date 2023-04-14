from typing import List
'''
1023. 驼峰式匹配
https://leetcode.cn/problems/camelcase-matching/submissions/

略
'''
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [True] * len(queries)
        n = len(pattern)
        for i, query in enumerate(queries):
            pointer = 0
            for c in query:
                if pointer == n:
                    if c.isupper():
                        res[i] = False
                        break
                    continue
                if c != pattern[pointer]:
                    if c.isupper():
                        res[i] = False
                        break
                    continue
                pointer += 1
            if pointer != n:
                res[i] = False
        return res
    
s = Solution()
print(s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))