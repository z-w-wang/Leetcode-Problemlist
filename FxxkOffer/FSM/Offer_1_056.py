from typing import List
'''
剑指 Offer 56 - II. 数组中数字出现的次数 II
https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/

一般做法是统计每个数字出现的次数：时间复杂度O(n)，空间复杂度O(n)
进阶做法是用32位数组统计每一位的出现次数：时间复杂度O(n)，空间复杂度O(32)
骚做法是进阶做法的优化 有限状态自动机：时间复杂度O(n)，空间复杂度O(2)

类比 剑指 Offer 56 - I. 数组中数字出现的次数
消除出现两次的数字，每一位数位的出现规律是0，1，0，1，0，1...
消除出现三次的数字，每一位数位的出现规律是0，1，2，0，1，2...
需要计算每一个状态数位的变化，三种状态可以用两个二进制位表示：00，01，10，00，01，10...
用one表示状态的第一位，two表示状态的第二位
初始情况下one的规律为：
if two == 0:
    if num == 0:
        # 00 + 0 == 0, 01 + 0 == 01
        one = one
    else:
        # 00 + 1 == 01, 01 + 1 == 10
        one = ~one
else:
    # 10 + 0 == 10, 10 + 1 == 00
    one = 0
可以简化为one = one ^ num & ~two
更新完one的状态后，用更新后的one去更新two：
if one == 0:
    if num == 0:
        # 00 + 0 == 0, 10 + 0 == 10
        two = two
    else:
        # 01 + 1 == 10, 10 + 1 == 00
        two = ~two
else:
    # 01 + 0 == 01, 00 + 1 == 01
    two = 0
可以化简为two = two ^ num & ~one
将数组中每个数字先算one再算two，最后剩下的所有01状态的数位即可组成只出现一次的数字，即one。
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one
    
s = Solution()
print(s.singleNumber([9,1,7,9,7,9,7]))