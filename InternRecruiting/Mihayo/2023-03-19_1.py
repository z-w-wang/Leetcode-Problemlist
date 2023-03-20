'''
2023-03-19 NLP算法方向 1

题目描述：
米小游拿到了一个仅由小写字母组成的字符串，她准备进行恰好一次操作：交换两个相邻字母，在操作结束后使得字符串的字典序尽可能大。
请你输出最终生成的字符串。

输入描述：
一个仅由小写字母组成的字符串s，2<=len(s)<=200000。

输出描述：
操作后的字符串。
'''
# 思路
'''
贪心就完了。
寻找第一对s[i] <= s[i + 1]的字符对，交换就完事儿了。
如果整体都是降序的，为了确保字典序损失尽量小，交换最后两个就行。
'''
# 100%
s = input()

s_list = list(s)
is_exchanged = False

for i in range(len(s) - 1):
    if s_list[i] <= s_list[i + 1]:
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
        is_exchanged = True
        break

if not is_exchanged:
    s_list[-1], s_list[-2] = s_list[-2], s_list[-1]

print("".join(s_list))