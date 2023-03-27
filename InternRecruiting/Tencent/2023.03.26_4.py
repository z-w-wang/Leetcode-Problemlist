'''
2023-03-26 算法岗 4
时间限制：C/C++ 1秒，其他语言2秒。
空间限制：C/C++ 262144K，其他语言 524288K。
题目描述：
给定一个长度为n的数组，求有多少长度为k的子区间满足：子区间中元素恰好构成一个顺子?
顺子的定义：排序后相邻两元素的差的绝对值恰好等于1.例如：[3,7,6,4,5]是一个顺子。
输入描述：
第一行两个整数n和k，1<=k<=n<=300000
第二行n个整数，a1,a2,...,an，1<=ai<=1000000
输出描述：
输出一个正整数代表答案。
'''
# 思路
'''
暴力PyPy3能过80%
最后一版代码没保存下来，懒得写了，用了滑窗+两个单调队列+集合查重，令滑窗满足：
1.最大值最小值差值为k-1
2.滑窗长度==k
3.无重复元素
时间复杂度缩小到O(n)，应该能AC。
只保留了暴力的80%的代码。
'''
# 80%
from bisect import bisect_left
line1 = input().strip().split(' ')
n, k = int(line1[0]), int(line1[1])
line2 = input().strip().split(' ')

nums = list(map(int, line2))
window = sorted([nums[i] for i in range(k - 1)])

count = 0
for i in range(n - k + 1):
    window.insert(bisect_left(window, nums[i + k - 1]), nums[i + k - 1])
    flag = False
    for j in range(k - 1):
        if window[j] != window[j + 1] - 1:
            flag = True
            break
    if not flag:
        count += 1
    window.pop(bisect_left(window, nums[i]))
print(count)