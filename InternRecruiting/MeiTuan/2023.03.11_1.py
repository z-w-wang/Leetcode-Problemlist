'''
字符串修改
时间限制: 3000MS
内存限制: 589824KB
题目描述:
小美有一个由数字字符组成的字符串。现在她想对这个字符串进行一些修改。
具体地，她可以将这个字符串中任意位置字符修改为任意的数字字符。
她想知道，至少进行多少次修改，可以使得修改后的字符串不包含两个连续相同的字符？
例如，对于字符串“111222333”，她可以进行3次修改将其变为“121212313”
输入描述：
一行，一个字符串s，保证s只含数字字符。
1<=|s|<=100000
输出描述：
一行，一个整数，表示修改的最少次数。
样例输入：
111222333
样例输出：
3
'''
# 思路
'''
统计连续字符长度，除以二即为所需修改的长度。
或者每遇到连续的字符就把它修改成一个字母，统计需要修改的次数。
'''
import sys
inp = input()
if len(inp) == 1:
    print(0)
    sys.exit(0)
res = 0
count = 0
for i in range(len(inp) - 1):
    if inp[i] == inp[i + 1]:
        count += 1
    else:
        res += (count + 1) // 2
        count = 0
res += (count + 1) // 2
print(res)
# # 方法二
# inp = input()
# inplist = [c for c in inp]
# count = 0
# for i in range(len(inplist) - 1):
#     if inplist[i] == inplist[i + 1]:
#         inplist[i + 1] = 'p'
#         count += 1
# print(count)