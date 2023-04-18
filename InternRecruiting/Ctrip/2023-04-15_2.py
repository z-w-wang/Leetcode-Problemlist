'''
2023-04-15 算法岗 2

题目描述：
游游拿到了一个正整数n，她希望找到两个正整数a和b(a<b)，使得a+b=n，且a和b的lcm (最小公倍数)尽可能大。你能帮帮她吗?

输入描述
第1行输入一个正整数t，代表询问的次数。
对于每组询问，输入一行一个正整数n。

对于50%的数据，保证t=1
对于另外20%的数据，1<=t<=10；2<=n<=10000
对于100%的数据，1<=t<=10^5；2<=n<=10^13

输出描述
共输出t行。对于每组询问,输出一行两个正整数a和b，用空格隔开。

输入示例
2
5
4

输出示例
2 3
1 3
'''
# 思路
'''
令a和b尽可能接近，且为奇数。
相邻两个奇数的最小公倍数为乘积，且a(n-a)最大的取值是尽可能令a接近n//2。
时间复杂度O(t)
'''
t = int(input())
res = [[0, 0] for _ in range(t)]
for i in range(t):
    n = int(input())
    if n == 2:
        res[i][0] = 1
        res[i][1] = 1
    elif n & 1:
        res[i][0] = n // 2
        res[i][1] = n // 2 + 1
    elif (n // 2) & 1:
        res[i][0] = n // 2 - 2
        res[i][1] = n // 2 + 2
    else:
        res[i][0] = n // 2 - 1
        res[i][1] = n // 2 + 1
for r in res:
    print(r[0], end = ' ')
    print(r[1])