from typing import List
from collections import deque
'''
剑指 Offer II 109. 开密码锁 == 752
最小次数→BFS
用集合存储deadends，一旦遇到该数字直接弹出。
用seen记录见过的code，防止无限循环。

题解中有A*算法，有空一定学。
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = {d for d in deadends}
        seen = set()
        q = deque([("0000", 0)])
        while q:
            code, time = q.popleft()
            if code == target:
                return time
            if code in deadends or code in seen:
                continue
            seen.add(code)
            time += 1
            for i in range(4):
                if code[i] == '9':
                    curname = code[:i] + '0' + code[i + 1: ]
                else:
                    curname = code[:i] + chr(ord(code[i]) + 1) + code[i + 1: ]
                q.append((curname, time))
                if code[i] == '0':
                    curname = code[:i] + '9' + code[i + 1: ]
                else:
                    curname = code[:i] + chr(ord(code[i]) - 1) + code[i + 1: ]
                q.append((curname, time))
        return -1
s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))