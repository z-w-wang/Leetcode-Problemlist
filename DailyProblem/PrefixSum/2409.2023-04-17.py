from itertools import accumulate
'''
2409. 统计共同度过的日子数
https://leetcode.cn/problems/count-days-spent-together/

将日期转换为一年中的第多少天，利用前缀和简化查询时间复杂度。
用容斥定理计算重合天数。
'''
PREFIXS = [0] + list(accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date2day(date: str) -> int:
            month, day = date.split('-')
            return PREFIXS[int(month) - 1] + int(day)
        
        Aa, Al, Ba, Bl = date2day(arriveAlice), date2day(leaveAlice), date2day(arriveBob), date2day(leaveBob)
        return 0 if Al < Ba or Bl < Aa else \
                1 + Al + Bl - Aa - Ba - max(Aa, Al, Ba, Bl) + min(Aa, Al, Ba, Bl)
    
s = Solution()
print(s.countDaysTogether("10-20", "12-22", "06-21", "07-05"))