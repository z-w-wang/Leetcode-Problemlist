from functools import cache
'''
1012. 至少有 1 位重复的数字
https://leetcode.cn/problems/numbers-with-repeated-digits/

原问题转换成求没有任何重复数字的个数，再用n减去这个结果
用@cache修饰器完成数位DP
递归参数i表示从左往右第i位，mask表示0-9数字是否出现，is_limit表示是否受到n的约束

题解的组合数学不想看了
'''

# Code from 0X3F
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        @cache # 记忆化搜索
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)  # is_num 为 True 表示得到了一个合法数字
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, mask, False, False)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if (mask >> d & 1) == 0:  # d 不在 mask 中
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return n - f(0, 0, True, False)
s = Solution()
print(s.numDupDigitsAtMostN(1000))