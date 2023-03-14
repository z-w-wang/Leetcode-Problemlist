from typing import List
'''
122. 买卖股票的最佳时机 II
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

能多次买入卖出的情况下，最好情况是每次涨价都能买到，每次下跌都没持有股票。
所以直接统计相邻两天的股票价格，上涨就买，求上涨的总和即可。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))