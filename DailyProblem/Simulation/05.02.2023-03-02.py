
'''
面试题 05.02. 二进制数转字符串

模拟就完事儿了
题解里用乘法代替除法，运算速度和精度上应该会有保证。
'''
class Solution:
    def printBin(self, num: float) -> str:
        if num == 0.0:
            return "0.0"
        b = 0.5
        res = "0."
        for i in range(10):
            if num >= b:
                num -= b
                res += '1'
            
            
            elif num < 2 ** -33:
                return res
            else:
                res += '0'
            b /= 2
        return "ERROR"