from typing import List
'''
1487. 保证文件名唯一

哈希表模拟，记录name出现的次数。
最终命名的名字也要记录，以通过样例["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]。
'''
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        cnt = dict()
        for i, name in enumerate(names):
            if name in cnt:
                curname = name
                while curname in cnt:
                    curname = f'{name}({cnt[name]})'
                    cnt[name] += 1
                names[i] = curname
                cnt[names[i]] = 1
            else:
                cnt[name] = 1
        return names
    
s = Solution()
print(s.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))