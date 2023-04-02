'''
182.小朋友崇拜圈

运行限制:
最大运行时间：1s
最大运行内存: 256M

题目介绍：
在一个游戏中，需要小朋友坐一个圈，每个小朋友都有自己最崇拜的小朋友在他的右手边。
求满足条件的圈最大多少人？
小朋友编号为 1,2,3,⋯N。

输入描述
输入第一行，一个整数 N（3<N<10^5）。
接下来一行 N 个整数，由空格分开。

输出描述
要求输出一个整数，表示满足条件的最大圈的人数。

输入
9
3 4 2 5 3 8 4 6 9

输出
4
'''
'''
贪心去搜就行，尽可能满足每一个小朋友的要求。
'''
n = int(input())
line = input().strip().split(' ')
nums = list(map(lambda x: x - 1, map(int, line)))
seen = set()
maxres = 0
for num in nums:
    count = 0
    while num not in seen:
        seen.add(num)
        count += 1
        num = nums[num]
    maxres = max(maxres, count)
print(maxres)