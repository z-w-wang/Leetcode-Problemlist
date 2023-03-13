'''
测试岗2023-03-13 2.零食

时间限制：3000 MS
内存限制：589824 KB

题目描述:小天最爱吃的零食有两种，分别为A、B。为了健康着想，他每天最多吃一种零食 (当然也可以不吃)，并且不能连续两天吃同一种零食。
他列出了接下来n天的计划，第i天他可以选择的A零食的美味度为ai，可以选择的B零食的美味度为bi。
请计算他n天能吃到的零食的美味度之和的最大值。

输入描述：
第一行有一个整数n (1<=n<=100000)，代表总天数。
第二行有n个整数a1,a2,...,an(1<=ai<=10^9) ，代表A类零食每天的美味度。
第三行有n个整数b1,b2,...,bn(1<=bn<=10^9) ，代表B类零食每天的美味度。

输出描述：
输出一个整数，代表美味度之和的最大值。

样例输入：
5
9 3 5 7 3
5 8 1 4 5

样例输出：
29
'''
# 思路
'''
动态规划，第i天的输入仅与第i-1天和第i-2天有关。

dp = [[0, 0] for _ in range(n + 2)]
for i in range(n):
    dp[i + 2][0] = max(dp[i + 1][1], dp[i][1]) + int(line2[i])
    dp[i + 2][1] = max(dp[i + 1][0], dp[i][0]) + int(line3[i])
print(max(dp[-1]))

可以用常量来减小空间复杂度。
样例只通过27%，不知道为什么。
'''
n = int(input())
line2 = input().split(" ")
line3 = input().split(" ")

day1a = day1b = day2a = day2b = 0
for i in range(n):
    day1a, day1b, day2a, day2b = day2a, day2b, \
        max(day1a, day1b, day2b) + int(line2[i]), max(day1a, day1b, day2a) + int(line3[i])
print(max(day2a, day2b))