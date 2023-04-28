from collections import defaultdict
from typing import List
'''
1048. 最长字符串链
https://leetcode.cn/problems/longest-string-chain/

连续的strchain，需要前后长度差为1。
首先按照长度给words分组，然后遍历不同长度的str
对于所有长度为i - 1的str，如果长度为i的str的前身是i - 1的str，则dp[i] = dp[i - 1] + 1
如果对于任何的长度为i - 1的str都不是该长度为i的str的前身，则dp[i] = 1

实现如下，时间复杂度O(nl^2)，n为words长度，l为words中单词的最大长度。
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dic = defaultdict(set)
        maxlen = 0
        for word in words:
            dic[len(word)].add(word)
            maxlen = max(maxlen, len(word))
        
        def check(s1, s2):
            assert len(s1) < len(s2)
            flag = 0
            for i in range(len(s1)):
                if s1[i] != s2[i + flag]:
                    if flag == 1:
                        return False
                    flag = 1
                    if s1[i] != s2[i + flag]:
                        return False
            return True
        res = 1
        predict = dict()
        for i in range(1, 17):
            curdict = defaultdict(int)
            for word in dic[i]:
                for k, v in predict.items():
                    if check(k, word):
                        curdict[word] = max(v + 1, curdict[word])
                        res = max(res, v + 1)
                if word not in curdict:
                    curdict[word] = 1
            predict = curdict
        return res