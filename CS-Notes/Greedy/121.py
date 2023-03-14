from typing import List
'''
121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

用minprice记录见过的最小值
遍历的时候如果遍历到的值比minprice小，就更新minprice
如果比minprice大，就比较现在卖出的话能赚多少钱

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        res = 0
        for price in prices:
            minprice = min(minprice, price)
            res = max(res, price - minprice)
        return res

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))