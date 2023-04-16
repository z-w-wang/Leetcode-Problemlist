'''
2023-04-15 图像算法方向 2

题目描述：
众所周知，任何正整数都可以表示为若干个不相等的3的幂的和或差。
例如20=27+3-9+1,30=27+3等。
给定一个正整数，请你输入一个合法的表达式，请务必保证表达式只包含加号和减号，且每一项均为3的幂。
为了保证答案唯一，你需要按每一项从大到小来输出。

输入描述：
一个正整数x
1<=x<=10^9

输出描述：
一个表达式，最终的答案必须等于x。
表达式的每一项必须是3的幂，且不能有两项相同。
例如6必须输出9-3而不是3+3。
'''
# 思路
'''
将x转换成三进制的形式。
从低位到高位遍历，每遇到一个不为0或者1的数位i，都将其转化为：
2 * 3^i = 3^(i+1) - 3^i
3 * 3^i = 3^(i+1)
用flag表示是否需要增加下一个高位。
时间复杂度O(logn)
'''
x = int(input())
nums = []
while x > 0:
    nums.append(x % 3)
    x //= 3
ops = ['+'] * len(nums)
flag = False
string = ""
for i, num in enumerate(nums):
    if flag:
        num += 1
        flag = False
    if num == 1:
        nums[i] = 1
    if num == 2:
        ops[i] = '-'
        nums[i] = 1
        flag = True
    if num == 3:
        nums[i] = 0
        flag = True
if flag:
    nums.append(1)
    ops.append('+')
res = ""
base = 1
for i in range(len(nums) - 1):
    if nums[i] > 0:
        res = ops[i] + str(base) + res
    base *= 3
res = str(base) + res
print(res)     