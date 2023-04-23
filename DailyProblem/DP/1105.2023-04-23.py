from typing import List
from bisect import bisect_left
from itertools import accumulate
'''
1105. 填充书架
https://leetcode.cn/problems/filling-bookcase-shelves/

DP
设dp[i]表示前i本书的最小高度。
对于0 <= j < i 且sum(width[j:i + 1]) < shelfWidth，将j到i的书本单独放一行，有
dp[i + 1] = dp[j] + maxwidth(j, i)

以下实现不是最优最快解法，随便写写，能跑。
'''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] + [float('inf')] * len(books)
        widths = [book[0] for book in books]
        prefixs = [0] + list(accumulate(widths))
        for i in range(len(books)):
            idx = bisect_left(prefixs, prefixs[i + 1] - shelfWidth)
            maxheight = 0
            for j in range(i, idx - 1, -1):
                maxheight = max(maxheight, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + maxheight)
        return dp[-1]
    
s = Solution()
print(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))