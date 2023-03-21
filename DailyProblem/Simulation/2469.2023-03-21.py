from typing import List
'''
2469. 温度转换
https://leetcode.cn/problems/convert-the-temperature/

...离谱
《CV题解就能过》
'''
class Solution:
    def convertTemperature(self, 摄氏度: float) -> List[float]:
        开氏度 = 摄氏度 + 273.15
        华氏度 = 摄氏度 * 1.80 + 32.00
        return [开氏度, 华氏度]
    
解 = Solution()
print(解.convertTemperature(36.50))