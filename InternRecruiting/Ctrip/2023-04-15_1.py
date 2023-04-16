'''
2023-04-15 算法岗 1

题目描述：
大概就是给一个二维字符数组，统计有多少个2*2的子数组含有“you”三个字符。

输入描述：
第一行两个整数n,m，表示字符数组有n行m列
接下来n行，为字符数组

输出描述：
一个数字，代表符合条件的子数组个数。
'''
# 思路
'''
数据大小好像挺小的，直接模拟就行
时间复杂度为O(c*m*n)，本题c=4。
'''
line1 = input().strip().split(' ')
n, m = int(line1[0]), int(line1[1])
strings = ["" for _ in range(n)]
for i in range(n):
    strings[i] = input().strip()
count = 0
for i in range(n - 1):
    for j in range(m - 1):
        s = set()
        s.add(strings[i][j])
        s.add(strings[i + 1][j])
        s.add(strings[i][j + 1])
        s.add(strings[i + 1][j + 1])
        if "y" in s and "o" in s and "u" in s:
            count += 1
print(count)